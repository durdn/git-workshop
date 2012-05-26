#!/usr/bin/env python
import sys
import re

inputfile = file(sys.argv[1])

lines = inputfile.readlines()

def uncomment(lines):
    commented = '\<\!\-\-\ (.*?)\-\-\>'
    for line in lines:
        match = re.search(commented,line)
        if match:
            print match.groups()[0]
        else:
            print line,

uncomment(lines)

