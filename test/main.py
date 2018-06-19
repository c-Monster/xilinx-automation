#!/usr/bin/env python

import os
import sys

import common
import char

def main():

	# arguments
	out = sys.argv[1]
	elf = sys.argv[2]
	
	# Thomas had never seen such a mess ...UGH
	cols = 4
	rows = 24

	i = 0;
	while (i < rows):

		j = 0;
		while (j < cols):

			bit = 'sweep_%d' % (j * rows) + i
			print bit
			with open(out, 'a+') as log:
				char.characterize(bit, elf, log)

			j += 1 

		i += 1

if __name__ == '__main__':
	main()
