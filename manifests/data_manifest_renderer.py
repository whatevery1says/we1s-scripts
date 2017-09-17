#!/usr/bin/env python

from jinja2 import Template

template_file = 'Data_Manifest.template.txt'

with open(template_file, 'r') as myfile:
    data=myfile.read().replace('\n', '')

t = Template("Hello {{ something }}!")
output = t.render(something="World")


# https://realpython.com/blog/python/primer-on-jinja-templating/
