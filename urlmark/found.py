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
from logging import basicConfig, DEBUG, root as logger
from sqlite3 import connect, OperationalError
from subprocess import Popen

import click
from pkg_resources import resource_filename

from . import VERSION_PROMPT, PROGRAM_NAME


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(VERSION_PROMPT,
                      '-V', '--version', prog_name=PROGRAM_NAME)
@click.argument('command')
@click.argument('args', nargs=-1)
def main(command, args):
    """Intentional command-not-found handler."""
    basicConfig(level=DEBUG)
    # logger.debug('argv: %s', argv)
    # args = ' '.join(argv[1:])
    logger.debug('command: %s', command)
    logger.debug('args: %s', args)
    handle_args(command + ' ' + ' '.join(args))


def handle_args(args):
    parts = args.split()
    start = parts[0]
    if start[0] == '@':
        operator = start[1:] if start[1:] else 'google'
        args = ' '.join(parts[1:])
        logger.debug('operator: %s', operator)
        logger.debug('args: %s', args)
        handle_operator(operator, args)
    else:
        raise RuntimeError('undefined!')


def handle_operator(operator, args):
    if args:
        try:
            url = globals()['handle_' + operator](args)
        except KeyError:
            raise
    else:
        path = resource_filename(__name__, 'aliases.db')
        logger.debug('path: %s', path)
        with connect(path) as database:
            cursor = database.cursor()
            sql = 'select link from aliases where name = ?'
            args = (operator,)
            logger.debug('sql: %s', sql)
            logger.debug('args: %s', args)
            try:
                cursor.execute(sql, args)
            except OperationalError:
                logger.exception('')
                return 1
            else:
                link = cursor.fetchone()
                if link:
                    url = link[0]
                else:
                    print('Sorry, you have not defined this alias!')
                    return 1
    popen_args = ['firefox', url]
    logger.debug('Popen args: %s', popen_args)
    Popen(popen_args)
    return 0


# TODO: POST.
# TODO: Escape.
# TODO: Find a better way.


def handle_kern(args):
    return 'https://www.kernel.org/doc/htmldocs/kernel-api/'\
        'API-{}.html'.format(args)


def handle_aur(args):
    return 'https://aur.archlinux.org/packages/?O=0&K=' + args


def handle_lxr(args):
    return 'http://lxr.free-electrons.com/ident?i=' + args


def handle_github(args):
    return 'https://github.com/search?&q=' + args


def handle_tmall(args):
    return 'https://list.tmall.com/search_product.htm?q=' + args


def handle_google(args):
    return 'https://www.google.com/#newwindow=1&q=' + args


def handle_bing(args):
    return 'https://bing.com/search?q=' + args


def handle_baidu(args):
    return 'https://www.baidu.com/s?wd=' + args


def handle_urban(args):
    return 'https://www.urbandictionary.com/define.php?term=' + args


def handle_etym(args):
    return 'http://www.etymonline.com/index.php?search=' + args


def handle_ahd(args):
    return 'https://ahdictionary.com/word/search.html?q=' + args


def handle_oxford(args):
    return 'https://www.oxforddictionaries.com/' \
        'us/definition/american_english/' + args
