
from ROOT import *
import os
import sys
import math


#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_JustLQ_2013_02_05_11_54_12/SummaryFiles'
#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonStrictRun_2013_04_05_22_05_11/SummaryFiles'
NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ElectronStrictRun_2013_04_10_21_49_53/SummaryFiles/'
TreeName = "PhysicalVariables"

#TestSelection = 'weight_pileup_central'
TestSelection = '1.0'



def main():
    GetFinalIntegralsTest(NormalDirectory,TreeName,TestSelection)


def QuickIntegral(tree,selection):
	h = TH1D('h','h',1,-1,3)
	#h.Sumw2()
        #print selection
	tree.Project('h','1.0',selection)
        #print "done"
	#I = h.GetBinContent(1)
        I = h.GetEntries()
	#E = h.GetBinError(1)
        h.Delete()
	return I

def QuickError(tree,selection):
	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
        #print selection
	tree.Project('h','1.0',selection)
        #print "done"
	#I = h.GetBinContent(1)
	E = h.GetBinError(1)
        h.Delete()
	return E

def GetFinalIntegralsTest(FileDirectory,TreeName,Selection):

    CurrentSignalFile = 'LQToUE_Single_L-0p2.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(16)]:
        mass=str(x)
        if x != 300:
            continue
        coupling=str(0.2)
        isCMu=str(0)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genelectron1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'

        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
 
        print str(SIGNAL)

    CurrentSignalFile = 'LQToUE_Single_L-0p4.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(16)]:
        mass=str(x)
        if x != 300:
            continue
        coupling=str(0.4)
        isCMu=str(0)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genelectron1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'
        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
 
        print str(SIGNAL)

    CurrentSignalFile = 'LQToUE_Single_L-0p6.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(25)]:
        mass=str(x)
        if x != 300:
            continue
        coupling=str(0.6)
        isCMu=str(0)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genelectron1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'
        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
 
        print str(SIGNAL)

    CurrentSignalFile = 'LQToUE_Single_L-0p8.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(25)]:
        mass=str(x)
        if x != 300:
            continue
        coupling=str(0.8)
        isCMu=str(0)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genelectron1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'
        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
 
        print str(SIGNAL)


    CurrentSignalFile = 'LQToUE_Single_L-1p0.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(31)]:
        mass=str(x)
        if x != 300:
            continue
        coupling=str(1.0)
        isCMu=str(0)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genelectron1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'
        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
 
        print str(SIGNAL)


main()


