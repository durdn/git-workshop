#!/usr/bin/env python
import sys
import re

inputfile = file(sys.argv[1])

lines = inputfile.readlines()


def parse_impress(line):
    linel = line.split(' ')
    title = linel[0][1:-1]
    scale = int(linel[2])
    x = int(linel[4])
    y = int(linel[6])


    return (title,x,y,0,scale)



def tokenize(lines):
    curr_token = []
    cue = '^\[.*?\]'
    first = True
    for line in lines:
        if re.search(cue,line):
            if not first:
                print '<!-- </div> -->'
            first = False
            print '<!-- <div id="%s" class="step" data-x="%s" data-y="%s" data-rotate="%s" data-scale="%s"> -->' % parse_impress(line)
        else:
            print line,
    print '<!-- </div> -->'



        

def has(pattern,s):
    return s.count(pattern) > 0

tokenize(lines)

