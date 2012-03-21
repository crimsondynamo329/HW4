#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

if len(argv) != 3:
    stderr.write("Usage: myprog.py STRING GRADE <inputfile\n")
    exit(1)
    
changeGrade(argv[1], argv[2])
    
def changeGrade( searchString, newGrade ):
    for line in fileinput.input('-'):
        m = re.search(searchString, line)
        values = line.rstrip().split(",")
        if m:
            values[3] = newGrade
            print ",".join(values)
        else:
            print line,
