from ROOT import *
import os
import sys
import math
import subprocess


Values = [(250+50*x) for x in range(13)]
for x in Values:
    print "On step " + str(x) + "=============================================================="

    ConfigFile = str(x) + ".cfg"
    CheckValue = os.popen("combine -M Asymptotic " + ConfigFile + " --rMax 5 | grep 97.5% | gawk '{print $NF}'").readline().replace('\n','')
    print CheckValue
    Check = true

    while Check == true:
        String = "combine -M Asymptotic " + str(x) + ".cfg --rMax " + str(CheckValue)
        print String
        TempFile = os.popen(String).readlines()
        print "==========Checking this value: " + str(CheckValue)
        Multiplied = false
        for line in TempFile:
            print "**"+line
            if ("At r =" in line) and ("inf" in line or "nan" in line or "q_mu = 0.00000" in line):
                if Multiplied == false:
                    CheckValue = CheckValue * 1.1
                    Multiplied = true
                    print "=====BAD LINE FOUND++++++++++"
        if Multiplied == false:
            Check = false
                
    
