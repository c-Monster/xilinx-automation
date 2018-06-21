#!/usr/bin/env python

import os
import sys
import json

import common
import char

cols = 24 
rows = 4 

def main():

	# arguments
	elf = sys.argv[1]

	results = {}
	with open('sweep.log', 'w') as log:
		i = 0;
		while (i < cols):
			j = 0;
			while (j < rows):

				# get bitstream
				key = (j * cols) + i
				bit = 'sweep_%d' % key
				log.write('\n\n%%%%%%' + bit + '%%%%%%\n\n')
				print common.OKGREEN + 'characterizing ' + bit + common.ENDC

				# run characterization
				result = char.runCharacterization(bit, elf)
				print result
				log.write(result)

				# extract value
				value = char.extractValue(result)
				results[key] = value

				j += 1 
			i += 1

	# dump json
	with open('sweep.json', 'w') as output:
		output.write(json.dumps(results))


if __name__ == '__main__':
	main()
