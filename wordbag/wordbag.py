#!/usr/bin/env python

"""
wordbag.py
Generate collectinos of words from text/files.

jeremydouglass@gmail.com

v1.0 2017-09-16
"""

import re
import os

from string import punctuation
from collections import Counter
from itertools import chain
from cStringIO import StringIO

#----------

def wb_filename(filename):
    with open(filename, "r+") as f:
        return wb_string(f.read())

def wb_file(text_file):
    # split
    return wb_list([line for line in text_file])

def wb_list(text_list):
    # split
    wordlist = [word for line in text_list for word in line.split()]
    print wordlist
    # sort, join, return
    return(" ".join(sorted(wordlist)))

def wb_string(text_string):
    wordlist = [word for word in text_string.split()]
    return(" ".join(sorted(wordlist)))

#----------

def wb_filename_replace(filename):
    with open(filename, "r+") as f:
        wb_file_replace(f)

def wb_file_replace(text_file):
    # split
    wordlist = [word for line in text_list for word in line.split()]
    # sort, join, write
    text_file.seek(0)
    text_file.write(" ".join(sorted(wordlist)))
    text_file.truncate()

#----------

# https://stackoverflow.com/a/35857833/7207622

def freq_filename(filename):
    with open(filename, "r+") as f:
        return freq_file(f)

def freq_file(text_file):
    linewords = (line.translate(None, punctuation).lower().split() for line in text_file)
    return Counter(chain.from_iterable(linewords))

def freq_to_alpha_bag (text_counter):
    return sorted(list(text_counter.elements()))

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

def test():
    txt = "Section 1.10.33 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC: At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."
    f = StringIO(txt)
    wb = Wordbag(f)
    print wb.bag()
    print wb.bag(raw=True)
    print wb.bag_string()
    print wb.bag_string(raw=True)
    print wb.counts()
    print wb.counts(raw=True)
    print wb.lines()

# def freq_list(text_):

# def wb_freq(filename):

# with open("file.txt",'r') as file:
#     content=file.read()
# with open("file.txt",'w') as file:
#     file.write()

# with open(filename) as f:
#     file_str = f.read()
#     file_str = alpha_bag(file_str)
# with open(filename, "w") as f:
#     f.write(file_str)
