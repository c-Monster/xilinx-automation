#!/usr/bin/env python

import sys
import pexpect

import common

def characterize(bit, elf, out):

    # spawn new ssh session
    child = pexpect.spawn(common.XMD)  
    child.expect('XMD%')
    child.expect('XMD%')
 
    # build and send command
    command = "fpga -f %s" % bit
    child.sendline(command)
    child.expect('XMD%')
    print common.OKGREEN + 'downloaded %s' % bit + common.ENDC
    
    child.sendline('connect mb mdm')
    child.expect('XMD%')
    print common.OKGREEN + 'connected to MDM UART target' + common.ENDC
        
    child.sendline('terminal -jtaguart_server')
    child.expect('XMD%')
    print common.OKGREEN + 'started JTAG server' + common.ENDC
 
    command = "dow %s" % elf
    child.sendline(command)
    child.expect('XMD%')
    print common.OKGREEN + 'downloaded %s' % elf + common.ENDC
    
    child.sendline('run')
    child.logfile = out
    child.expect('done', timeout = 120)
    child.logfile = None
    print common.OKGREEN + 'successfully characterized' + common.ENDC
        
    child.sendline('disconnect 0')
    child.expect('XMD%')
    child.sendline('exit')

def main():

    # arguments
    bitstream = sys.argv[1]
    elf = sys.argv[2]

    # open log file with write permissions
    logfile = open(sys.argv[3], 'w')

    characterize(bitstream, elf, logfile)

if __name__ == '__main__':
    main()



