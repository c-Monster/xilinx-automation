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
	# Thomas had never seen such a mess ...UGH

	with open('sweep.log', 'w') as log:
		i = 0;
		while (i < cols):
			j = 0;
			while (j < rows):
				bit = 'sweep_%d' % ((j * cols) + i)
				log.write(bit + '\n')
				print common.OKGREEN + 'characterizing ' + bit + common.ENDC
				result = char.runCharacterization(bit, elf)
				print result
				log.write(result)
				j += 1 
			i += 1



if __name__ == '__main__':
	main()
