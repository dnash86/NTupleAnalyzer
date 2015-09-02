#!/usr/bin/env python

################################
#
#  TransferToEOS.py
#
#  Script to transfer output of analyzer
#
#  author: David Nash (Northeastern)
#
################################

import sys
import os.path
import argparse
import csv


def getArguments():
    parser = argparse.ArgumentParser(description='Transfer a directory to EOS')

    # Command line flags
    parser.add_argument('-s', '--store_dir', action='store', dest='eosDir', default=False, help='The directory to transfer to')
    parser.add_argument('-d', '--output_dir', action='store', dest='outputDir', default=False, help='The directory to be transferred')

    args_ = parser.parse_args()
    return args_




def transfer(eosDir_,outputDir_):
    os.system('cmsMkdir '+eosDir_+'/'+outputDir_)
    files=os.popen('ls '+outputDir_+'/SummaryFiles').readlines()
    for line in files:
        os.system('cmsStage '+outputDir_ +'/SummaryFiles/'+line.replace('\n','')+' '+eosDir_+'/'+outputDir_)

def main():
    args = getArguments()
    transfer(args.eosDir,args.outputDir)

if __name__ == '__main__':
    main()
