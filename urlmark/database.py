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
from logging import root as logger
from sys import argv
from os.path import dirname, join, realpath
from sqlite3 import connect, IntegrityError
from re import match

import click
from pkg_resources import resource_filename

from . import VERSION_PROMPT, PROGRAM_NAME


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(VERSION_PROMPT,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.argument('args', nargs=-1)
def main(args):
    """Database manager for Intentional command-not-found handler."""
    path = resource_filename(__name__, 'aliases.db')
    logger.debug('path: %s', path)
    with connect(path) as database:
        cursor = database.cursor()
        sql = 'create table if not exists ' \
              'aliases (name text unique, link text)'
        cursor.execute(sql)
        handle(cursor, args, parse_comment)


def parse_comment(line):
    regex = r'\s*-\s\[(?P<name>.+)\]\((?P<link>.+)\)\s'\
            '<!--(?P<mark>.+)-->'
    one = match(regex, line)
    # If we have commented the alias, use it.
    try:
        return one.group('mark').strip(), one.group('link')
    except AttributeError:
        # If not, fallback to the lower case of the name,
        # which just works most of the time
        # and saves us from unnecessarily commenting.
        # TODO: Replace spaces with underscores and the like.
        regex = r'\s*-\s\[(?P<name>.+)\]\((?P<link>.+)\)'
        one = match(regex, line)
        try:
            return one.group('name').lower().strip(), one.group('link')
        except AttributeError:
            # This should never happen in my opinion.
            raise ValueError


# def parse_comment(line):
#     from parse import parse
#     tag = parse('{}[{name}]({link}){}<!--{mark}-->{}', line)
#     try:
#         return tag.named['mark'].strip(), tag.named['link'].strip()
#     except AttributeError:
        # raise ValueError


def parse_simple(line):
    return line.split()


def handle(cursor, filenames, parser):
    for filename in filenames:
        with open(filename) as stream:
            for line in stream:
                try:
                    name, link = parser(line)
                except ValueError:
                    pass
                else:
                    if link.strip() == '#':
                        continue
                    sql = 'insert into aliases values (?, ?)'
                    args = (name, link)
                    try:
                        cursor.execute(sql, args)
                    except IntegrityError:
                        pass
                    else:
                        print('Inserted', name, link)
