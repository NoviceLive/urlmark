UrlMark
=======

.. image:: https://img.shields.io/pypi/v/urlmark.svg
   :target: https://pypi.python.org/pypi/UrlMark

Write yourself a home page with bookmarks well-organized,
browser-agnostic and easy-to-share.


Demo_ based-on `awesome-python`_
-------------------------------

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

Recommended Way
+++++++++++++++

- ``git clone https://github.com/NoviceLive/urlmark.git``

  Add ``--recursive`` to obtain example Markdown files,
  as well as **templates**.

  Add ``--deth 1`` to prevent cloning unnecessary histories.
  However, this might be of no help
  since UrlMark uses its ``gh-pages``
  as a submodule which will result in full clone.

- ``cd urlmark``

- ``pip install -r requirements.txt``

- ``make install`` (Optional)


Alternatives
++++++++++++

- ``pip install urlmark``

  No example Markdown files and no **templates**,
  which are required if you don't want to write your own.

- Download from Github releases_.

.. _releases: https://github.com/NoviceLive/urlmark/releases.

- Download from PyPI_.

.. _PyPI: https://github.com/NoviceLive/urlmark/releases.


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

  You can use the included template in ``gh-pages`` branch,
  but it may not look eyeful. Here is the another demo:
  `Online Bookmarks <http://novicelive.github.io/urlmark/>`_.

  See the included template (in ``gh-pages``) to write your own one.
  It shall setup Foundation_ scaffold and has three placeholders:
  ``{left}``, ``{right}``, ``{time}``.

  And all other uses of brackets must be escaped
  as in Python ``str.format``.

- Run ``./urlmark.py`` with necessary options.

  If you name your left and right side
  as ``left.md`` and ``right.md``, your template as ``template.html``,
  you can just run ``./urlmark.py`` with no options
  on their residing directory.

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


Brainstorm & TODO
-----------------

- How about integrating CLI like `cym13/bookmark`_?

- Mobile view (i.e. responsive or not)?

- Write some fantastic themes (a.k.a templates)?


Disclaimer
----------

Bookmarks in example ``left.md`` and ``right.md``
are highly personal, and may have no other implications except
personal convenience for the time being.


.. _awesome-python: https://github.com/vinta/awesome-python
.. _Foundation: http://foundation.zurb.com/
.. _cym13/bookmark: https://github.com/cym13/bookmark
