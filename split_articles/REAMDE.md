# split_articles.py

-  Designed for command line use with arguments
-  Help: use --help from the command line for details
-  Script design was partly informed by online discussions here:
   -  https://stackoverflow.com/a/5871245/7207622
   -  https://stackoverflow.com/questions/22868587/python-creating-a-file-for-each-item-in-a-list
-  infile:
   -  can be a filename or list of filenames
-  counter:
   -  output will be automatically numbered
   -  numbering continues across all article chunks in multifile input
   -  output numbering style can be adjusted with -o
   -  output numbering can be adjusted with -c
-  splitpattern:
   -  can be plain text or a python regular expression
   -  to simplify command line use, save splitpattern in a splitpatternfile, e.g. `myptext.pattern.txt`
   -  for complex regex, if you need groups (foo) then use non-capturing groups (?:foo):
      
      		\s*Copyright \d{4} The News? York Times Company\s*(?:\r\n)*\s*(?:All Rights Reserved)?
