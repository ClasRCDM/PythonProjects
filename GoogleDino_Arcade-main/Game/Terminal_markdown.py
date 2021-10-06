""" Made by @AXGKI """
############################
# Markdown terminal printer#
############################

from os import environ
from unittest import TestCase

from mdvl import main

# see README.md:
inspect = environ.get('inspect')


def dedent(s):
    md = s.splitlines()
    if len(md) < 2: return s
    ind = len(md[1]) - len(md[1].lstrip())
    return '\n'.join([m[ind:] for m in md])


class M(TestCase):
    def c(s, md, **kw):
        md = dedent(md)
        mdr, f = main(md, no_print=True, **kw)

        print(mdr, end=' ')

    def text_md(s, text_markd):
        s.c(text_markd)
