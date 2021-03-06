
from ROOT import *
import os
import sys
import math


#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_JustLQ_2013_02_05_11_54_12/SummaryFiles'
#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonStrictRun_2013_04_05_22_05_11/SummaryFiles'
#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_David_2012_ForLQCount_2013_05_28_17_57_00/SummaryFiles/'
#NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/BareBonesForCountingLQ_ForLQCount_2013_05_29_19_08_30/SummaryFiles/'
NormalDirectory = '/store/user/dnash/LQAnalyzerOutput/BareBonesForCountingLQ_ForLQCount_2013_05_29_19_08_30/SummaryFiles/'
TreeName = "PhysicalVariables"

TestSelection = '1.0'
#TestSelection = '(((N_TruePileUpInteractions > -0.5)*(N_TruePileUpInteractions < 0.5)*(0.244530459598))+((N_TruePileUpInteractions > 0.5)*(N_TruePileUpInteractions < 1.5)*(0.31499229816))+((N_TruePileUpInteractions > 1.5)*(N_TruePileUpInteractions < 2.5)*(0.322198325491))+((N_TruePileUpInteractions > 2.5)*(N_TruePileUpInteractions < 3.5)*(0.341581979178))+((N_TruePileUpInteractions > 3.5)*(N_TruePileUpInteractions < 4.5)*(0.314648206273))+((N_TruePileUpInteractions > 4.5)*(N_TruePileUpInteractions < 5.5)*(0.56538981455))+((N_TruePileUpInteractions > 5.5)*(N_TruePileUpInteractions < 6.5)*(0.441769254091))+((N_TruePileUpInteractions > 6.5)*(N_TruePileUpInteractions < 7.5)*(0.427953902511))+((N_TruePileUpInteractions > 7.5)*(N_TruePileUpInteractions < 8.5)*(0.589749988768))+((N_TruePileUpInteractions > 8.5)*(N_TruePileUpInteractions < 9.5)*(0.90410918038))+((N_TruePileUpInteractions > 9.5)*(N_TruePileUpInteractions < 10.5)*(1.30791473807))+((N_TruePileUpInteractions > 10.5)*(N_TruePileUpInteractions < 11.5)*(1.67352362673))+((N_TruePileUpInteractions > 11.5)*(N_TruePileUpInteractions < 12.5)*(1.73749668906))+((N_TruePileUpInteractions > 12.5)*(N_TruePileUpInteractions < 13.5)*(1.55901911286))+((N_TruePileUpInteractions > 13.5)*(N_TruePileUpInteractions < 14.5)*(1.33294641224))+((N_TruePileUpInteractions > 14.5)*(N_TruePileUpInteractions < 15.5)*(1.16443495129))+((N_TruePileUpInteractions > 15.5)*(N_TruePileUpInteractions < 16.5)*(1.0778945916))+((N_TruePileUpInteractions > 16.5)*(N_TruePileUpInteractions < 17.5)*(1.05186609916))+((N_TruePileUpInteractions > 17.5)*(N_TruePileUpInteractions < 18.5)*(1.06930192555))+((N_TruePileUpInteractions > 18.5)*(N_TruePileUpInteractions < 19.5)*(1.11290406686))+((N_TruePileUpInteractions > 19.5)*(N_TruePileUpInteractions < 20.5)*(1.15374740394))+((N_TruePileUpInteractions > 20.5)*(N_TruePileUpInteractions < 21.5)*(1.17732035702))+((N_TruePileUpInteractions > 21.5)*(N_TruePileUpInteractions < 22.5)*(1.18611191193))+((N_TruePileUpInteractions > 22.5)*(N_TruePileUpInteractions < 23.5)*(1.18131632992))+((N_TruePileUpInteractions > 23.5)*(N_TruePileUpInteractions < 24.5)*(1.15759938709))+((N_TruePileUpInteractions > 24.5)*(N_TruePileUpInteractions < 25.5)*(1.11059879824))+((N_TruePileUpInteractions > 25.5)*(N_TruePileUpInteractions < 26.5)*(1.04068494668))+((N_TruePileUpInteractions > 26.5)*(N_TruePileUpInteractions < 27.5)*(0.951171301491))+((N_TruePileUpInteractions > 27.5)*(N_TruePileUpInteractions < 28.5)*(0.845167369924))+((N_TruePileUpInteractions > 28.5)*(N_TruePileUpInteractions < 29.5)*(0.727643057296))+((N_TruePileUpInteractions > 29.5)*(N_TruePileUpInteractions < 30.5)*(0.606056240769))+((N_TruePileUpInteractions > 30.5)*(N_TruePileUpInteractions < 31.5)*(0.488283455463))+((N_TruePileUpInteractions > 31.5)*(N_TruePileUpInteractions < 32.5)*(0.380046057388))+((N_TruePileUpInteractions > 32.5)*(N_TruePileUpInteractions < 33.5)*(0.285250787571))+((N_TruePileUpInteractions > 33.5)*(N_TruePileUpInteractions < 34.5)*(0.205823501565))+((N_TruePileUpInteractions > 34.5)*(N_TruePileUpInteractions < 35.5)*(0.142231316023))+((N_TruePileUpInteractions > 35.5)*(N_TruePileUpInteractions < 36.5)*(0.0941677929934))+((N_TruePileUpInteractions > 36.5)*(N_TruePileUpInteractions < 37.5)*(0.0599116312817))+((N_TruePileUpInteractions > 37.5)*(N_TruePileUpInteractions < 38.5)*(0.0367993896252))+((N_TruePileUpInteractions > 38.5)*(N_TruePileUpInteractions < 39.5)*(0.0220068531564))+((N_TruePileUpInteractions > 39.5)*(N_TruePileUpInteractions < 40.5)*(0.0129486820498))+((N_TruePileUpInteractions > 40.5)*(N_TruePileUpInteractions < 41.5)*(0.00759458681023))+((N_TruePileUpInteractions > 41.5)*(N_TruePileUpInteractions < 42.5)*(0.00450930103869))+((N_TruePileUpInteractions > 42.5)*(N_TruePileUpInteractions < 43.5)*(0.00275675132524))+((N_TruePileUpInteractions > 43.5)*(N_TruePileUpInteractions < 44.5)*(0.0017663818592))+((N_TruePileUpInteractions > 44.5)*(N_TruePileUpInteractions < 45.5)*(0.00119894122355))+((N_TruePileUpInteractions > 45.5)*(N_TruePileUpInteractions < 46.5)*(0.000864708996439))+((N_TruePileUpInteractions > 46.5)*(N_TruePileUpInteractions < 47.5)*(0.000659651697587))+((N_TruePileUpInteractions > 47.5)*(N_TruePileUpInteractions < 48.5)*(0.000527010924453))+((N_TruePileUpInteractions > 48.5)*(N_TruePileUpInteractions < 49.5)*(0.000436191386691))+((N_TruePileUpInteractions > 49.5)*(N_TruePileUpInteractions < 50.5)*(0.000370765362639))+((N_TruePileUpInteractions > 50.5)*(N_TruePileUpInteractions < 51.5)*(0.000321223237915))+((N_TruePileUpInteractions > 51.5)*(N_TruePileUpInteractions < 52.5)*(0.000282300996348))+((N_TruePileUpInteractions > 52.5)*(N_TruePileUpInteractions < 53.5)*(0.000250586295532))+((N_TruePileUpInteractions > 53.5)*(N_TruePileUpInteractions < 54.5)*(0.000223641464536))+((N_TruePileUpInteractions > 54.5)*(N_TruePileUpInteractions < 55.5)*(0.000200125931199))+((N_TruePileUpInteractions > 55.5)*(N_TruePileUpInteractions < 56.5)*(0.000179054157397))+((N_TruePileUpInteractions > 56.5)*(N_TruePileUpInteractions < 57.5)*(0.000159835686271))+((N_TruePileUpInteractions > 57.5)*(N_TruePileUpInteractions < 58.5)*(0.000142026696041))+((N_TruePileUpInteractions > 58.5)*(N_TruePileUpInteractions < 59.5)*(0.000263820856266)))'



