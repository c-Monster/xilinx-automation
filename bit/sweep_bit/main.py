#!/usr/bin/env python

import os
import sys
import json
import time

import common
import xil

def main():

    # start the timer
    start_time = time.time()

    # arguments
    if len(sys.argv) < 3:
        print common.FAIL + "ERROR: must specify sweep file, number of tiles, and cooldown time (in seconds) for each characterization" + common.ENDC
        sys.exit(1)

    elf = sys.argv[1]
    osc = sys.argv[2]
    #tim = sys.argv[3]

    results = {}
    with open('sweep.log', 'w') as log:
        i = int(osc)
        while (i > 0):
            i -= 1

            # get bitstream
            key = i
            bit = 'sweep_%d.bit' % key
            log.write('\n\n%%%%%%' + bit + '%%%%%%\n\n')
            print common.OKGREEN + 'characterizing ' + bit + common.ENDC

            # run characterization
            result = xil.runCharacterization(bit, elf)
            print result
            log.write(result)

            # extract value
            value = xil.extractValue(result)
            results[key] = value

            # cool 
            #xil.coolDown(tim)

    # dump json
    with open('sweep.json', 'w') as output:
	output.write(json.dumps(results))

    # print time
    printTime(time.time() - start_time)

def printTime(seconds):


    hours = seconds / common.HOURS
    minutes = (seconds - (hours * common.HOURS)) / common.MINUTES
    seconds -= ((minutes * common.MINUTES) + (hours * common.HOURS))

    message = "execution time %02d:%02d:%02d" % (hours, minutes, seconds)
    print message

if __name__ == '__main__':
	main()
