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


from sys import argv
from os.path import join, dirname

from setuptools import setup


PROGRAM_NAME = 'UrlMark'
PACKAGE_NAME = PROGRAM_NAME.lower()

__author__ = 'Gu Zhengxiong'

my_dir = dirname(argv[0])
version_file = 'version.txt'
version_path = join(my_dir, PACKAGE_NAME, version_file)
with open(version_path) as stream:
    __version__ = stream.read().strip()

with open(join(my_dir, 'requirements.txt')) as stream:
    requirements = stream.read().splitlines()


setup(
    name=PROGRAM_NAME,
    version=__version__,
    packages=[PACKAGE_NAME],
    package_data={
        'urlmark': ['template.html', version_file, 'aliases.db']
    },
    install_requires=['click', 'markdown', 'beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'urlmark={}.main:main'.format(PACKAGE_NAME),
            'found={}.found:main'.format(PACKAGE_NAME),
            'foundb={}.database:main'.format(PACKAGE_NAME)
        ]
    },

    author=__author__,
    author_email='rectigu@gmail.com',
    description='UrlMark',
    license='GPL-3',
    keywords='Home page, Bookmarks, URLs, Favorite sites',
    url='https://github.com/NoviceLive/{}'.format(PACKAGE_NAME),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
