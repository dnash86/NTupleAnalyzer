from ROOT import *
import os
import sys
import math
from time import strftime


#################################
# Parsing arguments

a=sys.argv
InputCuts=False
UseOutputDir=False
PlotHistos=False
Test=False
IntegrateOnly=False
PreselIntegrateOnly=False
FileLocation='blank'
CollectOnly=False
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-p' or a[n]=='--plot':
        PlotHistos=True
    if a[n]=='-I' or a[n]=='--integrate':
        IntegrateOnly=True
    if a[n]=='-P' or a[n]=='--presel_integrate':
        PreselIntegrateOnly=True
    if a[n]=='-f' or a[n]=='--final_selection_cutcard':
        fselfile=a[n+1]
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
    if a[n]=='-t' or a[n]=='--test':
        Test=True
    if a[n]=='-e' or a[n]=='--errors':
        FileLocation = a[n+1]
    if a[n]=='-c' or a[n]=='--CollectOnly':
        CollectOnly=True
    
        #for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
            
        #exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"



def collectall():
    collect('NNPDF')
    collect('CTEQ')
    collect('MSTW')
            

def collect(PDFType):
    print "On this PDF Type: "+PDFType
    FileList = os.popen('ls ParallelFiles/*'+PDFType+'*.txt').readlines()
    SmallestBackgroundEventCount = [99999.]*113
    SmallestSignalEventCount = [99999.]*113
    LargestBackgroundEventCount = [0.]*113
    LargestSignalEventCount = [0.]*113

    ReferenceFile = os.popen('cat OutputIntegrals.txt').readlines()
    for line in ReferenceFile:
        Background = float(line.replace('\n','').split(',')[1])+float(line.replace('\n','').split(',')[2])+float(line.replace('\n','').split(',')[3])+float(line.replace('\n','').split(',')[4])+float(line.replace('\n','').split(',')[5])+float(line.replace('\n','').split(',')[6]) #Not including QCD for now
        print Background
        Signal = float(line.replace('\n','').split(',')[8])
    for line in FileList:
        CurrentFile = os.popen('cat '+line.replace('\n','')).readlines()
        for i in range(len(CurrentFile)):
            Background = CurrentFile[i].replace('\n','').split(',')[0]
            Signal = CurrentFile[i].replace('\n','').split(',')[1]
            
            if float(Background) < SmallestBackgroundEventCount[i]:
                SmallestBackgroundEventCount[i]=float(Background)
            if Signal < SmallestSignalEventCount[i]:
                SmallestSignalEventCount[i]=Signal

            if float(Background) > LargestBackgroundEventCount[i]:
                LargestBackgroundEventCount[i]=float(Background)
            if Signal > LargestSignalEventCount[i]:
                LargestSignalEventCount[i]=Signal

                
           
    for i in range(len(SmallestBackgroundEventCount)):
        print "Range = " +str(SmallestBackgroundEventCount[i])+" - " +str(LargestBackgroundEventCount[i])

        #if PDFType='CTEQ':
        #1.645

def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        preselintegrate()
    if CollectOnly:
        collectall()

main()
