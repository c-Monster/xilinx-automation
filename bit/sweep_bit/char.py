#!/usr/bin/env python

import sys
import re
import pexpect
import cStringIO as string

import common

debug = False

def setDebug(state):
	debug = state

def runCharacterization(bit, elf, out, reg):

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
    print contents
    out.write(contents)
    return reg.findall(contents)

def main():

    # arguments
    bitstream = sys.argv[1]
    elf = sys.argv[2]

    # open log file with write permissions
    logfile = open(sys.argv[3], 'w')

    p = re.compile('([0-9]+[\n])')
    print runCharacterization(bitstream, elf, logfile, p)

if __name__ == '__main__':
    main()
