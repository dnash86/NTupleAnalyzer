#!/usr/bin/env python

################################
#
# CleanUpRun.py
#
#  Script to clean extra output files and logs from a run of AnalyzerMakerFast.py
#
#  author: David Nash (Northeastern)
#
################################

import sys
import os.path
import argparse
import csv


def getArguments():
    parser = argparse.ArgumentParser(description='Clean up spurious content from an AnalyzerMakerFast.py run')

    # Command line flags
    parser.add_argument('run_folder')
    parser.add_argument('-o', '--clean_output', action='store_true', dest='doOutput', default=False, help='Preset cleaning of output logs')
    parser.add_argument('-r', '--clean_root', action='store_true', dest='doRoot', default=False, help='Preset cleaning of output root files/folders')

    args_ = parser.parse_args()
    return args_



def CleanFolder(run_folder_,doOutput_,doRoot_):
    FolderContent = os.popen('ls '+run_folder_).readlines()
    if doRoot_:
        for line in FolderContent:
            if 'outputdir' in line:
                os.system('rm -r '+run_folder_+'/'+line.replace('\n',''))
    if doOutput_:
        OutputFiles = os.popen('ls '+run_folder_+'_*').readlines()
        for line in OutputFiles:
            os.system('rm '+line.replace('\n',''))
        

def main():
    args = getArguments()
    CleanFolder(args.run_folder,args.doOutput,args.doRoot)

if __name__ == '__main__':
    main()
