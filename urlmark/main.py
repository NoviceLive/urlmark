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


from __future__ import division, absolute_import, print_function
from time import asctime

from pkg_resources import resource_filename
import click
from markdown import markdown
from bs4 import BeautifulSoup

from . import VERSION_PROMPT, PROGRAM_NAME


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(VERSION_PROMPT,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.option('-l', '--left', default='left.md',
              show_default=True,
              # TODO: Used encoding='utf-8'
              # to workaround UnicodeDecodeError raised in Python 2.
              type=click.File('r', encoding='utf-8'),
              help='Use this as the left side.')
@click.option('-r', '--right', default='right.md',
              show_default=True,
              # TODO: Used encoding='utf-8'
              # to workaround UnicodeDecodeError raised in Python 2.
              type=click.File('r', encoding='utf-8'),
              help='Use this as the right side.')
@click.option('-t', '--template',
              default=resource_filename(__name__, 'template.html'),
              show_default=True,
              # TODO: Used encoding='utf-8'
              # to workaround UnicodeDecodeError raised in Python 2.
              type=click.File('r', encoding='utf-8'),
              help='Use this template.')
@click.option('-o', '--output', default='index.html',
              show_default=True,
              # TODO: Used encoding='utf-8'
              # to workaround UnicodeDecodeError raised in Python 2.
              type=click.File('w', encoding='utf-8'),
              help='Write to this file.')
def main(left, right, template, output):
    """Write yourself a home page with well-organized booksmarks."""
    output.write(apply_template(template, left, right))


def apply_template(template, left, right):
    """Apply template to the left and right side HTML."""
    return template.read().format(
        left=process_file(left), right=process_file(right),
        time=asctime())


def process_file(one):
    """Render Markdown to HTML and update it for use in Foundation."""
    return update_html(markdown(one.read()))


def update_html(doc):
    """Update HTML for Foundation to render it as drop-down menu."""
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
