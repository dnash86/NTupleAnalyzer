from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos import *

from CMSStyle import *
from HistoCreation import *
from WeightsAndFilters import *

#################################
#   Loading trees...


#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_TTBarReRun_2014_03_05_13_19_56/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMu_ReRun_2014_04_30_22_04_51/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_ForEMuFixedElectronEta_2014_07_01_16_02_33/SummaryFiles'
Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerSkim_2014_07_20_21_49_58/SummaryFiles'

#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRunOldNTuples_2014_02_25_21_20_15/SummaryFiles'
#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRun_OrderFixed_2014_05_06_15_52_31/SummaryFiles'

##  Less skimmed samples
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ElectronSmallerSkim_2014_06_10_01_46_29/SummaryFiles/'
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixElectronEta_2014_06_25_01_52_27/SummaryFiles'

Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ABCDStudy_ABCDStudy_2014_08_04_21_36_04/SummaryFiles'

#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixBEFilter_2014_06_24_00_50_34/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDReRunEdmundCS_NoPtJetElimination_2014_02_07_21_29_51/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDVeryStrict_2014_04_13_21_31_02/SummaryFiles'

#OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_ValuesSSB.txt'
OptimizationFile = '/afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Ele_SSB_log2.txt'

TreeName = 'PhysicalVariables'

Trigger = '*(CurrentDoubleElePass>0.5)'
Trigger_emu = '*(HLTMu40TriggerPass>0.5)'

#Replicating the HEEP isolation criterion as a cut...
HEEPIso = '*('
#The first electron must be isolated:
HEEPIso += '('
HEEPIso += '(fabs(Eta_HEEPele1)<1.442)*( (HcalIsoD1_HEEPele1+EcalIsoDR03_HEEPele1) >= ( 2.0 + 0.03* Pt_HEEPele1  +0.28*Rho) )  +'
HEEPIso += '(fabs(Eta_HEEPele1)>1.560)*( (HcalIsoD1_HEEPele1+EcalIsoDR03_HEEPele1) >= ( 2.5 + 0.03*(Pt_HEEPele1-50.0) +0.28*Rho) ) '
HEEPIso += ')'
#ALSO, the second electron must be isolated:
HEEPIso += '*('
HEEPIso += '(fabs(Eta_HEEPele2)<1.442)*( (HcalIsoD1_HEEPele2+EcalIsoDR03_HEEPele2) >= ( 2.0 + 0.03* Pt_HEEPele2  +0.28*Rho) )  +'
HEEPIso += '(fabs(Eta_HEEPele2)>1.560)*( (HcalIsoD1_HEEPele2+EcalIsoDR03_HEEPele2) >= ( 2.5 + 0.03*(Pt_HEEPele2-50.0) +0.28*Rho) ) '
HEEPIso += ')'
HEEPIso += ')'

#Now we do the same again, but inverted:
InvertedHEEPIso = '*('
#The first electron must NOT be isolated:
InvertedHEEPIso += '('
InvertedHEEPIso += '(fabs(Eta_HEEPele1)<1.442)*( (HcalIsoD1_HEEPele1+EcalIsoDR03_HEEPele1) < ( 2.0 + 0.03* Pt_HEEPele1  +0.28*Rho) )  +'
InvertedHEEPIso += '(fabs(Eta_HEEPele1)>1.560)*( (HcalIsoD1_HEEPele1+EcalIsoDR03_HEEPele1) < ( 2.5 + 0.03*(Pt_HEEPele1-50.0) +0.28*Rho) ) '
InvertedHEEPIso += ')'
#ALSO, the second electron must NOT be isolated:
InvertedHEEPIso += '*('
InvertedHEEPIso += '(fabs(Eta_HEEPele2)<1.442)*( (HcalIsoD1_HEEPele2+EcalIsoDR03_HEEPele2) < ( 2.0 + 0.03* Pt_HEEPele2  +0.28*Rho) )  +'
InvertedHEEPIso += '(fabs(Eta_HEEPele2)>1.560)*( (HcalIsoD1_HEEPele2+EcalIsoDR03_HEEPele2) < ( 2.5 + 0.03*(Pt_HEEPele2-50.0) +0.28*Rho) ) '
InvertedHEEPIso += ')'
InvertedHEEPIso += ')'



#Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'


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
WhichPU=0   #WhichPU = 0 means central values for pileup, -1 means varied down and 1 means varied up
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
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
    if a[n]=='-t' or a[n]=='--test':
        Test=True
    if a[n]=='-f' or a[n]=='--output_file':
        OutputIntegralsFile = a[n+1]
    if a[n]=='-e' or a[n]=='--errors':
        FileLocation = a[n+1]
    if a[n]=='-pd' or a[n]=='--pileup_down':
        WhichPU=-1
    if a[n]=='-pu' or a[n]=='--pileup_up':
        WhichPU=1
        #for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
            
        #exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"




print "Loading..."
print Files_ee
if FileLocation=='blank':
    for f in os.popen('cmsLs '+Files_ee+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        #print " = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        print f.replace('-','_').replace(".root\n","")
else:
    print "DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")"
    exec("DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")")   
    for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")       
    
for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    print 'emu_'+f.replace('-','_').replace(".root\n","")

for f in os.popen('cmsLs '+Files_qcd+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('qcd_'+f.replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_qcd+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'qcd_'+f.replace('-','_').replace(".root\n","")
print "...done loading"

###############################################


    
def DrawHisto(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):
    SetStyle()
    channel = "ee"
    Luminosity = "19600"

    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPU
    MaxRescaler=10.
    if "delta" in variable:
        MaxRescaler=10000.
    # Set canvases
   	

    c1 = TCanvas("c1","",800,480)
    pad1 = TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0)	
    pad1.Draw()
    pad1.cd()
    pad1.SetLogy()
    
    # Set gStyle
    gStyle.SetOptLogy()
    gStyle.SetOptStat(0)
    

    #Make the label
    Label=[xlabel,"Number of events"]
    
    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors
    Style_A=[0,2,0.0,2,1]
    Style_nonA=[0,5,0.0,2,2]
    #QCDStackStyle=[3006,21,.00001,2,3]


    ### Make the plots
    
    #Region A, should be OS, with the isolation applied
    h_QCD_A=MakeHisto('h_QCD_A','Data',DoublePhotonData,variable,binning,selection+HEEPIso+Filters+Trigger,Style_A,Label)

    h_qcd_A_WJets=MakeHisto('h_qcd_A_WJets','W+Jets',WJetsJBin,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_DiBoson=MakeHisto('h_qcd_A_DiBoson','DiBoson',DiBoson,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_ZJets=MakeHisto('h_qcd_A_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_SingleTop=MakeHisto('h_qcd_A_SingleTop','SingleTop',SingleTop,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_GJets=MakeHisto('h_qcd_A_Gjets','#gamma+Jets',Gjets,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_TTBar=MakeHisto('h_qcd_A_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_A,Label)
    

    print "Region _A:"
    print "Data = "+str(h_QCD_A.Integral())
    print "WJets = "+str(h_qcd_A_WJets.Integral())
    print "DiBoson = "+str(h_qcd_A_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_A_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_A_SingleTop.Integral())
    print "GJets = "+str(h_qcd_A_GJets.Integral())
    print "TTBar = "+str(h_qcd_A_TTBar.Integral())

    h_QCD_A.Add(h_qcd_A_WJets,-1)
    h_QCD_A.Add(h_qcd_A_DiBoson,-1)
    h_QCD_A.Add(h_qcd_A_ZJets,-1)
    h_QCD_A.Add(h_qcd_A_SingleTop,-1)
    h_QCD_A.Add(h_qcd_A_GJets,-1)
    h_QCD_A.Add(h_qcd_A_TTBar,-1)
    print "--->Contribution of A = "+str(h_QCD_A.Integral())
    
  
    #Region B, should be OS, with the isolation inverted
    h_QCD_B=MakeHisto('h_QCD_B','Data',DoublePhotonData,variable,binning,selection+InvertedHEEPIso+Filters+Trigger,Style_nonA,Label)

    h_qcd_B_WJets=MakeHisto('h_qcd_B_WJets','W+Jets',WJetsJBin,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_DiBoson=MakeHisto('h_qcd_B_DiBoson','DiBoson',DiBoson,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_ZJets=MakeHisto('h_qcd_B_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_SingleTop=MakeHisto('h_qcd_B_SingleTop','SingleTop',SingleTop,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_GJets=MakeHisto('h_qcd_B_Gjets','#gamma+Jets',Gjets,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_TTBar=MakeHisto('h_qcd_B_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    


    print "Region _B:"
    print "Data = "+str(h_QCD_B.Integral())
    print "WJets = "+str(h_qcd_B_WJets.Integral())
    print "DiBoson = "+str(h_qcd_B_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_B_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_B_SingleTop.Integral())
    print "GJets = "+str(h_qcd_B_GJets.Integral())
    print "TTBar = "+str(h_qcd_B_TTBar.Integral())

    h_QCD_B.Add(h_qcd_B_WJets,-1)
    h_QCD_B.Add(h_qcd_B_DiBoson,-1)
    h_QCD_B.Add(h_qcd_B_ZJets,-1)
    h_QCD_B.Add(h_qcd_B_SingleTop,-1)
    h_QCD_B.Add(h_qcd_B_GJets,-1)
    h_QCD_B.Add(h_qcd_B_TTBar,-1)
    print "--->Contribution of B = "+str(h_QCD_B.Integral())

    #Region C, should be SS, with the isolation applied
    h_QCD_C=MakeHisto('h_QCD_C','Data',DoublePhotonData,variable,binning,qcdselection+HEEPIso+Filters+Trigger,Style_nonA,Label)

    h_qcd_C_WJets=MakeHisto('h_qcd_C_WJets','W+Jets',WJetsJBin,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_DiBoson=MakeHisto('h_qcd_C_DiBoson','DiBoson',DiBoson,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_ZJets=MakeHisto('h_qcd_C_ZJets','Z+Jets',ZJetsJBin,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_SingleTop=MakeHisto('h_qcd_C_SingleTop','SingleTop',SingleTop,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_GJets=MakeHisto('h_qcd_C_Gjets','#gamma+Jets',Gjets,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_TTBar=MakeHisto('h_qcd_C_TTBar','t#bar{t}',TTBarDBin,variable,binning,qcdselection+HEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    
    print "Region _C:"
    print "Data = "+str(h_QCD_C.Integral())
    print "WJets = "+str(h_qcd_C_WJets.Integral())
    print "DiBoson = "+str(h_qcd_C_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_C_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_C_SingleTop.Integral())
    print "GJets = "+str(h_qcd_C_GJets.Integral())
    print "TTBar = "+str(h_qcd_C_TTBar.Integral())

    h_QCD_C.Add(h_qcd_C_WJets,-1)
    h_QCD_C.Add(h_qcd_C_DiBoson,-1)
    h_QCD_C.Add(h_qcd_C_ZJets,-1)
    h_QCD_C.Add(h_qcd_C_SingleTop,-1)
    h_QCD_C.Add(h_qcd_C_GJets,-1)
    h_QCD_C.Add(h_qcd_C_TTBar,-1)
    print "--->Contribution of C = "+str(h_QCD_C.Integral())
    


    #Region D, should be SS, with the isolation inverted
    h_QCD_D=MakeHisto('h_QCD_D','Data',DoublePhotonData,variable,binning,qcdselection+InvertedHEEPIso+Filters+Trigger,Style_nonA,Label)

    h_qcd_D_WJets=MakeHisto('h_qcd_D_WJets','W+Jets',WJetsJBin,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_DiBoson=MakeHisto('h_qcd_D_DiBoson','DiBoson',DiBoson,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_ZJets=MakeHisto('h_qcd_D_ZJets','Z+Jets',ZJetsJBin,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_SingleTop=MakeHisto('h_qcd_D_SingleTop','SingleTop',SingleTop,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_GJets=MakeHisto('h_qcd_D_Gjets','#gamma+Jets',Gjets,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_TTBar=MakeHisto('h_qcd_D_TTBar','t#bar{t}',TTBarDBin,variable,binning,qcdselection+InvertedHEEPIso+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,Style_nonA,Label)
    
    print "Region _D:"
    print "Data = "+str(h_QCD_D.Integral())
    print "WJets = "+str(h_qcd_D_WJets.Integral())
    print "DiBoson = "+str(h_qcd_D_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_D_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_D_SingleTop.Integral())
    print "GJets = "+str(h_qcd_D_GJets.Integral())
    print "TTBar = "+str(h_qcd_D_TTBar.Integral())

    h_QCD_D.Add(h_qcd_D_WJets,-1)
    h_QCD_D.Add(h_qcd_D_DiBoson,-1)
    h_QCD_D.Add(h_qcd_D_ZJets,-1)
    h_QCD_D.Add(h_qcd_D_SingleTop,-1)
    h_QCD_D.Add(h_qcd_D_GJets,-1)
    h_QCD_D.Add(h_qcd_D_TTBar,-1)
    print "--->Contribution of D = "+str(h_QCD_D.Integral())

    #Now the combined regions, will start with A 

    #Region A plus region B (should start with Data for region A, OS+iso)
    h_QCD_AplusB=MakeHisto('h_QCD_AplusB','Data',DoublePhotonData,variable,binning,selection+HEEPIso+Filters+Trigger,Style_A,Label)
    h_QCD_AplusB.Add(h_qcd_A_WJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_DiBoson,-1)
    h_QCD_AplusB.Add(h_qcd_A_ZJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_SingleTop,-1)
    h_QCD_AplusB.Add(h_qcd_A_GJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_TTBar,-1)
    h_QCD_AplusB.Add(h_QCD_B,1)

    #Region A plus region C (should start with Data for region A, OS+iso)
    h_QCD_AplusC=MakeHisto('h_QCD_AplusC','Data',DoublePhotonData,variable,binning,selection+HEEPIso+Filters+Trigger,Style_A,Label)
    h_QCD_AplusC.Add(h_qcd_A_WJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_DiBoson,-1)
    h_QCD_AplusC.Add(h_qcd_A_ZJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_SingleTop,-1)
    h_QCD_AplusC.Add(h_qcd_A_GJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_TTBar,-1)
    h_QCD_AplusC.Add(h_QCD_C,1)


    #Region C plus region D (should start with Data for region C, OS+noniso)
    h_QCD_CplusD=MakeHisto('h_QCD_CplusD','Data',DoublePhotonData,variable,binning,selection+InvertedHEEPIso+Filters+Trigger,Style_nonA,Label)
    h_QCD_CplusD.Add(h_qcd_C_WJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_DiBoson,-1)
    h_QCD_CplusD.Add(h_qcd_C_ZJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_SingleTop,-1)
    h_QCD_CplusD.Add(h_qcd_C_GJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_TTBar,-1)
    h_QCD_CplusD.Add(h_QCD_D,1)


    #Region B plus region D (should start with Data for region B, SS+iso)
    h_QCD_BplusD=MakeHisto('h_QCD_BplusD','Data',DoublePhotonData,variable,binning,qcdselection+HEEPIso+Filters+Trigger,Style_nonA,Label)
    h_QCD_BplusD.Add(h_qcd_B_WJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_DiBoson,-1)
    h_QCD_BplusD.Add(h_qcd_B_ZJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_SingleTop,-1)
    h_QCD_BplusD.Add(h_qcd_B_GJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_TTBar,-1)
    h_QCD_BplusD.Add(h_QCD_C,1)
  
    #Adding up backgrounds...
    
    #print "A = "+str(h_QCD_A.Integral())
    #print "B = "+str(h_QCD_B.Integral())
    #print "C = "+str(h_QCD_C.Integral())
    #print "D = "+str(h_QCD_D.Integral())

    print "A+B = "+str(h_QCD_AplusB.Integral())
    print "C+D = "+str(h_QCD_CplusD.Integral())

    print "A+C = "+str(h_QCD_AplusC.Integral())
    print "B+D = "+str(h_QCD_BplusD.Integral())

    print "B/D = "+str(h_QCD_B.Integral()/h_QCD_D.Integral())
    print "Total Background will be: "+str(h_QCD_C.Integral()*(h_QCD_B.Integral()/h_QCD_D.Integral()))
                                   
    #c1.cd(1).SetLogy()

    h_QCD_AplusB.Draw()
    h_QCD_CplusD.Draw("SAME")

    leg=TLegend(0.6,0.63,0.91,0.91,"","brNDC")
    leg.SetTextFont(132)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    leg.AddEntry(h_QCD_AplusB,"A+B")
    leg.AddEntry(h_QCD_CplusD,"C+D")
    leg.Draw("SAME")

    h_QCD_AplusB.SetMinimum(.1)
    h_QCD_AplusB.SetMaximum(MaxRescaler*(h_QCD_AplusB.GetMaximum()))


    
    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+"_SignComparison.png");
    else:
        c1.Print("PlotsSingleSub_ee2012/"+variable+"_"+tag+"_SignComparison.png");


    


    h_QCD_AplusC.Draw("HISTEP")
    h_QCD_BplusD.Draw("HISTEPSAME")

    leg1=TLegend(0.6,0.63,0.91,0.91,"","brNDC")
    leg1.SetTextFont(132)
    leg1.SetFillColor(0)
    leg1.SetBorderSize(0)
    leg1.AddEntry(h_QCD_AplusC,"A+C")
    leg1.AddEntry(h_QCD_BplusD,"B+D")
    leg1.Draw("SAME")

    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+"_IsoComparison.png");
    else:
        c1.Print("PlotsSingleSub_ee2012/"+variable+"_"+tag+"_IsoComparison.png");

    #txt = TLatex((binning[2]-binning[1])*.02+binning[1],.3*5.0*h_Data.GetMaximum(), "Work in Progress")
    #txt.SetTextFont(132)
    #txt.SetTextSize(0.06)
    #txt.Draw()

def GetSelections(ifile):
    import csv
    csvfile=open(ifile,'r')
    WriteToSelection=False
    WriteToSelection_emu=False
    WriteToSelection_qcd=False
    Selections=['','','']
    for row in csv.reader(csvfile):
        print row
        if row[0] == "#Selection":
            WriteToSelection=True
            WriteToSelection_emu=False
            WriteToSelection_qcd=False
        if row[0] == "#Selection_emu":
            WriteToSelection_emu=True
            WriteToSelection=False
            WriteToSelection_qcd=False
        if row[0] == "#Selection_qcd":
            WriteToSelection_qcd=True
            WriteToSelection_emu=False
            WriteToSelection=False
        if (row[0][0]!='#') and (len(row)==3):
            if WriteToSelection:
                if Selections[0]!='': Selections[0] += '*'
                Selections[0] += '('+row[0]+row[1]+row[2]+')'
            if WriteToSelection_emu:
                if Selections[1]!='': Selections[1] += '*'
                Selections[1] += '('+row[0]+row[1]+row[2]+')'
            if WriteToSelection_qcd:
                if Selections[2]!='': Selections[2] += '*'
                Selections[2] += '('+row[0]+row[1]+row[2]+')'
    print Selections
    return Selections




def plot():
    JustIntegrate=False
    drawSub = False
    use_emu = False
    #ttscaler = 0.489171949638 #0.479080479194  #0.488708924407 #0.490929901239
    ttscaler = 0.489186879557
    
    znorm = 0.981327517888
   
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        print "Please input cuts"
        return
    


    lq_choice = "*(LQmass==700)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"

    ptbinning = [50,0,1000]
    etabinning = [48,-2.4,2.4]
    mbinning = [50,0,2000]
    stbinning = [50,0,2000]
    vertexbinning = [45,-0.5,44.5]
    deltarbinning = [50,0,5]
    deltaphibinning = [80,-4,4]
    isobinning = [100,0,10]
    relisobinning=[100,0,0.5]
    hcalisobinning=[100,0,5]
    jetcountbinning=[9,0,8]

    chargebinning=[11,-5,5]

    filetag = "ABCDStudy"
    xtag = " ["+filetag+"]"

    print "About to start drawing the Histos..."
    print Selection


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, jetcountbinning, "PFJetCount", "PFJetCount", "PFJetCount", "PFJetCount" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

   
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_ee_single", "ST_pf_emu_single","(Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_HEEPele1", "max(Pt_HEEPele1,Pt_muon1)","Pt_QCDele1", "p_{T} (e_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd,use_emu , drawSub, ptbinning,  "Pt_HEEPele2", "min(Pt_HEEPele1,Pt_muon1)", "Pt_QCDele2","p_{T} (e_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)

    #return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele1", "Charge_HEEPele1","Charge_HEEPele1", "Ele 1 charge " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele2", "Charge_muon1","Charge_HEEPele2", "Ele 2 charge " +xtag, znorm, ttscaler,filetag)



def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        preselintegrate()

main()
