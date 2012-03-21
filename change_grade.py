#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

if len(argv) != 3:
    stderr.write("Usage: myprog.py STRING GRADE\n")
    exit(1)
    
for line in fileinput.input('-'):
    m = re.search(argv[1], line)
    values = line.rstrip().split(",")
    if m:
        values[3] = argv[2]
        print ",".join(values)
    else:
        print line,
