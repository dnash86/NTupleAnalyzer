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


Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerSkim_2014_07_20_21_49_58/SummaryFiles'

##  Less skimmed samples
Files_mumu='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonFixID_2014_07_30_14_18_20/SummaryFiles'


#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonABCDStudy_MuonABCDStudy_2014_08_11_18_32_40/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonABCDStudy_QCDBtagStudy_2014_09_03_13_35_09/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonABCDStudy_QCDBtagStudy_2014_09_04_20_23_09/SummaryFiles'

OptimizationFile = '/afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Ele_SSB_log2.txt'

TreeName = 'PhysicalVariables'

Trigger = '*(HLTMu40TriggerPass>0.5)'
#Trigger = ''
Trigger_emu = '*(HLTMu40TriggerPass>0.5)'


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
print Files_mumu
if FileLocation=='blank':
    for f in os.popen('cmsLs '+Files_mumu+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
        #print " = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        print f.replace('-','_').replace(".root\n","")
else:
    print "SingleMuData= TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+"SingleMuData.root"+"\")"+".Get(\""+TreeName+"\")"
    exec("SingleMuData= TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+"SingleMuData.root"+"\")"+".Get(\""+TreeName+"\")")   
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
    channel = "mumu"
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
    gStyle.SetOptTitle(0)
    

    #Make the label
    Label=[xlabel,"Number of events"]
    
    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors
    Style_A=[0,2,0.0,2,1]
    Style_nonA=[0,5,0.0,2,2]
    #QCDStackStyle=[3006,21,.00001,2,3]


    ### Make the plots
    
    #Region A, should be OS, with the isolation applied
    h_QCD_A=MakeHisto('h_QCD_A','',SingleMuData,variable,binning,selection+Filters+Trigger,Style_A,Label)
    Data_A=h_QCD_A.Integral()
    h_qcd_A_WJets=MakeHisto('h_qcd_A_WJets','W+Jets',WJetsJBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_DiBoson=MakeHisto('h_qcd_A_DiBoson','DiBoson',DiBoson,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_ZJets=MakeHisto('h_qcd_A_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_SingleTop=MakeHisto('h_qcd_A_SingleTop','SingleTop',SingleTop,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    #h_qcd_A_GJets=MakeHisto('h_qcd_A_Gjets','#gamma+Jets',Gjets,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    h_qcd_A_TTBar=MakeHisto('h_qcd_A_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    

    print "Region _A:"
    print "Data = "+str(h_QCD_A.Integral())
    print "WJets = "+str(h_qcd_A_WJets.Integral())
    print "DiBoson = "+str(h_qcd_A_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_A_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_A_SingleTop.Integral())
    #print "GJets = "+str(h_qcd_A_GJets.Integral())
    print "TTBar = "+str(h_qcd_A_TTBar.Integral())

    h_QCDTestA=MakeHisto('h_QCDTestA','h_QCDTestA',QCDMu,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_A,Label)
    print "Test MC = "+str(h_QCDTestA.Integral())

    h_QCD_A.Add(h_qcd_A_WJets,-1)
    h_QCD_A.Add(h_qcd_A_DiBoson,-1)
    h_QCD_A.Add(h_qcd_A_ZJets,-1)
    h_QCD_A.Add(h_qcd_A_SingleTop,-1)
    #h_QCD_A.Add(h_qcd_A_GJets,-1)
    h_QCD_A.Add(h_qcd_A_TTBar,-1)
    print "--->Contribution of A = "+str(h_QCD_A.Integral())
    
  
    #Region B, should be OS, with the isolation inverted (so I need to use "qcd_..." samples)

    Test=MakeHisto('Test','Data',qcd_SingleMuData,variable,binning,"1.0"+Filters+Trigger,Style_nonA,Label)
    print "Testing, just trigger and filters: "+ str(Test.Integral())

    h_QCD_B=MakeHisto('h_QCD_B','Data',qcd_SingleMuData,variable,binning,selection+Filters+Trigger,Style_nonA,Label)
    Data_B=h_QCD_B.Integral()
    h_qcd_B_WJets=MakeHisto('h_qcd_B_WJets','W+Jets',qcd_WJetsJBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_DiBoson=MakeHisto('h_qcd_B_DiBoson','DiBoson',qcd_DiBoson,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_ZJets=MakeHisto('h_qcd_B_ZJets','Z+Jets',qcd_ZJetsJBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_SingleTop=MakeHisto('h_qcd_B_SingleTop','SingleTop',qcd_SingleTop,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    #h_qcd_B_GJets=MakeHisto('h_qcd_B_Gjets','#gamma+Jets',qcd_Gjets,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_B_TTBar=MakeHisto('h_qcd_B_TTBar','t#bar{t}',qcd_TTBarDBin,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    


    print "Region _B:"
    print "Data = "+str(h_QCD_B.Integral())
    print "WJets = "+str(h_qcd_B_WJets.Integral())
    print "DiBoson = "+str(h_qcd_B_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_B_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_B_SingleTop.Integral())
    #print "GJets = "+str(h_qcd_B_GJets.Integral())
    print "TTBar = "+str(h_qcd_B_TTBar.Integral())

    h_QCD_B.Add(h_qcd_B_WJets,-1)
    h_QCD_B.Add(h_qcd_B_DiBoson,-1)
    h_QCD_B.Add(h_qcd_B_ZJets,-1)
    h_QCD_B.Add(h_qcd_B_SingleTop,-1)
    #h_QCD_B.Add(h_qcd_B_GJets,-1)
    h_QCD_B.Add(h_qcd_B_TTBar,-1)
    print "--->Contribution of B = "+str(h_QCD_B.Integral())

    h_QCDTestB=MakeHisto('h_QCDTestB','h_QCDTestB',qcd_QCDMu,variable,binning,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    print "Test MC = "+str(h_QCDTestB.Integral())


    #Region C, should be SS, with the isolation applied
    h_QCD_C=MakeHisto('h_QCD_C','Data',SingleMuData,variable,binning,qcdselection+Filters+Trigger,Style_nonA,Label)
    Data_C=h_QCD_C.Integral()
    h_qcd_C_WJets=MakeHisto('h_qcd_C_WJets','W+Jets',WJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_DiBoson=MakeHisto('h_qcd_C_DiBoson','DiBoson',DiBoson,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_ZJets=MakeHisto('h_qcd_C_ZJets','Z+Jets',ZJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_SingleTop=MakeHisto('h_qcd_C_SingleTop','SingleTop',SingleTop,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    #h_qcd_C_GJets=MakeHisto('h_qcd_C_Gjets','#gamma+Jets',Gjets,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_C_TTBar=MakeHisto('h_qcd_C_TTBar','t#bar{t}',TTBarDBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    
    print "Region _C:"
    print "Data = "+str(h_QCD_C.Integral())
    print "WJets = "+str(h_qcd_C_WJets.Integral())
    print "DiBoson = "+str(h_qcd_C_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_C_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_C_SingleTop.Integral())
    #print "GJets = "+str(h_qcd_C_GJets.Integral())
    print "TTBar = "+str(h_qcd_C_TTBar.Integral())

    h_QCD_C.Add(h_qcd_C_WJets,-1)
    h_QCD_C.Add(h_qcd_C_DiBoson,-1)
    h_QCD_C.Add(h_qcd_C_ZJets,-1)
    h_QCD_C.Add(h_qcd_C_SingleTop,-1)
    #h_QCD_C.Add(h_qcd_C_GJets,-1)
    h_QCD_C.Add(h_qcd_C_TTBar,-1)
    print "--->Contribution of C = "+str(h_QCD_C.Integral())

    h_QCDTestC=MakeHisto('h_QCDTestC','h_QCDTestC',QCDMu,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    print "Test MC = "+str(h_QCDTestC.Integral())
    


    #Region D, should be SS, with the isolation inverted
    h_QCD_D=MakeHisto('h_QCD_D','Data',qcd_SingleMuData,variable,binning,qcdselection+Filters+Trigger,Style_nonA,Label)
    Data_D=h_QCD_D.Integral()
    h_qcd_D_WJets=MakeHisto('h_qcd_D_WJets','W+Jets',qcd_WJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_DiBoson=MakeHisto('h_qcd_D_DiBoson','DiBoson',qcd_DiBoson,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_ZJets=MakeHisto('h_qcd_D_ZJets','Z+Jets',qcd_ZJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_SingleTop=MakeHisto('h_qcd_D_SingleTop','SingleTop',qcd_SingleTop,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    #h_qcd_D_GJets=MakeHisto('h_qcd_D_Gjets','#gamma+Jets',qcd_Gjets,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    h_qcd_D_TTBar=MakeHisto('h_qcd_D_TTBar','t#bar{t}',qcd_TTBarDBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    
    print "Region _D:"
    print "Data = "+str(h_QCD_D.Integral())
    print "WJets = "+str(h_qcd_D_WJets.Integral())
    print "DiBoson = "+str(h_qcd_D_DiBoson.Integral())
    print "ZJets = "+str(h_qcd_D_ZJets.Integral())
    print "SingleTop = "+str(h_qcd_D_SingleTop.Integral())
    #print "GJets = "+str(h_qcd_D_GJets.Integral())
    print "TTBar = "+str(h_qcd_D_TTBar.Integral())

    h_QCD_D.Add(h_qcd_D_WJets,-1)
    h_QCD_D.Add(h_qcd_D_DiBoson,-1)
    h_QCD_D.Add(h_qcd_D_ZJets,-1)
    h_QCD_D.Add(h_qcd_D_SingleTop,-1)
    #h_QCD_D.Add(h_qcd_D_GJets,-1)
    h_QCD_D.Add(h_qcd_D_TTBar,-1)
    print "--->Contribution of D = "+str(h_QCD_D.Integral())

    h_QCDTestD=MakeHisto('h_QCDTestD','h_QCDTestD',qcd_QCDMu,variable,binning,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,Style_nonA,Label)
    print "Test MC = "+str(h_QCDTestD.Integral())

    #Getting the total ratio and error:

    
    h=TH1D('h','h',1,-1,3)
    hdenom=TH1D('htotal','htotal',1,-1,3)

    hnum=TH1D('htotal','htotal',1,-1,3)


    h.Sumw2()
    hnum.Sumw2()
    hdenom.Sumw2()

    trees=[qcd_SingleMuData,qcd_WJetsJBin,qcd_DiBoson,qcd_ZJetsJBin,qcd_SingleTop,qcd_TTBarDBin]
    weights=[1,-1,-1,-1,-1,-1]
    selections=[selection+Filters+Trigger,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters]

    for i in range(len(trees)):
        trees[i].Project('h','1.0',selections[i])
        hnum.Add(h,weights[i])

    trees=[qcd_SingleMuData,qcd_WJetsJBin,qcd_DiBoson,qcd_ZJetsJBin,qcd_SingleTop,qcd_TTBarDBin]
    weights=[1,-1,-1,-1,-1,-1]
    qcdselections=[qcdselection+Filters+Trigger,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters]

    for i in range(len(trees)):
        trees[i].Project('h','1.0',qcdselections[i])
        hdenom.Add(h,weights[i])

    hnum.Divide(hdenom)

    I = hnum.GetBinContent(1)
    E = hnum.GetBinError(1)

    print str(I) +"+/-"+str(E)
    #Now the combined regions, will start with A 

    #Region A plus region B (should start with Data for region A, OS+iso)
    h_QCD_AplusB=MakeHisto('h_QCD_AplusB','Data',SingleMuData,variable,binning,selection+Filters+Trigger,Style_A,Label)
    h_QCD_AplusB.Add(h_qcd_A_WJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_DiBoson,-1)
    h_QCD_AplusB.Add(h_qcd_A_ZJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_SingleTop,-1)
    #h_QCD_AplusB.Add(h_qcd_A_GJets,-1)
    h_QCD_AplusB.Add(h_qcd_A_TTBar,-1)
    h_QCD_AplusB.Add(h_QCD_B,1)

    #Region A plus region C (should start with Data for region A, OS+iso)
    h_QCD_AplusC=MakeHisto('h_QCD_AplusC','Data',SingleMuData,variable,binning,selection+Filters+Trigger,Style_A,Label)
    h_QCD_AplusC.Add(h_qcd_A_WJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_DiBoson,-1)
    h_QCD_AplusC.Add(h_qcd_A_ZJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_SingleTop,-1)
    #h_QCD_AplusC.Add(h_qcd_A_GJets,-1)
    h_QCD_AplusC.Add(h_qcd_A_TTBar,-1)
    h_QCD_AplusC.Add(h_QCD_C,1)


    #Region C plus region D (should start with Data for region C, OS+noniso)
    h_QCD_CplusD=MakeHisto('h_QCD_CplusD','Data',SingleMuData,variable,binning,qcdselection+Filters+Trigger,Style_nonA,Label)
    h_QCD_CplusD.Add(h_qcd_C_WJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_DiBoson,-1)
    h_QCD_CplusD.Add(h_qcd_C_ZJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_SingleTop,-1)
    #h_QCD_CplusD.Add(h_qcd_C_GJets,-1)
    h_QCD_CplusD.Add(h_qcd_C_TTBar,-1)
    h_QCD_CplusD.Add(h_QCD_D,1)


    #Region B plus region D (should start with Data for region B, SS+iso)
    h_QCD_BplusD=MakeHisto('h_QCD_BplusD','Data',qcd_SingleMuData,variable,binning,selection+Filters+Trigger,Style_nonA,Label)
    h_QCD_BplusD.Add(h_qcd_B_WJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_DiBoson,-1)
    h_QCD_BplusD.Add(h_qcd_B_ZJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_SingleTop,-1)
    #h_QCD_BplusD.Add(h_qcd_B_GJets,-1)
    h_QCD_BplusD.Add(h_qcd_B_TTBar,-1)
    h_QCD_BplusD.Add(h_QCD_D,1)
  
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

    h_QCD_CplusD.Scale(h_QCD_AplusB.Integral()/h_QCD_CplusD.Integral())

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
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+"_SignComparison.png");


    


    h_QCD_AplusC.Draw()
    h_QCD_BplusD.Scale(h_QCD_AplusC.Integral()/h_QCD_BplusD.Integral())
    h_QCD_BplusD.Draw("SAME")

    leg1=TLegend(0.6,0.63,0.91,0.91,"","brNDC")
    leg1.SetTextFont(132)
    leg1.SetFillColor(0)
    leg1.SetBorderSize(0)
    leg1.AddEntry(h_QCD_AplusC,"A+C")
    leg1.AddEntry(h_QCD_BplusD,"B+D")
    leg1.Draw("SAME")

    File = open('QCD_mumu.tex','w')
    File.write('\\begin{tabular}{|c|c|c|c|c|}\n')
    File.write('\\hline\n')
    File.write('  & {A} & {B} & {C} & {D} \\\\\n')    
    File.write('\\hline\n')
    File.write('{Data}  & {'+str(round(Data_A,2))+'} & {'+str(round(Data_B,2))+'} & {'+str(round(Data_C,2))+'} & {'+str(round(Data_D,2))+'} \\\\\n')    
    File.write('\\hline\n')
    File.write('{W}  & {'+str(round(h_qcd_A_WJets.Integral(),2))+'} & {'+str(round(h_qcd_B_WJets.Integral(),2))+'} & {'+str(round(h_qcd_C_WJets.Integral(),2))+'} & {'+str(round(h_qcd_D_WJets.Integral(),2))+'} \\\\\n')    
    File.write('\\hline\n')
    File.write('{Diboson}  & {'+str(round(h_qcd_A_DiBoson.Integral(),2))+'} & {'+str(round(h_qcd_B_DiBoson.Integral(),2))+'} & {'+str(round(h_qcd_C_DiBoson.Integral(),2))+'} & {'+str(round(h_qcd_D_DiBoson.Integral(),2))+'} \\\\\n')    
    File.write('\\hline\n')
    File.write('{Z}  & {'+str(round(h_qcd_A_ZJets.Integral(),2))+'} & {'+str(round(h_qcd_B_ZJets.Integral(),2))+'} & {'+str(round(h_qcd_C_ZJets.Integral(),2))+'} & {'+str(round(h_qcd_D_ZJets.Integral(),2))+'} \\\\\n')    
    File.write('\\hline\n')
    File.write('{Single Top}  & {'+str(round(h_qcd_A_SingleTop.Integral(),2))+'} & {'+str(round(h_qcd_B_SingleTop.Integral(),2))+'} & {'+str(round(h_qcd_C_SingleTop.Integral(),2))+'} & {'+str(round(h_qcd_D_SingleTop.Integral(),2))+'} \\\\\n')    
    File.write('\\hline\n')
    File.write('{t\\bar{t}}  & {'+str(round(h_qcd_A_TTBar.Integral(),2))+'} & {'+str(round(h_qcd_B_TTBar.Integral(),2))+'} & {'+str(round(h_qcd_C_TTBar.Integral(),2))+'} & {'+str(round(h_qcd_D_TTBar.Integral(),2))+'} \\\\\n')    
    
    File.write('\\hline\n')
    File.write('\\hline\n')
    File.write('{Data \\minus MC}  & {'+str(round(h_QCD_A.Integral(),2))+'} & {'+str(round(h_QCD_B.Integral(),2))+'} & {'+str(round(h_QCD_C.Integral(),2))+'} & {'+str(round(h_QCD_D.Integral(),2))+'} \\\\\n')    
    File.write('\\end{tabular}\n')
    File.close()
    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+"_IsoComparison.png");
    else:
        c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+"_IsoComparison.png");

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

    return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

   
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single","(Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_muon1muon2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_muon1", "max(Pt_HEEPele1,Pt_muon1)","Pt_QCDele1", "p_{T} (e_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd,use_emu , drawSub, ptbinning,  "Pt_muon2", "min(Pt_HEEPele1,Pt_muon1)", "Pt_QCDele2","p_{T} (e_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "M_{e jet} " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_muon1*Charge_muon2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)

    #return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_muon1", "Charge_HEEPele1","Charge_HEEPele1", "Ele 1 charge " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_muon2", "Charge_muon1","Charge_HEEPele2", "Ele 2 charge " +xtag, znorm, ttscaler,filetag)



def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        preselintegrate()

main()
