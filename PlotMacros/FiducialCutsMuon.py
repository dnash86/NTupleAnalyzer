from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos_mumu import *

from CMSStyle import *
from HistoCreation import *
from WeightsAndFilters import *

#################################
#   Loading trees...

#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EmuReRunNewStoreFile_2013_10_29_18_45_49/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_ForEMuFixedElectronEta_2014_07_01_16_02_33/SummaryFiles'
Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerFixMuonKinematics_2014_07_30_14_17_53/SummaryFiles'
#Files_mumu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonsReRunNewStoreFile_2013_10_29_18_44_01/SummaryFiles'
Files_mumu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonFixID_2014_07_30_14_18_20/SummaryFiles'
#Files_mumu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_CheckMuonID_CheckingOtherMuonID_2014_08_17_04_07_01/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonABCDStudy_MuonABCDStudy_2014_08_11_18_32_40/SummaryFiles'
#OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_ValuesSSB.txt'






#Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_MuonsFixedLQMass_2014_09_27_15_32_17/SummaryFiles'

Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_MuonStrict_FixedGenMassesStatusOne_2014_10_30_13_44_17/SummaryFiles'

#OptimizationFile = '/afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Mu_SSB_log2.txt'
OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/MuonModifiedValues.txt'

TreeName = 'PhysicalVariables'


Trigger = '*(HLTMu40TriggerPass>0.5)'
Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
qcdscaler = 1.95

#################################
# Parsing arguments

a=sys.argv
InputCuts=False
UseOutputDir=False
PlotHistos=False
Test=False
IntegrateOnly=False
PreselIntegrateOnly=False
FiducialCuts = False
FileLocation='blank'
ExtraCutsBool=False
ZShapeFile='blank'
tdrstyle=False
WhichPU=0   #WhichPU = 0 means central values for pileup, -1 means varied down and 1 means varied up
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-p' or a[n]=='--plot':
        PlotHistos=True
    if a[n]=='-A' or a[n]=='--additional_cuts':
        ExtraCutsBool=True
        ExtraCuts=a[n+1]
        ExtraCutsValue = a[n+2]
    if a[n]=='-I' or a[n]=='--integrate':
        IntegrateOnly=True
    if a[n]=='-F' or a[n]=='--fiducial_cuts':
        FiducialCuts=True
        cutvalue = a[n+1]
    if a[n]=='-P' or a[n]=='--presel_integrate':
        PreselIntegrateOnly=True
    if a[n]=='-o' or a[n]=='--output_dir':
        OutputDir=a[n+1]
        UseOutputDir=True
    if a[n]=='-f' or a[n]=='--output_file':
        OutputIntegralsFile = a[n+1]
    if a[n]=='-e' or a[n]=='--errors':
        FileLocation = a[n+1]
        Files_CorrectedSignal=a[n+2]
    if a[n]=='-s' or a[n]=='--shape_errors':
        ZShapeFile = a[n+1]  
    if a[n]=='-pd' or a[n]=='--pileup_down':
        WhichPU=-1
    if a[n]=='-pu' or a[n]=='--pileup_up':
        WhichPU=1
        #for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    if a[n]=='-tdr' or a[n]=='--use_tdr_style':
        tdrstyle=True
        from tdrstyle import *
        
            
        #exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"

print "Loading..."
print Files_mumu
if FileLocation=='blank':
    #------Hacked for new signal files use with a ''
    for f in os.popen('cmsLs '+Files_mumu+'| grep ".root" | gawk \'{print $NF}\' | grep -v LQTo| gawk -F "/" \'{print $NF}\'').readlines():
        #print " = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        print f.replace('-','_').replace(".root\n","")
    for f in os.popen('cmsLs '+Files_CorrectedSignal+'| grep ".root" | gawk \'{print $NF}\'  | gawk -F "/" \'{print $NF}\'').readlines():
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

else:
    print "SingleMuData= TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+"SingleMuData.root"+"\")"+".Get(\""+TreeName+"\")"
    exec("SingleMuData= TFile.Open(\"root://eoscms//eos/cms/"+Files_mumu+"/"+"SingleMuData.root"+"\")"+".Get(\""+TreeName+"\")")   
    for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | grep -v LQTo| gawk -F "/" \'{print $NF}\'').readlines():
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")       
    for f in os.popen('cmsLs '+Files_CorrectedSignal+'| grep ".root" | gawk \'{print $NF}\'  | gawk -F "/" \'{print $NF}\'').readlines():
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    print 'emu_'+f.replace('-','_').replace(".root\n","")
\