def main():
    GetFinalIntegralsTest(NormalDirectory,TreeName,TestSelection)


def QuickIntegral(tree,selection):
	h = TH1D('h','h',1,-1,3)
	#h.Sumw2()
        #print selection
	tree.Project('h','1.0',selection)
        #print "done"
	I = h.GetBinContent(1)
        #I = h.GetEntries()
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


    print "------------------------------"
    Total = 0
    CurrentSignalFile = 'LQToCMu_Single_L-1p0.root'
    exec('CurrentSignalTree'+" = TFile.Open(\"root://eoscms//eos/cms/"+FileDirectory+"/"+CurrentSignalFile.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    for x in [(300+100*y) for y in range(16)]:
        mass=str(x)
        coupling=str(1.0)
        isCMu=str(1)
        Cut = Selection+'*(LQmass=='+mass+')*(LQcoupling=='+coupling+')*(LQisCMu=='+isCMu+')'
        masscut = str(x - 100)
        #Cut = Cut + '*(  (WhichE==1)*(Mass_genelectron1genjet > '+masscut+') + (WhichE==2)*(Mass_genelectron2genjet > '+masscut+'))'
        #Cut = Cut + '*(Mass_Member_electron> '+masscut+')'
        #Cut = Cut + '*(Mass_genmuon1genjet > '+masscut+')'
        #Cut = Cut + '*(WhichE == 1)'
        SIGNAL = QuickIntegral(CurrentSignalTree,Cut)
        Total = Total + SIGNAL
        print str(SIGNAL)
    print Total

main()


