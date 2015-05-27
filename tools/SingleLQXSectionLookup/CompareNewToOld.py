from ROOT import *
import os
import sys
import math



Old = os.popen("gawk -F ',' '{print $NF}' CrossSections\[pb].csv").readlines()

New = os.popen("cat June3Output.txt").readlines()

Ratio = []

for x in range(len(Old)):
    Old[x] = float(Old[x].replace('\n',''))
    New[x] = float(New[x].replace('\n',''))
    Ratio.append(New[x]/Old[x])
    print Ratio[x]