for f in os.popen('cmsLs '+Files_qcd+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('qcd_'+f.replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_qcd+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'qcd_'+f.replace('-','_').replace(".root\n","")
print "...done loading"


if ZShapeFile != 'blank':
    del ZJetsJBin
    ZJetsJBin = TFile.Open("root://eoscms//eos/cms/"+ZShapeFile).Get(TreeName)

###############################################


def integrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>110))*(ST_pf_mumu_single> 250)'
        
        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = ''  # Just for compatibility with the electron side

    

    #Trigger = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu

    
    JustIntegrate=True
    drawSub = False
    use_emu = True
    #ttscaler = 0.5942599
    #znorm = 0.98580048415651985403

    ttscaler = 0.566
    znorm =  0.97647964662  #0.
        
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    for i in range(1):
        MassRangeLength = 16
        Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==1)*(LQcoupling==1)*(1/1000)"
            
            AdditionalCut="*(  (Pt_genmuon1 > Pt_genmuon2) *(Mass_genmuon1genjet > "+str(float(x)*0.75)+") +(Pt_genmuon1 < Pt_genmuon2) *(Mass_genmuon2genjet > "+str(float(x)*0.75)+")  )*(Mass_genmuon1muon2 > 110.)"
            #AdditionalCut="*(  (Pt_genmuon1 > Pt_genmuon2) *(Mass_genmuon1genjet > 200.) +(Pt_genmuon1 < Pt_genmuon2) *(Mass_genmuon2genjet > 200.)  )*(Mass_genmuon1muon2 > 110.)"
            if x > 300:
                continue
            #print lq_choice
            #Cuts=os.popen("grep -A 1 "+Coupling+ " /afs/cern.ch/work/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_SSB_log2.txt  | grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')


            if IntegrateOnly:
                Cuts=os.popen("grep -A 1 "+Coupling+" " + OptimizationFile + "| grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')
                Cuts_emu=Cuts.replace('M_muon2pfjet1','M_HEEPele1pfjet1').replace('mumu','emu')
            if PreselIntegrateOnly:
                Cuts="1.0"
                Cuts_emu='1.0'
            #print "gonna integrate"
            IntsAndErrs =  GetIntegralsAndErrors(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Cuts_emu+"*"+Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut, use_emu, drawSub, chargebinning, "Charge_muon1*Charge_muon2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)
            #print IntsAndErrs[0]
            File = open(OutputIntegralsFile+".txt",'a') 
            File.write(IntsAndErrs[0]+'\n')
            File.close()

            File = open(OutputIntegralsFile+"_Errors.txt",'a') 
            File.write(IntsAndErrs[1]+'\n')
            File.close()

            File = open(OutputIntegralsFile+"_Entries.txt",'a') 
            File.write(IntsAndErrs[2]+'\n')
            File.close()
            
            

                   
def preselintegrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>110))*(ST_pf_mumu_single> 250)'
        
        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = ''  # Just for compatibility with the electron side

    

    #Trigger = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger     
    
    JustIntegrate=True
    drawSub = False
    use_emu = False
    ttscaler = 0.5942599
    znorm = 0.98580048415651985403
        
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    for i in range(1):
        MassRangeLength = 16
        Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==1)*(LQcoupling==1)*(1/1000)"
            AdditionalCut = ""
            Cuts="1.0"
            String = DrawHisto(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)
            print String
            File = open('IntegralOutput.txt','a') 
            File.write(String+'\n')
            File.close()
            
            

    
