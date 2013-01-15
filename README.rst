**Note: this only works on Mac OS X.**

Inspired by a hack suggested at ``#hackAAS`` by `Kathy Cooksey
<https://twitter.com/klcooksey>`_.

Built by `Dan Foreman-Mackey <http://dan.iel.fm>`_ and distributed under
the BSD 2-clause license (see ``LICENSE``).

**This web scraping project makes use of the** `html2text
<http://www.aaronsw.com/2002/html2text/>`_ **module written by one of the
greatest scrapers that that community has known:** `Aaron Swartz
<http://www.aaronsw.com/>`_.


Installation
------------

You can install using ``pip`` with:

::

    pip install arxiv2speech


Usage
-----

::

    Usage: arxiv2speech [-h | --help] [-u URL] [-o OUTPUT] [--clobber]

    -h --help  show this
    -u URL     custom arXiv RSS [default: http://export.arxiv.org/rss/astro-ph]
    -o OUTPUT  base directory for output [default: ./build]
    --clobber  overwrite an existing archive
    --quiet    don't print any status messages
