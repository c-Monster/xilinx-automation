#!/usr/bin/env python

import os
import sys
import json
# Find the best implementation available on this platform
try:
        from cStringIO import StringIO
except:
        from StringIO import StringIO

import common
import char

def main():

	# arguments
	out = sys.argv[1]
	elf = sys.argv[2]
	
	# Thomas had never seen such a mess ...UGH

        entries = {}
	cols = 4
	rows = 24

        i = 0;
        while (i < rows):
            j = 0;
    	    while (j < cols):
                index = (j * rows) + i
                bit = 'sweep_%d' % index
                print bit
        	value = char.characterize(bit, elf, log)
                entries[index] = value;
        	j += 1 
       	    i += 1

        output = json.dumps(entries)
        with open('output.txt', 'w+') as outfile:
            outfile.write(output)
            
#        total = rows * cols
#        i = 0
#        while (i < total):
#            i += 1



if __name__ == '__main__':
	main()
