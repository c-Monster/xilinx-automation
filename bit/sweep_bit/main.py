#!/usr/bin/env python

import os
import sys
import json
import time

import common
import char

def main():

    # start the timer
    start_time = time.time()

    # arguments
    if len(sys.argv) < 3:
        print common.FAIL + "ERROR: must specify sweep file and number of tiles" + common.ENDC
        sys.exit(1)

    elf = sys.argv[1]
    osc = sys.argv[2]

    results = {}
    with open('sweep.log', 'w') as log:
        for i in range(int(osc)):

            # get bitstream
            key = i
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

    # dump json
    with open('sweep.json', 'w') as output:
	output.write(json.dumps(results))

def printTime(seconds):


    hours = seconds / common.HOURS
    minutes = (seconds - (hours * common.HOURS)) / common.MINUTES
    seconds -= ((minutes * common.MINUTES) + (hours * common.HOURS))

    message = "execution time %02d:%02d:%02d" % (hours, minutes, seconds)
    print message

if __name__ == '__main__':
	main()
