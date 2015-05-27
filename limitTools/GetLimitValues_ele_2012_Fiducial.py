from ROOT import *
import os
import sys
import math
import subprocess

#Limits.open('Limits.txt','w')

Records = open('FiducialLog.txt','w')

def GetPDFError(File,y):
    y -=1
    String = "gawk -F ',' '(NR==" + str(y) +")' " + File
    #print String
    PDFErrors=os.popen(String).readline().replace('\n','').split(',')
    #print PDFErrors
    for i in range(len(PDFErrors)):
        PDFErrors[i] = float(PDFErrors[i])
        PDFErrors[i] = math.fabs(PDFErrors[i])
    return  PDFErrors



a=sys.argv

for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input':
        InputRescales=a[n+1]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

os.system("cp LimitPlots/TEMPLATE_2012_ele.C LimitPlots/CurrentLimits2012_ele.C")
os.system("sed -i -e 's/CurrentLimits/CurrentLimits2012_ele/g' LimitPlots/CurrentLimits2012_ele.C")



List = [y+2 for y in range(113)] #To start with a value of 2, for gawk
x = 200
coupling = "0p2"
PreviousObsLim=0.6
for y in List:

    if (y-2) == 16:
        x = 200
        coupling = "0p4"
    if (y-2) == 32:
        x = 200
        coupling = "0p6"
    if (y-2) == 57:
        x = 200
        coupling = "0p8"
    if (y-2) == 82:
        x = 200
        coupling = "1p0"


    x += 100

    #if (not ((x==600) and (coupling=="1p0"))):
        #continue

    print "On step " + str(x)+","+coupling + "=========================================================="

    ConfigFile = str(x) +'_'+coupling+ "_2012temp.cfg"

    TempStore = os.popen("combine -M Asymptotic " + ConfigFile + " --rMax 5 | grep 97.5% | gawk '{print $NF}'").readline().replace('\n','')
    if is_number(TempStore):
        CheckValue = float(TempStore)
        if CheckValue == 0.0:
            CheckValue=1
            #if PreviousObsLim < 1:
            #    CheckValue = 1
            #else:
            #    CheckValue = 20

    else:
        CheckValue = CheckValue + 5

    Check = true

    while Check == true:
        String = "combine -M Asymptotic " + str(x)+'_'+coupling + "_2012temp.cfg --rMax " + str(CheckValue)
        print String
        TempFile = os.popen(String).readlines()
        print "==========Checking this value: " + str(CheckValue)
        Multiplied = false
        ExpLimitFound=false
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
               ExpLimitFound=true
            if "Expected 16.0%: r < " in line:
               MinusOne  =  float(line.split(" ")[4])
            
            if "Expected 50.0%: r < " in line:
               Center  =  float(line.split(" ")[4])
            
            if "Expected 84.0%: r < " in line:
               PlusOne  =  float(line.split(" ")[4])
            
            if "Expected 97.5%: r < " in line:
               PlusTwo  =  float(line.split(" ")[4])
           
        if not ExpLimitFound:
            if Multiplied == false:
                CheckValue = CheckValue *1.1
                Multiplied = true
        if ExpLimitFound:
            if Multiplied==true:
                Multiplied=false
                CheckValue = CheckValue /1.1
            

        if Multiplied == false:
            Check = false
                
    CS=float(os.popen("grep UE CrossSections\[pb].csv | grep 'M = " + str(x) + " GeV' | grep "+coupling+" | gawk -F ',' '{print $3}'").readline().replace('\n',''))/1000
    String = "gawk '(NR=="+str(y-1)+")' "+InputRescales
    CurrentRescaler=float(os.popen(String).readline().replace('\n',''))

    CS *= CurrentRescaler

    print "Rescaling by:" + str(CurrentRescaler)
    

    
    PreviousObsLim = ObsLim

    print "========================================"
    print ObsLim
    print "--------------"
    print MinusTwo
    print MinusOne
    print Center
    print PlusOne
    print PlusTwo

    os.system("sed -i -e 's/Obs" + str(x)+"_"+coupling + "/" + str(ObsLim*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/MinTwo" + str(x)+"_"+coupling + "/" + str(-MinusTwo*CS+Center*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/MinOne" + str(x)+"_"+coupling + "/" + str(-MinusOne*CS+Center*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/Center" + str(x)+"_"+coupling + "/" + str(Center*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/PlusOne" + str(x)+"_"+coupling + "/" + str(PlusOne*CS-Center*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/PlusTwo" + str(x)+"_"+coupling + "/" + str(PlusTwo*CS-Center*CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/ThCS" + str(x)+"_"+coupling + "/" + str(CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")

    Records.write(str(Center)+','+str(ObsLim)+','+str(CS)+'\n')

    sig_pdfs=GetPDFError('Ele_SignalNormalization_PDF.txt',y)

    sig_NNPDFdown = sig_pdfs[0]
    sig_NNPDFup = sig_pdfs[1]


    LowerTheoryBand = (1-sig_NNPDFdown)*CS
    UpperTheoryBand = (1+sig_NNPDFup)*CS

    os.system("sed -i -e 's/ThNormDown" + str(x)+"_"+coupling + "/" + str(CS-LowerTheoryBand) + "/g' LimitPlots/CurrentLimits2012_ele.C")
    os.system("sed -i -e 's/ThNormUp" + str(x)+"_"+coupling + "/" + str(UpperTheoryBand-CS) + "/g' LimitPlots/CurrentLimits2012_ele.C")

Records.close()
os.system("root -b LimitPlots/CurrentLimits2012_ele.C")

