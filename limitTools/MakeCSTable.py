import os
import sys
import math
import numpy
from math import log10, floor

#these=os.popen("cat CrossSectionTableForPaper_Split.csv").readlines()
these=os.popen("cat ElectronSelectionTable.csv").readlines()
#these=os.popen("cat SignalTable.csv").readlines()

def round_sig(x, sig):
    if x==0:
        return 0.0
    return round(x, sig-int(floor(log10(x)))-1)


def NPlaces(x):
    StringX = str(x)
    Ints = len(StringX.split('.')[0])
    Dec = len(StringX.split('.')[1])
    if Dec > 1:
        return Dec
    else:
        if StringX.split('.')[1]!="0":
            return Dec
        else:
            return -1*(Ints-2)


NeedRound=True

for line in these:
    element=[]
    #print line
    for thing in line.split(','):
        if len(thing) > 1:
            #print thing
            if NeedRound:
                thing=float(thing)
                rounder = round_sig(thing,2)
                if NPlaces(rounder) < 1:
                    roundee = int(thing)
                else:
                    roundee = round(thing,NPlaces(rounder))
                    
                #element.append(round(float(thing),4)
                element.append(roundee)
            else:
                element.append(thing)
        else:
            element.append('')
    string=''
    for thing in element:
        if thing!='':
            if NeedRound:
                rounder = round_sig(thing,2)
                if NPlaces(rounder) < 1:
                    roundee = int(thing)
                else:
                    roundee = round(thing,NPlaces(rounder))
                    
                #element.append(round(float(thing),4)

                #string+=str(round(float(thing),4))+'&'
                string+=str(roundee)+'&'
            else:
                string+=thing.replace('\n','')+'&'
        else:
            string+='&'
        
    print string+'\\\\'
    #print "\\hline"
    #print line.replace('\n','').replace(',','&')+'\\\\'
    
