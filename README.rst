**Note: this only works on Mac OS X.**

Inspired by a hack suggested at ``#hackAAS`` by [someone?].

Built by `Dan Foreman-Mackey <http://dan.iel.fm>`_ and distributed under
MIT (see ``LICENSE``).


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
