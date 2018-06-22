#!/usr/bin/env python

import sys
import re
import pexpect
import time
import cStringIO as string

import common

def main():

    # arguments
    bitstream = sys.argv[1]
    elf = sys.argv[2]

    # open log file with write permissions
    logfile = open(sys.argv[3], 'w')

    print runCharacterization(bitstream, elf, logfile, p)

def runCharacterization(bit, elf):

    # spawn new xmd session
    xmd = pexpect.spawn(common.XMD)  
    xmd.expect('XMD%')
    xmd.expect('XMD%')
 
    # program FPGA with bitstream
    command = "fpga -f %s" % bit
    xmd.sendline(command)
    xmd.expect('XMD%')
    print common.OKGREEN + 'downloaded %s' % bit + common.ENDC
    
	# connect to MDM
    xmd.sendline('connect mb mdm')
    xmd.expect('XMD%')
    print common.OKGREEN + 'connected to MDM' + common.ENDC
        
    xmd.sendline('terminal -jtaguart_server')
    xmd.expect('XMD%')
    print common.OKGREEN + 'started JTAG server' + common.ENDC
 
 	# download ELF file
    command = "dow %s" % elf
    xmd.sendline(command)
    xmd.expect('XMD%')
    print common.OKGREEN + 'downloaded %s' % elf + common.ENDC 

    logStream = string.StringIO()
    xmd.sendline('run')
    xmd.logfile = logStream
    xmd.expect('done', timeout = 120)
    xmd.logfile = None
    print common.OKGREEN + 'successfully characterized' + common.ENDC

    xmd.sendline('disconnect 0')
    xmd.expect('XMD%')
    xmd.sendline('exit') 
    contents = logStream.getvalue()
    return contents

def extractValue(logStr):
    reg = getRegex()
    return reg.search(logStr).group()

# builds the regex used to extract the frequency
def getRegex():
    return re.compile('([0-9][0-9]+[\r\r\n])')

def coolDown(interval):

	xmd = pexpect.spawn(common.XMD)

	xmd.expect('XMD%')
   	xmd.expect('XMD%')

	xmd.sendline("fpga -f blank.bit")
	xmd.expect('XMD%')
	print common.OKGREEN + 'downloaded blank bitstream' + common.ENDC

	time.sleep(interval)
	print common.OKGREEN + 'done cooling down' + common.ENDC

debug = False
def setDebug(state):
	debug = state

if __name__ == '__main__':
    main()
