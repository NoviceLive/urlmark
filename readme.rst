UrlMark
=======


Write yourself a home page with bookmarks well-organized,
browser-agnostic and easy-to-share.


Demo
----

`Online Bookmarks <http://novicelive.github.io/urlmark/>`_


Installation
------------

Recommended Way
+++++++++++++++

- ``git clone https://github.com/NoviceLive/urlmark.git``

  Add ``--recursive`` to obtain example Markdown files,
  as well as **templates**.

  Add ``--deth 1`` to prevent cloning unnecessary histories.

- ``cd urlmark``

- ``pip install -r requirements.txt``

- ``make install`` (Optional)


Alternatives
++++++++++++

- ``pip install urlmark``

  No example Markdown files and no **templates**,
  which are required if you don't want to write your own.


Get Started
-----------

::

   ./urlmark.py --help
   Usage: urlmark.py [OPTIONS]

     Write you self a home page with well-organized booksmarks.

   Options:
     -l, --left FILENAME      Use this as the left side.  [default: left.md]
     -r, --right FILENAME     Use this as the right side.  [default: right.md]
     -t, --template FILENAME  Use this template.  [default: template.html]
     -o, --output FILENAME    Write to this file.  [default: index.html]
     --help                   Show this message and exit.


Brainstorm & TODO
-----------------

- How about integrating command line interface like `cym13/bookmark`_?

- Mobile view (i.e. responsive or not)?

- Does it look good?

- Write some fantastic themes (a.k.a templates)?


.. _cym13/bookmark: https://github.com/cym13/bookmark


Disclaimer
----------

Bookmarks in example ``left.md`` and ``right.md`` are highly personal.
