#!/usr/bin/env python

import os
import sys

import common
import char

cols = 24
rows = 4 

def main():

	# arguments
	elf = sys.argv[1]
	out = sys.argv[2]
	
	# Thomas had never seen such a mess ...UGH

	i = 0;
	while (i < cols):
		j = 0;
		while (j < rows):
                    getCharData(elf, out, i, j)
	       	    j += 1 
		i += 1

def getCharData(elf, out, i, j):

    bit = 'sweep_%d' % ((j * cols) + i)
    print common.OKGREEN + 'characterizing %s' % bit + common.ENDC
    with open(out, 'a+') as log:
        char.characterize(bit, elf, log)

if __name__ == '__main__':
	main()
