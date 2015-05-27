from ROOT import *
import os
import sys
import math
import subprocess

#Limits.open('Limits.txt','w')

Records = open('FiducialLogMuon.txt','w')

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

os.system("cp LimitPlots/TEMPLATE_2012_mu.C LimitPlots/CurrentLimits2012_mu.C")
os.system("sed -i -e 's/CurrentLimits/CurrentLimits2012_mu/g' LimitPlots/CurrentLimits2012_mu.C")


Values = [(300+100*x) for x in range(16)]
#Values = [1700,1800]
for x in Values:
    print "On step " + str(x) + "=============================================================="
    y = (x-300)/100+2
    ConfigFile = str(x) + "_2012temp.cfg"
    
    TempStore = os.popen("combine -M Asymptotic " + ConfigFile + " --rMax 5 | grep 97.5% | gawk '{print $NF}'").readline().replace('\n','')
    print TempStore
    if is_number(TempStore):
        CheckValue = float(TempStore)
        if CheckValue == 0.0:
            CheckValue = 20
    else:
        CheckValue = CheckValue + 5
        
    Check = True

    while Check == True:
        String = "combine -M Asymptotic " + str(x) + "_2012temp.cfg --rMax " + str(CheckValue)
        print String
        TempFile = os.popen(String).readlines()
        print "==========Checking this value: " + str(CheckValue)
        Multiplied = False
        FoundBad=True
        for line in TempFile:
            #print "**"+line
            
            
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

            if ("At r =" in line) and not ("inf" in line or "nan" in line or "q_mu = 0.00000" in line):
                FoundBad=False
                #if (Multiplied == false):
                    #CheckValue = CheckValue * 1.1
                    #Multiplied = true
                    #print "=====BAD LINE FOUND++++++++++"

        if FoundBad:
            CheckValue = CheckValue * 1.1
            Multiplied = True
        if Multiplied == False:
            Check = False
                
    CS=float(os.popen("grep CMu CrossSections\[pb].csv | grep 'M = " + str(x) + " GeV' | gawk -F ',' '{print $3}'").readline().replace('\n',''))/1000
    String = "gawk '(NR=="+str(y-1)+")' "+InputRescales
    CurrentRescaler=float(os.popen(String).readline().replace('\n',''))

    CS *= CurrentRescaler

    print "Rescaling by:" + str(CurrentRescaler)

    print "========================================"
    print ObsLim
    print "--------------"
    print MinusTwo
    print MinusOne
    print Center
    print PlusOne
    print PlusTwo

    os.system("sed -i -e 's/Obs" + str(x) + "/" + str(ObsLim*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/MinTwo" + str(x) + "/" + str(-MinusTwo*CS+Center*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/MinOne" + str(x) + "/" + str(-MinusOne*CS+Center*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/Center" + str(x) + "/" + str(Center*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/PlusOne" + str(x) + "/" + str(PlusOne*CS-Center*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/PlusTwo" + str(x) + "/" + str(PlusTwo*CS-Center*CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/ThCS" + str(x) + "/" + str(CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")

    Records.write(str(Center)+','+str(ObsLim)+','+str(CS)+','+str(ObsLim*CS)+'\n')

    sig_pdfs=GetPDFError('Mu_SignalNormalization_PDF.txt',y)

    sig_NNPDFdown = sig_pdfs[0]
    sig_NNPDFup = sig_pdfs[1]


    LowerTheoryBand = (1-sig_NNPDFdown)*CS
    UpperTheoryBand = (1+sig_NNPDFup)*CS

    #Adding a +70% uncertainty to the theoretical CS uncertainty
    UpperTheoryBand = CS+sqrt((UpperTheoryBand-CS)**2 + (0.7 * CS)**2)

    os.system("sed -i -e 's/ThNormDown" + str(x)+ "/" + str(CS-LowerTheoryBand) + "/g' LimitPlots/CurrentLimits2012_mu.C")
    os.system("sed -i -e 's/ThNormUp" + str(x)+ "/" + str(UpperTheoryBand-CS) + "/g' LimitPlots/CurrentLimits2012_mu.C")

Records.close()
os.system("root -b LimitPlots/CurrentLimits2012_mu.C")
