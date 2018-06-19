#!/usr/bin/env python 

import sys
import common
import pexpect
import getpass


def deploy(bitfile, outfile):
    
    child = pexpect.spawn(common.XMD) # spawn new ssh session
    child.logfile = outfile

    child.expect('XMD%')
    child.expect('XMD%')
    command = "fpga -f %s" % bitfile
    child.sendline(command)

    child.expect('XMD%')
    child.sendline('exit')
    

def main():

    print common.WARNING + "starting characterization..." + common.ENDC

    outfile = open('monsterLog.txt', 'wb')
    bitstream = sys.argv[1];

    deploy(bitstream, outfile)

    print common.WARNING + "finished characterization" + common.ENDC

if __name__ == '__main__':
    print common.WARNING + "starting single deployment" + common.ENDC
    main()
else:
    print common.WARNING + "importing module" + common.ENDC
