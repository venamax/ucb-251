#!/usr/bin/python
import os

os.system(u'chmod a+x download.sh')

for i in range (2,4):
    try:
        os.system(u'./download.sh %s'%i)
    except ValueError:
        continue
