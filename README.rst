UrlMark
=======

.. image:: https://img.shields.io/pypi/v/urlmark.svg
   :target: https://pypi.python.org/pypi/UrlMark

Write yourself a home page with bookmarks well-organized,
browser-agnostic and easy-to-share.


Demos
-----

Shared browser bookmarks
++++++++++++++++++++++++

See http://librecrops.github.io/shared-bookmarks/.

Source lies here, https://github.com/LibreCrops/shared-bookmarks.

Demo_ based-on `awesome-python`_
++++++++++++++++++++++++++++++++

A concise awesome list using UrlMark:
http://novicelive.github.io/urlmark/awepy/.

.. _Demo: http://novicelive.github.io/urlmark/awepy/

- Credits

  Links are from `awesome-python`_.

- Notice

  I made execessive manual editing and rearrangement.
  Therefore, it may contain errors, but it's merely a demo.


Installation
------------

- ``pip install git+https://github.com/NoviceLive/urlmark.git``

  Lastest Git version.

- ``pip install urlmark``

- Download from Github releases_.

.. _releases: https://github.com/NoviceLive/urlmark/releases

- Download from PyPI_.

.. _PyPI: https://pypi.python.org/pypi/UrlMark


Get Started
-----------

- Write the left and right side links in Markdown lists.

  It looks like this and in ``gh-pages`` of this repository,
  there are examples of ``left.md`` and ``right.md``.

  ::

     - [FOSS](#)
         - [Repositories](#)
             - [GitHub](https://github.com/)
             - [Bitbucket](https://bitbucket.org/)
             - [GitLab](https://about.gitlab.com/)
             - [SourceForge](http://sourceforge.net/)
             - [CodePlex](https://www.codeplex.com/)
             - [GitCafe](https://gitcafe.com/)

- Write a template.

  You can use the included template, but it may not look eyeful.

  See the bundled template to write your own one.
  It shall setup Foundation_ scaffold and has three placeholders:
  ``{left}``, ``{right}``, ``{time}``.

  And all other uses of brackets must be escaped
  as in Python ``str.format``.

- Run ``./urlmark.py`` with necessary options.

  If you name your left and right side
  as ``left.md`` and ``right.md``,
  you can just run ``./urlmark.py`` with no options
  on the residing directory.

  ::

     ./urlmark.py --help
     Usage: urlmark.py [OPTIONS]

       Write you self a home page with well-organized bookmarks.

     Options:
       -l, --left FILENAME      Use this as the left side.  [default: left.md]
       -r, --right FILENAME     Use this as the right side.  [default: right.md]
       -t, --template FILENAME  Use this template.  [default: template.html]
       -o, --output FILENAME    Write to this file.  [default: index.html]
       --help                   Show this message and exit.


Command Line Launcher & Intentional Command-Not-Found
-----------------------------------------------------

UrlMark is intended to be commandline-friendly,
which is achieved using **intentional** command-not-found handler
together with our extended interpretation of Markdown_.

Warning
+++++++

This feature is experimental and work in progress,
and probably contains hardcoded behaviors,
which will be removed gradually.

Consider it as a **demonstration** of some idea from the author.

Shell Setup
+++++++++++

- Install the Git version of UrlMark.
- Use the following pieces of code as your command-not-found handler.

  ::

     found "${@}" || return 127

  Specifically, for Zsh_, add the following to you shell profile.

  ::

     command_not_found_handler() {
         found "${@}" || return 127
     }

  For Bash_ users, the following.

  ::

     command_not_found_handle() {
         found "${@}" || return 127
     }

Basic Show Cases
++++++++++++++++

::

   $ # Search in Google or Bing, and many others.
   $ @google Who is the president of US
   $ @bing Who is the president of US

   $ # Open a website.
   $ @github

   $ # Search in dictionaries.
   $ @oxford pulchritude
   $ @urban '<3'

Extended Interpretation
+++++++++++++++++++++++

Simply, UrlMark will interpret HTML comments as short names of
links.

What follows is an example of this.

::

   - [FOSS](#)
       - [Repository Hosting](#)
           - [GitHub](https://github.com/) <!-- gb -->
           - [Bitbucket](https://bitbucket.org/) <!-- bt -->
           - [GitLab](https://gitlab.com/)
           - [SourceForge](https://sourceforge.net/) <!-- sf -->
           - [CodePlex](https://www.codeplex.com/)

Suppose that the above content resides in a file named ``left.md``,
you can then prepare the dataset used by UrlMark using,
``foundb left.md``,
(UrlMark is intended to automatically handle
data preparation by itself in later updates.),
after which you can then type ``@gb`` on you terminal to
launch your browser,
which is hardcoded as ``firefox`` for the time being,
to the website of Github.

To be described in detail later.
But you are always free and **encouraged** to go ahead
and read the source code.


Brainstorm & TODO
-----------------

- Bugs

  - Remove the hardcoded ``firefox`` and use a launcher corresponding to the running system.

    E.g. ``xdg-open`` on GNU/Linux, ``open`` on MacOS.

- Features

  - Mobile view (i.e. responsive or not)?
  - Write some fantastic themes (a.k.a templates)?


Disclaimer
----------

Bookmarks in example ``left.md`` and ``right.md``
are highly personal, and may have no other implications except
personal convenience for the time being.


.. _awesome-python: https://github.com/vinta/awesome-python
.. _Foundation: http://foundation.zurb.com/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Bash: https://www.gnu.org/software/bash/
.. _Zsh: http://www.zsh.org/
