"""
Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>

This file is part of UrlMark.

UrlMark is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrlMark is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with UrlMark.  If not, see <http://www.gnu.org/licenses/>.
"""


import time

import click
from markdown import markdown
from bs4 import BeautifulSoup


@click.command()
@click.argument('left', default='left.md', type=click.File('r'))
@click.argument('right', default='right.md', type=click.File('r'))
@click.argument('template', default='template.html',
                type=click.File('r'))
@click.option('-o', '--output', default='index.html',
              type=click.File('w'))
def main(left, right, template, output):
    output.write(apply_template(template, left, right))


def apply_template(template, left, right):
    return template.read().format(
        process_file(left), process_file(right), time.asctime())


def process_file(one):
    return update_html(markdown(one.read()))


def update_html(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    soup.find('ul').unwrap()

    for tag in soup('ul'):
        tag['class'] = 'submenu menu vertical'

    for tag in soup('a'):
        if tag.attrs['href'] == '#':
            tag['class'] = 'has-submenu'
            tag['data-submenu'] = ''
        else:
            tag['target'] = '_blank'

    return soup