def GetIntegralsAndErrors(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):

    channel = "ee"
    Luminosity = "19.6"

    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPUUp
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPUDown

    ### Make the plots
    
    #print selection

    signaltrees=[LQToCMu_Single_L_1p0]
    signalweights = [1]
    signalselections = [selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters+lq_choice]

    print signalselections

    SignalValues=IntegralAndError(signaltrees,signalweights,signalselections)

    DataValues=IntegralAndError([SingleMuData],[1],[selection+Trigger+Filters])

    WJetsValues=IntegralAndError([WJetsJBin],[1],[selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    DiBosonValues=IntegralAndError([DiBoson],[1],[selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    SingleTopValues=IntegralAndError([SingleTop],[1],[selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    ZJetsValues=IntegralAndError([ZJetsJBin],[1],[selection+'*('+str(zscale)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    h=TH1D('h','h',1,-1,3)
    h.Sumw2()
    ZJetsJBin.Project('h','1.0',selection+'*('+str(zscale)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters)
        
    print "------------------------>Entries = " +str(h.GetEntries())

    #QCDValues=IntegralAndError([QCDMu],[1],[selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    if use_emu:
        ttbartrees=[emu_SingleMuData,emu_WJetsJBin,emu_DiBoson,emu_ZJetsJBin,emu_SingleTop]
        ttbarweights=[1,-1,-1,-1,-1]
        ttbarselections=[emuselection+Trigger_emu+R_mumu_over_mu+'*('+str(ttscaler)+')'+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_mumu_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_mumu_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_mumu_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_mumu_over_mu+Filters]

        TTBarValues=IntegralAndError(ttbartrees,ttbarweights,ttbarselections)

    else:
        TTBarValues=IntegralAndError([TTBarDBin],[1],[selection+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters])
    if (zscale!=1.00):
        qcdtrees=[SingleMuData,WJetsJBin,DiBoson,ZJetsJBin,SingleTop,TTBarDBin]
        qcdweights=[1,-1,-1,-1,-1,-1]
        qcdselections=[qcdselection+'*('+str(qcdscaler)+')'+Filters+Trigger,qcdselection+'*('+str(qcdscaler)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+'*('+str(qcdscaler)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+'*('+str(qcdscaler)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+'*('+str(qcdscaler)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters,qcdselection+'*('+str(qcdscaler)+')'+CorrectLumiAndPU+DoubleMuNonEmulatedTrigger+Filters]

        QCDValues=IntegralAndError(qcdtrees,qcdweights,qcdselections)
   

    if JustIntegrate:
        ValuesString= str(DataValues[0])+","+str(TTBarValues[0]) + "," + str(ZJetsValues[0]) + "," + str(DiBosonValues[0]) + "," + str(SingleTopValues[0]) + "," + str(WJetsValues[0]) + "," + str(QCDValues[0]) + "," + str(SignalValues[0])
        ErrorsString= str(DataValues[1])+","+str(TTBarValues[1]) + "," + str(ZJetsValues[1]) + "," + str(DiBosonValues[1]) + "," + str(SingleTopValues[1]) + "," + str(WJetsValues[1]) + "," + str(QCDValues[1]) + "," + str(SignalValues[1])
        EntriesString= str(DataValues[2])+","+str(TTBarValues[2]) + "," + str(ZJetsValues[2]) + "," + str(DiBosonValues[2]) + "," + str(SingleTopValues[2]) + "," + str(WJetsValues[2]) + "," + str(QCDValues[2]) + "," + str(SignalValues[2])

        return [ValuesString,ErrorsString,EntriesString]
                   
    
    
def DrawHisto(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):
    if tdrstyle:
        setTDRStyle()
    else:
        SetStyle()
    Luminosity = "19.6"


    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPUUp
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPUDown


    MaxRescaler=10.
    if zscale==1.0:
        MaxRescaler = 10000
    if "N_Vertices" in variable:
        MaxRescaler = 1000.
    if "delta" in variable:
        MaxRescaler=10000.
    if "Eta" in variable:
        MaxRescaler = 1000000
    # Set canvases
    if drawSub:
        c1 = TCanvas("c1","",800,800)
        pad1 = TPad("pad1","The pad 60% of the height",0.0,0.4,1.0,1.0,0)
        pad2 = TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0)
        pad2r = TPad("pad2r","The ptad 20% of the height",0.0,0.0,1.0,0.2,0)
        pad1.Draw()
        pad2.Draw()
        pad2r.Draw()
    else:
        c1 = TCanvas("c1","",800,480)
        pad1 = TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0)	
        pad1.Draw()
        
    pad1.cd()
    pad1.SetLogy()
    
    # Set gStyle
    gStyle.SetOptLogy()
    gStyle.SetOptStat(0)
    

    #Make the label
    Label=[xlabel,"Events / "+str((binning[2]-binning[1])/binning[0])+" GeV"]
    
    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors
    DataRecoStyle=[0,21,0.0,2,1]
    WStackStyle=[3007,21,.00001,2,9]
    TTStackStyle=[3005,21,.00001,2,4]
    ZStackStyle=[3004,21,.00001,2,2]
    DiBosonStackStyle=[3006,21,.00001,2,9]
    StopStackStyle=[3006,21,.00001,2,3]
    QCDStackStyle=[3006,21,.00001,2,3]
    #GJetsStackStyle=[3009,21,.00001,2,5]

    SignalStyle=[0,22,0.7,3,1]

    ### Make the plots
    h_Signal=MakeHisto('h_Signal','LQToCMu_Single_L_1p0',LQToCMu_Single_L_1p0,variable,binning,selection+Filters+LumiAndPU+DoubleMuNonEmulatedTrigger+lq_choice,SignalStyle,Label)
    

    h_Data=MakeHisto('h_Data','Data',SingleMuData,variable,binning,selection+Trigger+Filters,DataRecoStyle,Label)

    h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,WStackStyle,Label)
    h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,DiBosonStackStyle,Label)
    h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,StopStackStyle,Label)    
    #h_QCD=MakeHisto('h_QCD','h_QCD',QCDMu,variable,binning,selection+LumiAndPU+DoubleMuNonEmulatedTrigger+Filters,QCDStackStyle,Label)

    
    c1.cd(1).SetLogy()

    #MCStack.SetMinimum(.1)
    #MCStack.SetMaximum(MaxRescaler*h_Data.GetMaximum())                              
    #MCStack=BeautifyStack(MCStack,Label)
    h_Signal.SetMaximum(10)
    h_Signal.SetMinimum(.0001)
    h_Signal.SetLineStyle(3)
    h_Signal.Draw("HIST")
    #h_Signal.Draw("HISTSAME")
    #h_Data.Draw("HISTEPSAME")

    


    txt = TLatex((binning[2]-binning[1])*.02+binning[1],.15*5.0*h_Data.GetMaximum(), "CMS Preliminary")
    txt.SetTextFont(132)
    txt.SetTextSize(0.06)
    txt.Draw()

    drawSub=False
    if drawSub:
        pad2.cd()
	
        h_comp = TH1F("h_comp","",binning[0],binning[1],binning[2])
        h_compr = TH1F("h_compr","",binning[0],binning[1],binning[2])	
	
        h_bg = TH1F("h_bg","",binning[0],binning[1],binning[2])

        h_bg.Sumw2()
        for histo in Backgrounds:
            h_bg.Add(histo)
	
        nbinsx = binning[0]	
        ibin = 0
	
        chi2 = 0.0
	
        ndat = 0.0
        nbg = 0.0
        err_nbg = 0.0
        err_total = 0.0
	
        datmean = 0.0
        mcmean = 0.0
	
        xminl = 0
        xmaxl = 0
	
        for ibin in range(nbinsx):
            
            ndat = 1.0*(h_Data.GetBinContent(ibin))
            nbg = 1.0*(h_bg.GetBinContent(ibin))
            datmean += 1.0*(h_Data.GetBinContent(ibin))*h_Data.GetBinCenter(ibin)
            err_nbg = 1.0*(h_bg.GetBinError(ibin))
            err_total = sqrt(  pow(err_nbg,2.0) + ndat )
            
            mcmean += 1.0*(h_bg.GetBinContent(ibin))*h_bg.GetBinCenter(ibin)
            if (ndat!=0):
                chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5)
            
            h_comp.SetBinContent(ibin,0.0 )
            h_compr.SetBinContent(ibin,0.0 )
            if (ndat!=0 and nbg != 0):
                h_comp.SetBinContent(ibin, (ndat - nbg)/err_total )
            if (ndat!=0 and nbg != 0):
                h_compr.SetBinContent(ibin, (ndat - nbg)/nbg )
            if (ndat!=0 and nbg != 0):
                h_compr.SetBinError(ibin, (err_total)/nbg )

        h_comp.GetYaxis().SetTitle("N(#sigma) Diff.")
        h_comp.GetYaxis().SetTitleFont(132)
        h_comp.GetYaxis().SetTitleSize(.17)
        h_comp.GetYaxis().SetLabelSize(.11)
        h_comp.GetXaxis().SetLabelSize(.11)	
        h_comp.GetYaxis().SetTitleOffset(.25)
	
        line0 = TLine(binning[1],0,binning[2],0)
        line2u = TLine(binning[1],2,binning[2],2)
        line2d = TLine(binning[1],-2,binning[2],-2)
	
        h_comp.SetMinimum(-8)
        h_comp.SetMaximum(8)
        h_comp.SetMarkerStyle(21)
        h_comp.SetMarkerSize(0.5)
	
	
        h_comp.Draw("p")
        line0.Draw("SAME")
        line2u.Draw("SAME")
        line2d.Draw("SAME")
		
		
        pad2r.cd()
	
        h_compr.GetYaxis().SetTitle("Frac. Diff.")
        h_compr.GetYaxis().SetTitleFont(132)
        h_compr.GetYaxis().SetTitleSize(.17)
        h_compr.GetYaxis().SetLabelSize(.11)
        h_compr.GetXaxis().SetLabelSize(.11)	
        h_compr.GetYaxis().SetTitleOffset(.25)
	   
        h_compr.SetMinimum(-1.0)
        h_compr.SetMaximum(1.0)
        h_compr.SetLineColor(kRed)
        h_compr.SetLineWidth(2)
        h_compr.SetMarkerColor(kRed)
        h_compr.SetMarkerStyle(1)
        h_compr.SetMarkerSize(0.0)
	
        h_compr.Draw("ep")
        line0.Draw("SAME")
        print "Made the chi2 plots"
    c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".png");
    c1.Print("PlotsSingleSub_mumu2012/"+variable+"_"+tag+".eps");

def GetSelections(ifile):
    import csv
    csvfile=open(ifile,'r')
    WriteToSelection=False
    WriteToSelection_emu=False
    WriteToSelection_qcd=False
    Selections=['','','']
    for row in csv.reader(csvfile):
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
    return Selections


def plot():
    JustIntegrate=False
    drawSub = False
    use_emu = True
    ttscaler = 0.566 #0.630454545922 #0.62016483283 #0.567190832357 #0.5814
    #znorm = 0.931898

    znorm =  0.97647964662  #0.969409814891    #+/-0.00628962930326

    #znorm = 0.988282869379  #0.981183421074 # With Darin's Sel
    #znorm = 0.97647964662
    #znorm = 0.976720712482
    #znorm = 1.0
    #Trigger = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = ''

    #znorm=0.64
    #znorm=1.0

    #znorm=1.0

    if znorm==1.0:
        #Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1ele2>0.3)*((abs(Eta_muon1)<2.5)*(abs(Eta_HEEPele2)<2.5))*(M_HEEPele1ele2>80)*(M_HEEPele1ele2<100))*(ST_pf_ee_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        #Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.5)*(abs(Eta_muon1)<2.5))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 250)*((Charge_HEEPele1*Charge_muon1)==-1)'
        #Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.5)*(abs(Eta_QCDele2)<2.5))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'
        
        Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>80)*(M_muon1muon2<100))*(ST_pf_mumu_single> 250)'
        Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 250)'
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'

        #Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>80)*(M_muon1muon2<100))*(ST_pf_mumu_single> 500)*((Charge_muon1*Charge_muon2)==-1)'
        #Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 500)*((Charge_HEEPele1*Charge_muon2)==-1)'
        #Selection_qcd = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>80)*(M_muon1muon2<100))*(ST_pf_mumu_single> 500)*((Charge_muon1*Charge_muon2)==1)'

        #Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>125)*(Pt_pfjet2>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>80)*(M_muon1muon2<100))*(ST_pf_mumu> 300)'
        #Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>125)*(Pt_pfjet2>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu> 300)'
        #Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'

        use_emu=False

        #Selection +=Trigger
        #Selection_emu +=Trigger_emu
        #Selection_qcd += Trigger_qcd
    
        lq_choice = "*(LQmass==700)*(LQcoupling==1.0)*(LQisCMu==1)*(1/1000)"

        mbinning = [50,80,100]
        filetag = "ZNormalization"
        xtag = " ["+filetag+"]"
        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_muon1muon2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{#mu#mu}(GeV)  " +xtag  ,znorm, ttscaler,filetag)
        return
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>110))*(ST_pf_mumu_single> 250)'
        
        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = ''  # Just for compatibility with the electron side

    print Selection
    #print '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_pfjet1>45)*(deltaR_muon1muon2>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1))*(M_muon1muon2>110))*(ST_pf_mumu_single> 250)'
    print "------------------------------"
    print Selection_emu
    #print '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
    #exit()

   

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger_qcd

    lq_choice = "*(LQmass==1400)*(LQcoupling==1.0)*(LQisCMu==1)*(1/1000)"

   

    ptbinning = [50,0,1000]
    etabinning = [48,-2.4,2.4]
    mbinning = [50,0,2000]
    stbinning = [50,0,2000]
    vertexbinning = [45,-0.5,44.5]
    jetcountbinning=[9,0,8]

    #ptbinning = [12,0,1000]
    #etabinning = [12,-2.4,2.4]
    #mbinning = [12,0,2000]
    #stbinning = [12,0,2000]
    #vertexbinning = [45,-0.5,44.5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"
    #xtag=""

    print "About to start drawing the Histos..."

    if False:
        filetag = "Fullselection"
        xtag = " ["+filetag+"]"
        #xtag=""
        Selection +='*(ST_pf_mumu_single > 1000)*(max(M_muon1pfjet1,M_muon2pfjet1) > 800)'
        Selection_emu +='*(ST_pf_emu_single > 1000)*(max(M_muon1pfjet1,M_HEEPele1pfjet1) > 800)'
        Selection_qcd += '*(ST_pf_mumu_single > 1000)*(max(M_muon1pfjet1,M_muon2pfjet1) > 800)'

        print lq_choice
        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, False, drawSub, mbinning, "(  (Pt_genmuon1 > Pt_genmuon2) *(Mass_genmuon1genjet) +(Pt_genmuon1 < Pt_genmuon2) *(Mass_genmuon2genjet))", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "FiducialMass" +xtag, znorm, ttscaler,filetag)
        return

        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh","", "M_{ #mu jet} " +xtag, znorm, ttscaler,filetag)
        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single","", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)
        return


    print "Selection = "+ Selection
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, False, drawSub, mbinning, "(  (Pt_genmuon1 > Pt_genmuon2) *(Mass_genmuon1genjet) +(Pt_genmuon1 < Pt_genmuon2) *(Mass_genmuon2genjet))", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "FiducialMass" +xtag, znorm, ttscaler,filetag)
    return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, jetcountbinning, "PFJetCount", "PFJetCount", "PFJetCount", "PFJetCount" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_mumu_single", "ST_pf_emu_single","", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_muon1", "max(Pt_HEEPele1,Pt_muon1)","", "p_{T} (#mu_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd,use_emu , drawSub, ptbinning,  "Pt_muon2", "min(Pt_HEEPele1,Pt_muon1)", "","p_{T} (#mu_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    #return

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_muon2", "Eta_muon1*(Pt_muon1<Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1<Pt_muon1)","", "#eta (#mu_{2}) " +xtag,  znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_muon1", "Eta_muon1*(Pt_muon1>Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1>Pt_muon1)","", "#eta (#mu_{1}) " +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_pfjet1", "Eta_pfjet1", "Eta_pfjet1","#eta (jet_{1}) " +xtag, znorm, ttscaler,filetag)




    
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_muon1muon2", "M_muon1HEEPele1", "", "M_{#mu#mu}(GeV)  " +xtag  ,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_singleLQ_mupfjet_Masshigh", "M_singleLQ_emusel_Masshigh","", "M_{e jet} " +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_muon1pfjet1", "M_HEEPele1pfjet1", "","M_{#mu jet} " +xtag,znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, vertexbinning, "N_Vertices", "N_Vertices", "", "N_{Vertices}" +xtag, znorm, ttscaler,filetag)	


def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        integrate()

main()
