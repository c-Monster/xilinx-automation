#!/usr/bin/env python 

import sys
import pexpect
import getpass

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def deploy(bitfile, outfile):
    
    child = pexpect.spawn('/opt/Xilinx/14.4/ISE_DS/EDK/bin/lin64/xmd') # spawn new ssh session
    child.logfile = outfile

    child.expect('XMD%')
    child.expect('XMD%')
    command = "fpga -f %s" % bitfile
    child.sendline(command)

    child.expect('XMD%')
    child.sendline('exit')
    

def main():

    print colors.WARNING + "starting characterization..." + colors.ENDC

    outfile = open('monsterLog.txt', 'wb')
    bitstream = sys.argv[1];

    deploy(bitstream, outfile)

    print colors.WARNING + "finished characterization" + colors.ENDC

if __name__ == '__main__':
    print colors.WARNING + "starting single deployment" + colors.ENDC
    main()
else:
    print colors.WARNING + "importing module" + colors.ENDC
