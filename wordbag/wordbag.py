#!/usr/bin/env python

"""
wordbag.py
Collections of words from text / files.

jeremydouglass@gmail.com

v1.0 2017-09-16
"""

import os

from string import punctuation
from collections import Counter
from itertools import chain
from cStringIO import StringIO

#----------

class Wordbag:
    
    def __init__(self, fileobj):
        self.lines_list = fileobj.readlines()
        
    def bag(self, raw=False):
        return sorted(list(self.counts(raw).elements()))
        
    def bag_string(self, raw=False):
        return " ".join(sorted(list(self.counts(raw).elements())))
        
    def counts(self, raw=False):
        if raw:
            linewords = (line.split() for line in self.lines_list)
        else:
            linewords = (line.translate(None, punctuation).lower().split() for line in self.lines_list)
        return Counter(chain.from_iterable(linewords))
        
    def lines(self):
        return self.lines_list
