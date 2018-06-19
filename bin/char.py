#!/usr/bin/env python

import sys
import pexpect

def characterize(bit, elf, out):

    # spawn new ssh session
    child = pexpect.spawn(common.XMD) 
    child.logfile = out
    child.expect('XMD%')
    child.expect('XMD%')

    # build and send command
    command = "fpga -f %s" % bit
    child.sendline(command)

    child.expect('XMD%')
    child.sendline('connect mb mdm')

    child.expect('XMD%')
    child.sendline('terminal -jtaguart_server')

    child.expect('XMD%')
    command = "dow %s" % elf
    child.sendline(command)
    
    child.expect('XMD%')
    child.sendline('run')

    child.expect('done')
    child.sendline('disconnect 0')

    child.expect('XMD%')
    child.sendline('exit')

def main():

    characterize(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main();



