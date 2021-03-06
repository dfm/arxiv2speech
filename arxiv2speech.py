#!/usr/bin/env python

from __future__ import print_function, absolute_import, unicode_literals

__all__ = ["run"]

__version__ = "0.0.4"
__author__ = "Dan Foreman-Mackey (danfm@nyu.edu)"
__copyright__ = "Copyright 2013 Daniel Foreman-Mackey"
__contributors__ = []

import os
import re
import json
import shutil
import subprocess
from multiprocessing import Pool

import feedparser
from html2text import html2text


# Regular expressions.
id_re = re.compile(r"http://arxiv.org/abs/(.*)")
title_re = re.compile(r"(.*) \(arXiv(?:.*?)\)$")
author_re = re.compile(r"<a href=\"(?:.*?)\">(.*?)</a>")


def run(basedir, url="http://export.arxiv.org/rss/astro-ph",
        clobber=False, quiet=False, limit=None):
    # Make the base directory.
    try:
        os.makedirs(basedir)
    except:
        if not clobber:
            raise
        shutil.rmtree(basedir)
        os.makedirs(basedir)

    # Fetch the abstracts.
    if not quiet:
        print("Fetching recent abstracts from: {0}".format(url))
    abstracts = get_recent(url)
    if not quiet:
        print("    ... Found {0} abstracts.".format(len(abstracts)))

    if limit is not None:
        print("Limiting to {0} total.".format(limit))
        abstracts = abstracts[:int(limit)]

    if not quiet:
        print("Saving audio files (slowly) in: {0}".format(basedir))
    p = Pool()
    p.map(_run_one, zip([basedir] * len(abstracts), abstracts))
    if not quiet:
        print("    ... Done.")


def _run_one(args):
    basedir, abstract = args

    # Create the directory for the audio files.
    basedir = os.path.join(basedir, abstract["id"])
    os.makedirs(basedir)

    # Save the metadata.
    json.dump(abstract, open(os.path.join(basedir, "info.json"), "w"),
              sort_keys=True, indent=4, separators=(",", ": "))

    # Save the audio files.
    by = "\n\nBy: " + abstract["authors"][0]
    l = len(abstract["authors"])
    if l == 2:
        by += " and " + abstract["authors"][1]
    elif l > 2:
        by += " and {0} others.".format(l - 1)

    r = text2audio(abstract["title"] + by,
                   os.path.join(basedir, "brief.m4a"))
    assert r == 0, "Couldn't save brief for: {0}".format(abstract["id"])

    r = text2audio(", ".join(abstract["authors"]),
                   os.path.join(basedir, "authors.m4a"))
    assert r == 0, "Couldn't save authors for: {0}".format(abstract["id"])

    r = text2audio(abstract["abstract"], os.path.join(basedir, "abstract.m4a"))
    assert r == 0, "Couldn't save abstract for: {0}".format(abstract["id"])


def get_recent(rss_url):
    d = feedparser.parse(rss_url)

    results = []
    for e in d.entries:
        results.append({
                "id": id_re.findall(e.id)[0],
                "title": title_re.findall(e.title)[0],
                "authors": author_re.findall(e.author),
                "abstract": html2text(e.summary),
            })

    return results


def text2audio(text, filename):
    p = subprocess.Popen(["say", "-o", filename],
                         stdin=subprocess.PIPE)
    p.communicate(text)
    code = p.wait()
    return code
