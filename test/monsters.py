#!/usr/bin/env python

strings = ['hello', 'from', 'cMonster']

with open('file.txt', 'a+') as f:
    for s in strings:
        f.write(s + '\n')
