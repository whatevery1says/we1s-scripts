#!/usr/bin/env python

"""
alpha_articles.py
Split a single article collection text file into individual article files.

jeremydouglass@gmail.com

v1.0 2017-09-16
"""

import re
import os
import argparse

def filename_series_opener(args):
    counter = args.counter
    while True:
        yield open(args.outfilepattern % counter, 'w')
        counter += 1

def alpha(file):
    
    
    
    with open(filename, 'r') as file

def alpha(filename):
    with open(filename, "r+") as f:
        # data = f.read()
        paragraph = " ".join(line.strip() for line in f)
        output = 
        f.seek(0)
        f.write(output)
        f.truncate()


with open("file.txt",'r') as file:
    content=file.read()
with open("file.txt",'w') as file:
    file.write()
    
    alpha(file)
print("aaa" in content)
with open("file.txt","a") as file:
    file.write("\nccccc")


def alpha_bag_file():


def alpha_bag(filename):    
    with open(filename) as f:
        file_str = f.read()
        file_str = alpha_bag(file_str)
    with open(filename, "w") as f:
        f.write(file_str)
    
    
    

def main(args):
    
    # intialize file series
    fs = filename_series_opener(args)
    
    # load filepattern from arg or external file
    if args.splitpatternfile:
        with open(args.splitpatternfile) as patternfile:
            splitpattern = patternfile.read()
    else:
        splitpattern = args.splitpattern
    myre = re.compile(splitpattern)
    
    # split file on pattern
    splitfilelist = []
    for argfile in args.infile:
        with open(argfile) as file:
            splitfilelist += myre.split(file.read())
        if args.verbose:
            print "Adding %d split files" % split_files.length
    
    for count, item in enumerate(splitfilelist):
        if args.trim and item.isspace():
            print "Skipping %d: whitespace" % (count + args.counter)
        else:
            outfile = next(fs)
            outfile.write(item)

def run(filelist):


## ENTRY POINT

if __name__ == '__main__':

    ## COMMAND LINE ARGUMENT PARSING

    parser = argparse.ArgumentParser(description='Split a single article collection text file into individual article files. Splitting is based on a text pattern that occurs between each article text. The pattern may be a python regular expression.', epilog='EXAMPLE:\n  python '+os.path.basename(__file__)+'-i articles.txt -s "Copyright \d\{4\}" -o "%%03d.article.txt" -c 0 -t \n\n\n\n ', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--infile', nargs='+', required=True, help='input file path (plain text)')
    
    feature_parser = parser.add_mutually_exclusive_group(required=True)
    feature_parser.add_argument('-s', '--splitpattern', help='Text to split articles on. Support python regular expressions. For complex expressions, non-capturing groups (?:foo).')
    feature_parser.add_argument('-S', '--splitpatternfile', help='File containing text to split articles on. Support python regular expressions. For complex expressions, non-capturing groups (?:foo).')

    parser.add_argument('-o', '--outfilepattern', default='%d.article.txt', help='output file pattern (optional) -- use %%d or to place counter')

    parser.add_argument('-c', '--counter', type=int, default=1, help='counter starting number (optional)')
    parser.add_argument('-t', '--trim', action='store_true', help='remove whitespace-only segments')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
    
    CL_ARGS = parser.parse_args()
    main(CL_ARGS)
