from ROOT import *
import os
import sys
import math
import subprocess

#Limits.open('Limits.txt','w')

os.system("cp LimitPlots/TEMPLATE.C LimitPlots/CurrentLimitsNew_ele.C")
os.system("sed -i -e 's/CurrentLimits/CurrentLimitsNew_ele/g' LimitPlots/CurrentLimitsNew_ele.C")


Values = [(250+50*x) for x in range(13)]
for x in Values:
    print "On step " + str(x) + "=============================================================="

    ConfigFile = str(x) + "_ele.cfg"
    CheckValue = float(os.popen("combine -M Asymptotic " + ConfigFile + " --rMax 5 | grep 97.5% | gawk '{print $NF}'").readline().replace('\n',''))
    Check = true

    while Check == true:
        String = "combine -M Asymptotic " + str(x) + "_ele.cfg --rMax " + str(CheckValue)
        print String
        TempFile = os.popen(String).readlines()
        print "==========Checking this value: " + str(CheckValue)
        Multiplied = false
        for line in TempFile:
            #print "**"+line
            if ("At r =" in line) and ("inf" in line or "nan" in line or "q_mu = 0.00000" in line):
                if Multiplied == false:
                    CheckValue = CheckValue * 1.1
                    Multiplied = true
                    #print "=====BAD LINE FOUND++++++++++"
            if "Observed Limit: r < " in line:
               ObsLim  =  float(line.split(" ")[4])
            if "Expected  2.5%: r < " in line:
               MinusTwo  =  float(line.split(" ")[5])        #There's an extra space here to align the 2.5% result, that's silly...
            if "Expected 16.0%: r < " in line:
               MinusOne  =  float(line.split(" ")[4])
            if "Expected 50.0%: r < " in line:
               Center  =  float(line.split(" ")[4])
            if "Expected 84.0%: r < " in line:
               PlusOne  =  float(line.split(" ")[4])
            if "Expected 97.5%: r < " in line:
               PlusTwo  =  float(line.split(" ")[4])
        if Multiplied == false:
            Check = false
                
    CS=float(os.popen("grep ue LQinfo.csv | grep " + str(x) + " | gawk -F ',' '{print $5}'").readline().replace('\n',''))
    
    print "========================================"
    print ObsLim
    print "--------------"
    print MinusTwo
    print MinusOne
    print Center
    print PlusOne
    print PlusTwo

    os.system("sed -i -e 's/Obs" + str(x) + "/" + str(ObsLim*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/MinTwo" + str(x) + "/" + str(-MinusTwo*CS+Center*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/MinOne" + str(x) + "/" + str(-MinusOne*CS+Center*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/Center" + str(x) + "/" + str(Center*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/PlusOne" + str(x) + "/" + str(PlusOne*CS-Center*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/PlusTwo" + str(x) + "/" + str(PlusTwo*CS-Center*CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
    os.system("sed -i -e 's/ThCS" + str(x) + "/" + str(CS) + "/g' LimitPlots/CurrentLimitsNew_ele.C")
