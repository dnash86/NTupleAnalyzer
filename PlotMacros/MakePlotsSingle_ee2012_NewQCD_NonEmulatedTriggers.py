from ROOT import *
import os
import sys
import math
from time import strftime


#from ProcessHistos import *

from CMSStyle import *
from HistoCreation import *
from WeightsAndFilters import *
#from tdrstyle import *
from CMS_lumi import *

#################################
#   Loading trees...


#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_TTBarReRun_2014_03_05_13_19_56/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMu_ReRun_2014_04_30_22_04_51/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_ForEMuFixedElectronEta_2014_07_01_16_02_33/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerSkim_2014_07_20_21_49_58/SummaryFiles'
#Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerSkim_2014_07_20_21_49_58/SummaryFiles'
Files_emu = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_Foremu_EMuLowerFixMuonKinematics_2014_07_30_14_17_53/SummaryFiles'
#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRunOldNTuples_2014_02_25_21_20_15/SummaryFiles'
#Files_ee = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ReRun_OrderFixed_2014_05_06_15_52_31/SummaryFiles'

##  Less skimmed samples
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_ElectronSmallerSkim_2014_06_10_01_46_29/SummaryFiles/'
Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixElectronEta_2014_06_25_01_52_27/SummaryFiles'
#Files_ee='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixBEFilter_2014_06_24_00_50_34/SummaryFiles'
Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDReRunEdmundCS_NoPtJetElimination_2014_02_07_21_29_51/SummaryFiles'
#Files_qcd = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ForQCDStudy_QCDVeryStrict_2014_04_13_21_31_02/SummaryFiles'



#Files_CorrectedSignal = '/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_JustSignalTest_2014_09_21_17_20_04/SummaryFiles'

#Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_JustSignalTest_2014_09_22_16_42_16/SummaryFiles'

#Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_JustSignalTest_2014_09_22_21_08_35/SummaryFiles'

#Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_JustSignalTest_2014_09_23_15_24_21/SummaryFiles'
#Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_SignalDiEleMass_2014_10_27_13_44_10/SummaryFiles'


Files_CorrectedSignal='/store/user/dnash/LQAnalyzerOutput2/NTupleAnalyzer_V00_02_06_David_2012_ElectronStrict_FixedGenMassesStatusOne_2014_10_29_16_54_57/SummaryFiles'
#OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_ValuesSSB.txt'
#OptimizationFile = '/afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/Ele_SSB_log2.txt'
#OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/EleModifiedValues.txt'
OptimizationFile='/afs/cern.ch/user/d/dnash/SingleLQAnalysis/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/EleOptimizationJust1p0.txt'
#OptimizationFile = '/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/PlotMacros/EleModifiedValues_0p4split.txt'


TreeName = 'PhysicalVariables'

Trigger = '*(CurrentDoubleElePass>0.5)'
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
FiducialIntegrateOnly=False
FileLocation='blank'
ZShapeFile='blank'
ExtraCutsBool=False
tdrstyle=False
AddCuts=''
WhichPU=0   #WhichPU = 0 means central values for pileup, -1 means varied down and 1 means varied up
for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input_cutcard':
        InputCuts=True
        ifile=a[n+1]
        print "Will use the input cut card for selection"
    if a[n]=='-r' or a[n]=='--input_rescales':
        RescaleCuts=True
        rfile=a[n+1]
        print "Will use a rescale card"
    if a[n]=='-p' or a[n]=='--plot':
        PlotHistos=True
    if a[n]=='-I' or a[n]=='--integrate':
        IntegrateOnly=True
    if a[n]=='-F' or a[n]=='--fiducial_integrate':
        FiducialIntegrateOnly=True
        MassForFiducialStudy=a[n+1]
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
        Files_CorrectedSignal=a[n+2]
    if a[n]=='-n' or a[n]=='--new_signal':
        SignalFileLocation = a[n+1]
    if a[n]=='-pd' or a[n]=='--pileup_down':
        WhichPU=-1
    if a[n]=='-pu' or a[n]=='--pileup_up':
        WhichPU=1
    if a[n]=='-s' or a[n]=='--shape_errors':
        ZShapeFile = a[n+1]  
    if a[n]=='-A' or a[n]=='--additional_cuts':
        ExtraCutsBool=True
        ExtraCuts=a[n+1]
        ExtraCutsValue = a[n+2]
    if a[n]=='-tdr' or a[n]=='--use_tdr_style':
        tdrstyle=True
        from tdrstyle import *
    if a[n]=='-fid' or a[n]=='--fiducial_cuts':
        AddCuts = "*(  (Pt_genelectron1 > Pt_genelectron2) *(Mass_genelectron1genjet > 1000*0.66) +(Pt_genelectron1 < Pt_genelectron2) *(Mass_genelectron2genjet > 1000*0.66)  ) *(Mass_genele1ele2 > 110)"
        #for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
            
        #exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
if not InputCuts:
    print "No input cut card, will use standard selection"




print "Loading..."
print Files_ee
print FileLocation
if FileLocation=='blank':
    #------Hacked for new signal files use with a ''
    for f in os.popen('cmsLs '+Files_ee+'| grep ".root" | gawk \'{print $NF}\' | grep -v LQToUE | gawk -F "/" \'{print $NF}\'').readlines():
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
        print f
    for f in os.popen('cmsLs '+Files_CorrectedSignal+'| grep ".root" | gawk \'{print $NF}\'  | gawk -F "/" \'{print $NF}\'').readlines():
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")


else:
    #------Hacked for new signal files use with a ''
    print "DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")"
    exec("DoublePhotonData= TFile.Open(\"root://eoscms//eos/cms/"+Files_ee+"/"+"DoublePhotonData.root"+"\")"+".Get(\""+TreeName+"\")")   
    for f in os.popen('cmsLs '+FileLocation+'| grep ".root" | gawk \'{print $NF}\' | grep -v LQToUE | gawk -F "/" \'{print $NF}\'').readlines():
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+FileLocation+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")       
    for f in os.popen('cmsLs '+Files_CorrectedSignal+'| grep ".root" | gawk \'{print $NF}\'  | gawk -F "/" \'{print $NF}\'').readlines():
        #print f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")"
        exec(f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_CorrectedSignal+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

    
for f in os.popen('cmsLs '+Files_emu+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('emu_'+f.replace('-','_').replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_emu+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    print 'emu_'+f.replace('-','_').replace(".root\n","")

for f in os.popen('cmsLs '+Files_qcd+'| grep ".root" | grep -v LQTo | gawk \'{print $NF}\' | gawk -F "/" \'{print $NF}\'').readlines():
    exec('qcd_'+f.replace(".root\n","")+" = TFile.Open(\"root://eoscms//eos/cms/"+Files_qcd+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
    #print 'qcd_'+f.replace('-','_').replace(".root\n","")
print "...done loading"

if ZShapeFile != 'blank':
    del ZJetsJBin
    ZJetsJBin = TFile.Open("root://eoscms//eos/cms/"+ZShapeFile).Get(TreeName)


###############################################

def test():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.5)*(abs(Eta_HEEPele2)<2.5))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.5)*(abs(Eta_HEEPele1)<2.5))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.5)*(abs(Eta_QCDele2)<2.5))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    ftmp = TFile.Open("garbage.root","RECREATE")
    print "On DoublePhotonData:"

    LookForDuplicates(DoublePhotonData,Selection)
    return

    PrintTestInfo(DoublePhotonData,Selection)
    print "On Diboson:"
    PrintTestInfo(DiBoson,Selection)
    print "On Gjets:"
    PrintTestInfo(Gjets,Selection)

    print "On SingleTop:"
    PrintTestInfo(SingleTop,Selection)
    print "On TTBarMC:"
    PrintTestInfo(TTBarDBin,Selection)
    print "On WJets:"
    PrintTestInfo(WJetsJBin,Selection)
    print "On ZJets:"
    PrintTestInfo(ZJetsJBin,Selection)

    print "On Signal:"
    PrintTestInfo(LQToUE_Single_L_0p2,Selection)
    PrintTestInfo(LQToUE_Single_L_0p4,Selection)
    PrintTestInfo(LQToUE_Single_L_0p6,Selection)
    PrintTestInfo(LQToUE_Single_L_0p8,Selection)
    PrintTestInfo(LQToUE_Single_L_1p0,Selection)

def PrintTestInfo(tree,Selection):
    TestData = tree.CopyTree(Selection)
    for n in range(TestData.GetEntries()):
        TestData.GetEntry(n)
        if TestData.Pt_HEEPele1 < TestData.Pt_HEEPele2:
            #print "Found a flip in "+str(tree)
            if (TestData.Pt_HEEPele2-TestData.Pt_HEEPele1)>5.0:
                print "-----------> Its Big: "
            print str(TestData.Pt_HEEPele1)+", "+str(TestData.Pt_HEEPele2)  
    
def LookForDuplicates(tree,Selection):
    TestData = tree.CopyTree(Selection)
    ListofEventNumbers=[]
    for n in range(TestData.GetEntries()):
        TestData.GetEntry(n)
        AlreadyInList=0
        for EventNumber in ListofEventNumbers:
            if TestData.event_number == EventNumber:
                AlreadyInList += 1
                if AlreadyInList > 1: 
                    print "Double Duplicate event: "+ str(TestData.event_number)
        if AlreadyInList > 0:
            ListofEventNumbers.append(TestData.event_number)
    print ListofEventNumbers
            

def integrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
        
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    if RescaleCuts:
        AdditionalSelections=GetRescaleSelections(rfile)
        Selection += AdditionalSelections[0]
        Selection_emu += AdditionalSelections[1]
        Selection_qcd += AdditionalSelections[2]

    #Trigger = '*(CurrentDoubleElePass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'

    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger     
    
    JustIntegrate=True
    drawSub = False
    use_emu = True
    #ttscaler = 0.5942599
    #znorm = 0.98580048415651985403

    Z_Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>80)*(M_HEEPele1ele2<100))*(ST_pf_ee_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
    Z_Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
    Z_Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)*((Charge_HEEPele1*Charge_HEEPele2)==1)'
    use_emu=False
    
    mbinning = [20,80,100]
    lq_choice = "*(LQmass==1000)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"
    filetag = "ZNormalization"

    ttscaler =  0.435 
    JustIntegrate=False
    xtag = ""
    znorm=1.0
    znorm = DrawHisto(JustIntegrate,lq_choice, Z_Selection, Z_Selection_emu, Z_Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)
    
    print "Znorm = "+str(znorm)

    ttscaler = FindNormalization(Selection,Selection_emu)
    print "ttscaler = " +str(ttscaler)

    JustIntegrate=True
    use_emu = True


     
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    for i in range(5):
        if i == 0:
            MassRangeLength = 16
            Coupling = "L-0p2"
        if i == 1:
            MassRangeLength = 16
            Coupling = "L-0p4"
        if i == 2:
            MassRangeLength = 25
            Coupling = "L-0p6"
        if i == 3:
            MassRangeLength = 25
            Coupling = "L-0p8"
        if i == 4:
            MassRangeLength = 31
            Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==0)*(LQcoupling=="+str( (float)(i+1)/5)+")*(1/1000)"
            print "My lq choice I'm on now is: "+lq_choice
            AdditionalCut = ""
            if ExtraCutsBool:
                #AdditionalCut="*"+ExtraCuts+"["+str(ExtraCutsValue)+"]"
                #AdditionalCut = "*(Mass_genelectron1genjet > "+str(float(x)*0.4)+")"
                AdditionalCut = "*(Mass_genelectron1genjet > 0.0)"
            #print lq_choice
            #Cuts=os.popen("grep -A 1 "+Coupling+ " /afs/cern.ch/work/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/Optimization/Ele_SSB_log2.txt  | grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')



            if IntegrateOnly:
                Cuts=os.popen("grep -A 1 "+Coupling+" " + OptimizationFile + "| grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')
                Cuts_emu=Cuts.replace('epfjet','emusel').replace('ee','emu')
            if PreselIntegrateOnly:
                Cuts="1.0"
                Cuts_emu='1.0'
            IntsAndErrs =  GetIntegralsAndErrors(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Cuts_emu+"*"+Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)
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

            if RescaleCuts:
                ptllbinning=[12,90,1290]

                Error=DrawHisto(JustIntegrate,lq_choice, Cuts+"*"+Selection+AdditionalCut, Cuts_emu+"*"+Selection_emu+AdditionalCut, Cuts+"*"+Selection_qcd+AdditionalCut , use_emu, true, ptllbinning, "(Pt_HEEPele1+Pt_HEEPele2)", "(Pt_HEEPele1+Pt_HEEPele2)","", "p_{T}(ll) (GeV)" +xtag, znorm, ttscaler,filetag)
                print "Error is:"
                print Error
                File = open(OutputIntegralsFile+"_RescaleError.txt",'a') 
                File.write(str(Error)+'\n')
                File.close()
                
            
            
           

def fidintegrate():
    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPUUp
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPUDown

    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
        
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    JustIntegrate=True
    drawSub = False
    use_emu = True
     
    chargebinning=[11,-5,5]

    filetag = "Preselection"
    xtag = " ["+filetag+"]"

    Coupling = "L-1p0"
    x=MassForFiducialStudy
    Cuts=os.popen("grep -A 1 "+Coupling+" " + OptimizationFile + "| grep -A 1 \"Mass = " + str(x) + "\" | grep ST_pf").readline().replace('\n','')

    lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"


    values=[y*0.0125 for y in range(60)]    
    #values=[y*0.1 for y in range(10)]    

    print "Opening file"
    File = open(OutputIntegralsFile+".txt",'w') 
    for value in values:

        AdditionalCut = "*(  (Pt_genelectron1 > Pt_genelectron2) *(Mass_genelectron1genjet > "+str(float(x)*value)+") +(Pt_genelectron1 < Pt_genelectron2) *(Mass_genelectron2genjet > "+str(float(x)*value)+")  ) *(Mass_genele1ele2 > 110)"
        signaltrees=[LQToUE_Single_L_0p2,LQToUE_Single_L_0p4,LQToUE_Single_L_0p6,LQToUE_Single_L_0p8,LQToUE_Single_L_1p0]
        signalweights = [1,1,1,1,1]
        selection=Selection
        signalselections = [Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut,Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut,Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut,Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut,Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut]

        #print Cuts+"*"+selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice+AdditionalCut
        SignalValues=IntegralAndError(signaltrees,signalweights,signalselections)
        #print "Cut = "+str(float(x)*value)
        print SignalValues[0]
        File.write(str(SignalValues[0])+'\n')

    File.close()
                   
def preselintegrate():
    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'
        
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    

    #Trigger = '*(CurrentDoubleElePass>0.5)'
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

    for i in range(5):
        if i == 0:
            MassRangeLength = 16
            Coupling = "L-0p2"
        if i == 1:
            MassRangeLength = 16
            Coupling = "L-0p4"
        if i == 2:
            MassRangeLength = 25
            Coupling = "L-0p6"
        if i == 3:
            MassRangeLength = 25
            Coupling = "L-0p8"
        if i == 4:
            MassRangeLength = 31
            Coupling = "L-1p0"

        for x in [(300+100*y) for y in range(MassRangeLength)]:
            lq_choice = "*(LQmass=="+str(x)+")*(LQisCMu==0)*(LQcoupling=="+str( (float)(i+1)/5)+")*(1/1000)"
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

    signaltrees=[LQToUE_Single_L_0p2,LQToUE_Single_L_0p4,LQToUE_Single_L_0p6,LQToUE_Single_L_0p8,LQToUE_Single_L_1p0]
    signalweights = [1,1,1,1,1]
    signalselections = [selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice]

    SignalValues=IntegralAndError(signaltrees,signalweights,signalselections)

    DataValues=IntegralAndError([DoublePhotonData],[1],[selection+Filters+Trigger])

    WJetsValues=IntegralAndError([WJetsJBin],[1],[selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])
    DiBosonValues=IntegralAndError([DiBoson],[1],[selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])
    SingleTopValues=IntegralAndError([SingleTop],[1],[selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])
    ZJetsValues=IntegralAndError([ZJetsJBin],[1],[selection+'*('+str(zscale)+')'+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])

    print "On TTBar now"
    if use_emu:
        ttbartrees=[emu_SingleMuData,emu_WJetsJBin,emu_DiBoson,emu_ZJetsJBin,emu_SingleTop]
        ttbarweights=[1,-1,-1,-1,-1]
        ttbarselections=[emuselection+'*('+str(ttscaler)+')'+Filters+Trigger_emu+R_ee_over_mu,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,emuselection+'*('+str(ttscaler)+')'+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters]

        TTBarValues=IntegralAndError(ttbartrees,ttbarweights,ttbarselections)

    else:
        TTBarValues=IntegralAndError([TTBarDBin],[1],[selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])

   
    GJetsValues=IntegralAndError([Gjets],[1],[selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters])

    if (zscale != 1.00):
        if True:
            qcdtrees=[DoublePhotonData,WJetsJBin,DiBoson,ZJetsJBin,SingleTop,Gjets,TTBarDBin]
            qcdweights=[1,-1,-1,-1,-1,-1,-1]
            qcdselections=[qcdselection+Filters+Trigger,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters]

            QCDValues=IntegralAndError(qcdtrees,qcdweights,qcdselections)
           
    if JustIntegrate:
        ValuesString= str(DataValues[0])+","+str(TTBarValues[0]) + "," + str(ZJetsValues[0]) + "," + str(DiBosonValues[0]) + "," + str(SingleTopValues[0]) + "," + str(WJetsValues[0]) + "," + str(GJetsValues[0]) + ","+str(QCDValues[0]) + "," + str(SignalValues[0])
        ErrorsString= str(DataValues[1])+","+str(TTBarValues[1]) + "," + str(ZJetsValues[1]) + "," + str(DiBosonValues[1]) + "," + str(SingleTopValues[1]) + "," + str(WJetsValues[1]) + "," + str(GJetsValues[1]) + ","+str(QCDValues[1]) + "," + str(SignalValues[1])
        EntriesString= str(DataValues[2])+","+str(TTBarValues[2]) + "," + str(ZJetsValues[2]) + "," + str(DiBosonValues[2]) + "," + str(SingleTopValues[2]) + "," + str(WJetsValues[2]) + "," + str(GJetsValues[2])+ "," + str(QCDValues[2]) + "," + str(SignalValues[2])
        return [ValuesString,ErrorsString,EntriesString]
                   
    
    


def FindNormalization(selection, emuselection):

    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPUUp
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPUDown
    
    TTStackStyle=[3005,21,.00001,2,4]
    binning= [10,0,5000]
    h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,"Pt_HEEPele1",binning,selection+CorrectLumiAndPU+Filters,TTStackStyle,"label")
    h_TTBar_emusel=MakeHisto('h_TTBar','t#bar{t}',emu_TTBarDBin,"Pt_muon1",binning,emuselection+CorrectLumiAndPU+Filters,TTStackStyle,"label")

    #print selection
    #print emuselection
    #print h_TTBar.Integral()
    #print h_TTBar_emusel.Integral()
    print "Scale fac = " + str(h_TTBar.Integral()/h_TTBar_emusel.Integral())

    htt=TH1D('htt','htt',1,-1,3)
    httemu=TH1D('httemu','httemu',1,-1,3)
    htt.Sumw2()
    httemu.Sumw2()

    TTBarDBin.Project('htt','1.0',selection+LumiAndPU+Filters)
    emu_TTBarDBin.Project('httemu','1.0',emuselection+LumiAndPU+Filters)
    htt.Divide(httemu)

    #print str(round(htt.GetBinContent(1),3)) +"+/-" +str(round(htt.GetBinError(1),3))
    
    return (h_TTBar.Integral()/h_TTBar_emusel.Integral())



def DrawHisto(JustIntegrate,lq_choice, selection, emuselection, qcdselection, use_emu, drawSub, binning, variable, variable_emu, variable_qcd, xlabel,zscale,ttscaler,tag):
    
    channel = "ee"
    Luminosity = "19.6"

    if WhichPU==0:
        CorrectLumiAndPU=LumiAndPU
    if WhichPU==1:
        CorrectLumiAndPU=LumiAndPUUp
    if WhichPU==-1:
        CorrectLumiAndPU=LumiAndPUDown

    MaxRescaler=10.

    if True:
        MaxRescaler=100.
    if True:
        MaxRescaler=1500.

    if True:
        MaxRescaler=500.
    if zscale==1.0:
        MaxRescaler=10000
    if "N_Vertices" in variable:
        MaxRescaler = 1000.
    if "delta" in variable:
        MaxRescaler=10000.
    if "Eta" in variable:
        MaxRescaler = 1000.
    # Set canvases

    if tdrstyle:
        print "Setting tdrstyle"
        setTDRStyle()

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
        #pad1 = TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0)	
        pad1 = TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0)	
        pad1.Draw()
        
    pad1.cd()
    pad1.SetLogy()
    
    # Set gStyle
    gStyle.SetOptLogy()
    gStyle.SetOptStat(0)
    
    #else:
    #    SetStyle()

    #Make the label
    Label=[xlabel,"Events / "+str((binning[2]-binning[1])/binning[0])+" GeV"]
    
    #Set the style for each dataset   Format:  FillStyle,MarkerStyle,MarkerSize,LineWidth,Colors
    DataRecoStyle=[0,2,0.0,2,1]
    
    WStackStyle=[3017,21,.00001,2,9]
    #WStackStyle=[3254,21,.00001,2,9]

    TTStackStyle=[3005,21,.00001,2,4]
    ZStackStyle=[3004,21,.00001,2,2]
    DiBosonStackStyle=[3006,21,.00001,2,9]
    StopStackStyle=[3006,21,.00001,2,3]
    QCDStackStyle=[3018,21,.00001,2,3]
    GJetsStackStyle=[3009,21,.00001,2,5]

    

    SignalStyle=[0,1,0.0,3,1]
    

    ### Make the plots
    
    #print selection
    h_Signal=MakeHisto('h_Signal','LQToUE_Single_L_0p2',LQToUE_Single_L_0p2,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,SignalStyle,Label)
    h_LQToUE_Single_L0p4=MakeHisto('h_LQToUE_Single_L0p4','LQToUE_Single_L0p4',LQToUE_Single_L_0p4,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p4)
    h_LQToUE_Single_L0p6=MakeHisto('h_LQToUE_Single_L0p6','LQToUE_Single_L0p6',LQToUE_Single_L_0p6,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p6)
    h_LQToUE_Single_L0p8=MakeHisto('h_LQToUE_Single_L0p8','LQToUE_Single_L0p8',LQToUE_Single_L_0p8,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L0p8)
    h_LQToUE_Single_L1p0=MakeHisto('h_LQToUE_Single_L1p0','LQToUE_Single_L1p0',LQToUE_Single_L_1p0,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters+lq_choice,SignalStyle,Label)
    h_Signal.Add(h_LQToUE_Single_L1p0)

    h_Data=MakeHisto('h_Data','Data',DoublePhotonData,variable,binning,selection+Filters+Trigger,DataRecoStyle,Label)
    h_DataDummy=MakeHisto('h_DataDummy','DataDummy',DoublePhotonData,variable,binning,selection+Filters+Trigger,DataRecoStyle,Label)

    h_WJets=MakeHisto('h_WJets','W+Jets',WJetsJBin,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,WStackStyle,Label)
    h_DiBoson=MakeHisto('h_DiBoson','DiBoson',DiBoson,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,DiBosonStackStyle,Label)
    h_SingleTop=MakeHisto('h_SingleTop','SingleTop',SingleTop,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,StopStackStyle,Label)    

    h_ZJets=MakeHisto('h_ZJets','Z+Jets',ZJetsJBin,variable,binning,selection+'*('+str(zscale)+')'+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,ZStackStyle,Label)
    #print "Made the normal plots"

    if use_emu:
        print R_ee_over_mu
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',emu_SingleMuData,variable_emu,binning,emuselection+Filters+Trigger_emu+R_ee_over_mu,TTStackStyle,Label)
        h_emu_WJets=MakeHisto('h_emu_WJets','W+Jets',emu_WJetsJBin,variable_emu,binning,emuselection+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,TTStackStyle,Label)
        h_emu_DiBoson=MakeHisto('h_emu_DiBoson','DiBoson',emu_DiBoson,variable_emu,binning,emuselection+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,TTStackStyle,Label)
        h_emu_ZJets=MakeHisto('h_emu_ZJets','Z+Jets',emu_ZJetsJBin,variable_emu,binning,emuselection+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,TTStackStyle,Label)
        h_emu_SingleTop=MakeHisto('h_emu_SingleTop','SingleTop',emu_SingleTop,variable_emu,binning,emuselection+CorrectLumiAndPU+SingleMuNonEmulatedTrigger+R_ee_over_mu+Filters,TTStackStyle,Label)
        #h_emu_GJets=MakeHisto('h_Gjets','t#bar{t}',emu_Gjets,variable,binning,tt_sel_weight,GJetsStackStyle,Label)

        h_TTBar.Add(h_emu_WJets,-1)
        h_TTBar.Add(h_emu_DiBoson,-1)
        h_TTBar.Add(h_emu_ZJets,-1)
        h_TTBar.Add(h_emu_SingleTop,-1)

        h_TTBar.Scale(ttscaler)
    else:
        h_TTBar=MakeHisto('h_TTBar','t#bar{t}',TTBarDBin,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,TTStackStyle,Label)

    #print "Made the ttbar plots"

    #If the channel is ee, include G Jets background and the QCD fake rate sample
    h_GJets=MakeHisto('h_GJets','#gamma+Jets',Gjets,variable,binning,selection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,GJetsStackStyle,Label)
    if (zscale != 1.00):

        #if (zscale != 1.00):
        if True:
            h_QCD=MakeHisto('h_QCD','Data',DoublePhotonData,variable,binning,qcdselection+Filters+Trigger,QCDStackStyle,Label)

            h_qcd_WJets=MakeHisto('h_qcd_WJets','W+Jets',WJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,WStackStyle,Label)
            h_qcd_DiBoson=MakeHisto('h_qcd_DiBoson','DiBoson',DiBoson,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,DiBosonStackStyle,Label)
            h_qcd_ZJets=MakeHisto('h_qcd_ZJets','Z+Jets',ZJetsJBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,ZStackStyle,Label)
            h_qcd_SingleTop=MakeHisto('h_qcd_SingleTop','SingleTop',SingleTop,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,StopStackStyle,Label)
            h_qcd_GJets=MakeHisto('h_qcd_Gjets','#gamma+Jets',Gjets,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,GJetsStackStyle,Label)
            h_qcd_TTBar=MakeHisto('h_qcd_TTBar','t#bar{t}',TTBarDBin,variable,binning,qcdselection+CorrectLumiAndPU+DoubleENonEmulatedTrigger+Filters,TTStackStyle,Label)

            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_WJets,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_DiBoson,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_ZJets,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_SingleTop,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_GJets,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            h_QCD.Add(h_qcd_TTBar,-1)
            print "QCD Integral = " + str(h_QCD.Integral())
            
            nBins = binning[0]
           

        #else:
            #h_QCD=MakeHisto('h_qcd_Data','Data',qcd_SinglePhotonData,variable_qcd,binning,qcdselection+Filters,DataRecoStyle,Label)
            #h_QCD.Scale(0.0000000000000001) 
    
            #print "Made the QCD plots"


    if (JustIntegrate and not RescaleCuts):
        return str(h_Data.Integral())+","+str(h_TTBar.Integral()) + "," + str(h_ZJets.Integral()) + "," + str(h_DiBoson.Integral()) + "," + str(h_SingleTop.Integral()) + "," + str(h_WJets.Integral()) + "," + str(h_GJets.Integral()) + ","+str(h_QCD.Integral()) + "," + str(h_Signal.Integral())
        
    #If the channel is mumu, no need to include G Jets and use the mu enriched QCD sample
    #if channel = "mumu":
    #    h_QCDMu=MakeHisto('h_QCDMu','QCD',QCDMu,variable,binning,tt_sel_weight,QCDStackStyle,Label)
                                   

    #Adding up backgrounds...
    h_WJets.SetTitle("Other Backgrounds")
    h_WJets.Add(h_DiBoson)
    h_WJets.Add(h_SingleTop)
    h_WJets.Add(h_GJets)
    if (zscale !=1.00):
        Backgrounds=[h_WJets,h_QCD,h_TTBar,h_ZJets]
    else:
        Backgrounds=[h_WJets,h_TTBar,h_ZJets]
    #Backgrounds=[h_WJets,h_TTBar,h_ZJets]

    print "W_Jets = " + str(h_WJets.Integral())
    MCStack = THStack ("MCStack","")
    BackgroundIntegral = sum(k.Integral() for k in Backgrounds)
    DataIntegral = h_Data.Integral()
    ZIntegral = h_ZJets.Integral()

    SigmaData = math.sqrt(DataIntegral)
    SigmaNonZ = 0
    if (zscale !=1.00):
        NonZSigmaBackgrounds=[h_WJets,h_QCD,h_TTBar]
    else:
        NonZSigmaBackgrounds=[h_WJets,h_TTBar]
    for bg in Backgrounds:
        if bg.GetEntries() > 0:
            SigmaNonZ += bg.Integral() * math.pow(bg.GetEntries(),-0.5)
    if (h_ZJets.GetEntries() > 0):
        SigmaZ = h_ZJets.Integral()*math.pow(h_ZJets.GetEntries(),-0.5)

    print "Data = " + str(DataIntegral)
    print "Background = " + str(BackgroundIntegral)
    if (h_TTBar.GetEntries()>0):
        print "tt : " + str(h_TTBar.Integral()) + "+/-" +str( h_TTBar.Integral()* math.pow(h_TTBar.GetEntries(),-0.5) )
    if (h_ZJets.GetEntries()>0):
        print "z : " + str(ZIntegral) + "+/-" +str( h_ZJets.Integral()* math.pow(h_ZJets.GetEntries(),-0.5) )
    if (zscale !=1.00):
        print "qcd : " + str(h_QCD.Integral())
    print "Signal : " +str(h_Signal.Integral())
        
    if (ZIntegral >0):
        ZfracNumerator = DataIntegral - (BackgroundIntegral - ZIntegral)
        ZfracDenominator = ZIntegral
        Zfrac = ZfracNumerator/ ZfracDenominator
    
        SigmaZfracNumerator = math.sqrt(math.pow(SigmaData,2)+math.pow(SigmaNonZ,2))
        SigmaZfracDenominator = SigmaNonZ
    
        if (ZfracNumerator>0):
            SigmaZfrac = Zfrac * math.pow( (math.pow(SigmaZfracNumerator/ZfracNumerator,2) +math.pow(SigmaZfracDenominator/ZfracDenominator,2) ),0.5)
        
            print "Z Scale Factor: " + str(Zfrac) + "+/-"+str(SigmaZfrac)

    nbinsx = binning[0]	
    for ibin in range(nbinsx):

        BackgroundIntegralBinned = sum(k.GetBinContent(ibin) for k in Backgrounds)
        DataIntegralBinned = h_Data.GetBinContent(ibin)
        ZIntegralBinned = h_ZJets.GetBinContent(ibin)
        SigmaNonZBinned = 0
        if (zscale !=1.00):
            NonZSigmaBackgrounds=[h_WJets,h_QCD,h_TTBar]
        else:
            NonZSigmaBackgrounds=[h_WJets,h_TTBar]
            for bg in Backgrounds:
                SigmaNonZBinned += bg.GetBinError(ibin)


        SigmaDataBinned = math.sqrt(DataIntegralBinned)

        if (DataIntegralBinned!=0 and BackgroundIntegralBinned != 0):
            ZfracNumeratorBinned = DataIntegralBinned - (BackgroundIntegralBinned - ZIntegralBinned)
            ZfracDenominatorBinned = ZIntegralBinned
            if (ZfracDenominatorBinned>0):
                ZfracBinned = ZfracNumeratorBinned/ ZfracDenominatorBinned
        
                SigmaZfracNumeratorBinned = math.sqrt(math.pow(SigmaDataBinned,2)+math.pow(SigmaNonZBinned,2))
                SigmaZfracDenominatorBinned = SigmaNonZBinned
        
                SigmaZfracBinned = ZfracBinned * math.pow( (math.pow(SigmaZfracNumeratorBinned/ZfracNumeratorBinned,2) +math.pow(SigmaZfracDenominatorBinned/ZfracDenominatorBinned,2) ),0.5)

                print str(h_Data.GetXaxis().GetBinLowEdge(ibin))+","+str(h_Data.GetXaxis().GetBinUpEdge(ibin))+","+str(ZfracBinned)+","+str(SigmaZfracBinned)

    if (RescaleCuts and variable=="(Pt_HEEPele1+Pt_HEEPele2)"):
        print "here now"
        TotalRescaleError=0
        RescaleError=GetRescaleValues(rfile)
        for ibin in range(len(RescaleError)):
            TotalRescaleError+=(h_ZJets.GetBinContent(ibin+1)*float(RescaleError[ibin]))
        return TotalRescaleError

    if (zscale == 1.0):
        File = open('ZScale_ee.tex','w')
        File.write('\begin{tabular}{|c|c|}\n')
        File.write('{Z}  & {'+str(round(h_ZJets.Integral(),2))+'} \\\\\n')

        File.write('\hline\n')
        File.write('{Data}  & {'+str(round(DataIntegral,2))+'} \\\\\n')
        File.write('{$t\bar{t}$}  & {'+str(round(h_TTBar.Integral(),2))+'} \\\\\n')
        File.write('{Single Top}  & {'+str(round(h_SingleTop.Integral(),2))+'} \\\\\n')
        File.write('{DiBoson}  & {'+str(round(h_DiBoson.Integral(),2))+'} \\\\\n')
        File.write('{W}  & {'+str(round(h_WJets.Integral(),2))+'} \\\\\n')
        #File.write('{QCD}  & {'+str(round(h_QCD.Integral(),2))+'} \\\\\n')
        File.write('\hline\n')
        File.write('\hline\n')
        File.write('{$R_{Z}$}  & {'+str(round(Zfrac,2))+"+/-"+str(round(SigmaZfrac,2))+'} \\\\\n')
        File.write('\end{tabular}\n')
        File.close()

    #print 'Stacking...  '	
    for histo in Backgrounds:
        MCStack.Add(histo)
        histo.SetMaximum(MaxRescaler*h_Data.GetMaximum())
                                   
    MCStack.Draw("HIST")
    c1.cd(1).SetLogy()

    MCStack.SetMinimum(.1)
    MCStack.SetMaximum(MaxRescaler*h_Data.GetMaximum())                              
    MCStack=BeautifyStack(MCStack,Label)
    h_Signal.SetLineStyle(3)
    h_Signal.Draw("HISTSAME")
    #h_Signal.Draw("HISTSAME")
    h_Data.Draw("HISTEPSAME")

    leg=TLegend(0.4,0.55,0.85,0.89,"","brNDC")
    leg.SetTextFont(42)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)

    h_DataDummy.SetMarkerSize(1.)
    #leg.AddEntry(h_DataDummy,"Data 2012, "+Luminosity+" fb^{-1}, 8 TeV")
    leg.AddEntry(h_DataDummy,"Data")
    leg.AddEntry(h_ZJets,"Z/#gamma* + jets")



    if (not use_emu):
        leg.AddEntry(h_TTBar,"t#bar{t}")
    if (use_emu):
        leg.AddEntry(h_TTBar,"t#bar{t} based on data")
	


    if (zscale !=1.00):
        print "did do this, now am not"
        leg.AddEntry(h_QCD,"QCD")
    leg.AddEntry(h_WJets,"Other backgrounds")
    leg.AddEntry(h_Signal,"LQ Mass = 1000 GeV, #lambda = 0.4, #beta = 1.0")
    leg.Draw("SAME")

    h_Data.SetMinimum(.1)
    h_Data.SetMaximum(MaxRescaler*(h_Data.GetMaximum()))
    
    print h_Data.GetYaxis().GetTitle()


    #h_Data.GetYaxis().SetTitleOffset(-0.75)

    
    
    #h_Data.GetYaxis().Draw("SAME")
    #h_Data.GetXaxis().Draw("SAME")

    #txt = TLatex((binning[2]-binning[1])*.04+binning[1],.15*5.0*h_Data.GetMaximum(), "CMS Preliminary")
    #txt.SetTextFont(42)
    #txt.SetTextSize(0.06)
    #txt.Draw()


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
                #print str(h_Data.GetXaxis().GetBinLowEdge(ibin))+","+str(h_Data.GetXaxis().GetBinUpEdge(ibin))+","+str(1+(ndat - nbg)/nbg)+","+str((err_total)/nbg)

        h_comp.GetYaxis().SetTitle("N(#sigma) Diff.")
        h_comp.GetYaxis().SetTitleFont(42)
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
        h_compr.GetYaxis().SetTitleFont(42)
        h_compr.GetYaxis().SetTitleSize(.17)
        h_compr.GetYaxis().SetLabelSize(.11)
        h_compr.GetXaxis().SetLabelSize(.11)	
        h_compr.GetYaxis().SetTitleOffset(.25)
	   
        h_compr.SetMinimum(-2.0)
        h_compr.SetMaximum(2.0)
        h_compr.SetLineColor(kRed)
        h_compr.SetLineWidth(2)
        h_compr.SetMarkerColor(kRed)
        h_compr.SetMarkerStyle(1)
        h_compr.SetMarkerSize(0.0)
	
        h_compr.Draw("ep")
        line0.Draw("SAME")
        print "Made the chi2 plots"

    CMS_lumi(pad1,2,0)
    if UseOutputDir:
        c1.Print(OutputDir+"/"+variable+"_"+tag+".png");
        c1.Print(OutputDir+"/"+variable+"_"+tag+".pdf");
    else:
        c1.Print("PlotsSingleSub_ee2012/"+variable+"_"+tag+".png");
        c1.Print("PlotsSingleSub_ee2012/"+variable+"_"+tag+".pdf");


    return Zfrac

   
def GetRescaleValues(rfile):
    import csv
    csvfile=open(rfile,'r')
    Selection=[]
    WriteToSelection=False
    for row in csv.reader(csvfile):
        if row[0] == "#Selection":
            WriteToSelection=True
        if row[0] == "#Selection_emu":
            WriteToSelection=False
        if row[0] == "#Selection_qcd":
            WriteToSelection=False
        if (row[0][0]!='#') and (len(row)==5):
            if WriteToSelection:
                Selection.append(row[4])
    return Selection


def GetRescaleSelections(rfile):
    import csv
    csvfile=open(rfile,'r')
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
        if (row[0][0]!='#') and (len(row)==5):
            if WriteToSelection:
                if Selections[0]!='': Selections[0] += '+'
                Selections[0] += '('+row[0]+'>'+row[1]+')*('+row[0]+'<'+row[2]+')*('+row[3]+')'
            if WriteToSelection_emu:
                if Selections[1]!='': Selections[1] += '+'
                Selections[1] += '('+row[0]+'>'+row[1]+')*('+row[0]+'<'+row[2]+')*('+row[3]+')'
            if WriteToSelection_qcd:
                if Selections[2]!='': Selections[2] += '+'
                Selections[2] += '('+row[0]+'>'+row[1]+')*('+row[0]+'<'+row[2]+')*('+row[3]+')'
    SelectionsToAdd=[]
    for sel in Selections:
        SelectionsToAdd.append('*('+sel+')')
    print SelectionsToAdd
    return SelectionsToAdd


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
    use_emu = True
    #ttscaler = 0.489171949638 #0.479080479194  #0.488708924407 #0.490929901239
    ttscaler =  0.435 #0.435481463283
    #znorm = 0.981327517888   #+/-0.00705124299541 
    #znorm = 0.9857
    #znorm = 0.96072
    #znorm = 1.0001
    #znorm = 0.99191431851
    #znorm = 1.0

    znorm = 0.981327517888
    #znorm = 1.0
    #Trigger = '*(CurrentDoubleElePass>0.5)'
    #Trigger_emu = '*(HLTMu40TriggerPass>0.5)'
    #Trigger_qcd = '*((SinglePhotonTriggerPass>0.5)*SinglePhotonTriggerPrescale)'
    #znorm=1.0
    #znorm=1

    #znorm=1.0
    if znorm==1.0:
        #Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.5)*(abs(Eta_HEEPele2)<2.5))*(M_HEEPele1ele2>80)*(M_HEEPele1ele2<100))*(ST_pf_ee_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        #Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.5)*(abs(Eta_muon1)<2.5))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 250)*((Charge_HEEPele1*Charge_muon1)==-1)'
        #Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.5)*(abs(Eta_QCDele2)<2.5))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>80)*(M_HEEPele1ele2<100))*(ST_pf_ee_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu_single> 250)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)*((Charge_HEEPele1*Charge_HEEPele2)==1)'
        #Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>125)*(Pt_pfjet2>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>80)*(M_HEEPele1ele2<100))*(ST_pf_ee> 300)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        #Selection_emu = '((Pt_HEEPele1>45)*(Pt_muon1>45)*(Pt_pfjet1>125)*(Pt_pfjet2>45)*(deltaR_HEEPele1muon1>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_muon1)<2.1))*(M_HEEPele1muon1>80)*(M_HEEPele1muon1<100))*(ST_pf_emu> 300)*((Charge_HEEPele1*Charge_HEEPele2)==-1)'
        #Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>125)*(Pt_pfjet2>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1+Pt_pfjet2)>300)*((Charge_HEEPele1*Charge_HEEPele2)==1)'
        use_emu=False

        drawSub=False
        #Selection +=Trigger
        #Selection_emu +=Trigger_emu
        #Selection_qcd += Trigger_qcd
    

        mbinning = [20,80,100]
        lq_choice = "*(LQmass==1000)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"
        filetag = "ZNormalization"
        #xtag = " ["+filetag+"]"
        xtag = ""
        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)

        mbinning = [100,50,1000]
        lq_choice = "*(LQmass==1000)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"
        filetag = "ZNormalizationFullRange"
        #xtag = " ["+filetag+"]"
        xtag = ""

        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)
        return

    if InputCuts:
        Selections = GetSelections(ifile)
        Selection = Selections[0]
        Selection_emu = Selections[1]
        Selection_qcd = Selections[2]
    else:
        Selection = '((Pt_HEEPele1>45)*(Pt_HEEPele2>45)*(Pt_pfjet1>45)*(deltaR_HEEPele1ele2>0.3)*((abs(Eta_HEEPele1)<2.1)*(abs(Eta_HEEPele2)<2.1))*(M_HEEPele1ele2>110))*(ST_pf_ee_single> 250)'

        Selection_emu = '((Pt_muon1>45)*(Pt_HEEPele1>45)*(Pt_pfjet1>45)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)*(abs(Eta_HEEPele1)<2.1))*(M_muon1HEEPele1>110))*(ST_pf_emu_single> 250)'

        Selection_qcd = '((Pt_QCDele1>45)*(Pt_QCDele2>45)*(Pt_pfjet1>45)*(deltaR_QCDele1ele2>0.3)*((abs(Eta_QCDele1)<2.1)*(abs(Eta_QCDele2)<2.1))*(M_QCDele1ele2>110))*((Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)>250)'

    
    if RescaleCuts:
        AdditionalSelections=GetRescaleSelections(rfile)
        Selection += AdditionalSelections[0]
        Selection_emu += AdditionalSelections[1]
        Selection_qcd += AdditionalSelections[2]


    #Selection +=Trigger
    #Selection_emu +=Trigger_emu
    #Selection_qcd += Trigger

    lq_choice = "*(LQmass==1000)*(LQisCMu==0)*(LQcoupling==0.4)*(1/1000)"
    #lq_choice = "*(LQmass==300)*(LQisCMu==0)*(LQcoupling==1.0)*(1/1000)"

    #lq_choice +=AddCuts

    ptbinning = [50,0,1000]
    etabinning = [48,-2.4,2.4]
    mbinning = [48,110,2030]
    mljbinning = [51,0,2080]
    stbinning = [46,250,2050]
    #stbinning = [40,0,1600]
    vertexbinning = [45,-0.5,44.5]
    deltarbinning = [50,0,5]
    deltaphibinning = [80,-4,4]
    isobinning = [100,0,10]
    relisobinning=[100,0,0.5]
    hcalisobinning=[100,0,5]
    jetcountbinning=[9,0,8]

    chargebinning=[11,-5,5]

    filetag = "Preselection"
    #xtag = " ["+filetag+"]"
    xtag=""

    print "About to start drawing the Histos..."
    print Selection

    if False:
        filetag = "Fullselection"
        #xtag = " ["+filetag+"]"
        xtag=""
        mbinning = [50,500,2500]
        stbinning = [50,500,2500]

        #mbinning = [49,110,2030]
        mljbinning = [26,0,2080]
        stbinning = [23,250,2090]

        #mljbinning = [25,500,2500]
        #stbinning = [25,500,2500]


        Selection +='*(ST_pf_ee_single > 800)*(M_singleLQ_epfjet_Masshigh > 900)'
        Selection_emu +='*(ST_pf_emu_single > 800)*(M_singleLQ_emusel_Masshigh > 900)'
        Selection_qcd += '*(ST_pf_ee_single > 800)*(M_singleLQ_epfjet_Masshigh > 900)'


        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mljbinning, "M_singleLQ_epfjet_Masshigh", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "M_{e j} (GeV)" +xtag, znorm, ttscaler,filetag)
        #return
        DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_ee_single", "ST_pf_emu_single","(Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)
        return



    ptllbinning=[12,90,1290]

    #DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, true, ptllbinning, "(Pt_HEEPele1+Pt_HEEPele2)", "(Pt_HEEPele1+Pt_HEEPele2)","", "p_{T}(ll) (GeV)" +xtag, znorm, ttscaler,filetag)
    #return

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1ele2", "M_muon1HEEPele1", "M_QCDele1ele2", "M_{ee}(GeV)  " +xtag  ,znorm, ttscaler,filetag)
    #return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "ST_pf_ee_single", "ST_pf_emu_single","(Pt_QCDele1+Pt_QCDele2+Pt_pfjet1)", "S_{T} (GeV)" +xtag, znorm, ttscaler,filetag)
    #return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mljbinning, "M_singleLQ_epfjet_Masshigh", "M_singleLQ_emusel_Masshigh","max(M_QCDele1pfjet1,M_QCDele2pfjet1)", "M_{e j} (GeV)" +xtag, znorm, ttscaler,filetag)




    return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, jetcountbinning, "PFJetCount", "PFJetCount", "PFJetCount", "PFJetCount" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_pfjet1","Pt_pfjet1", "Pt_pfjet1", "p_{T} (jet_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)

   



    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "Pt_HEEPele1", "max(Pt_HEEPele1,Pt_muon1)","Pt_QCDele1", "p_{T} (e_{1}) (GeV) " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd,use_emu , drawSub, ptbinning,  "Pt_HEEPele2", "min(Pt_HEEPele1,Pt_muon1)", "Pt_QCDele2","p_{T} (e_{2}) (GeV) " +xtag,znorm, ttscaler,filetag)
    return

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele1*Charge_HEEPele2", "Charge_HEEPele1*Charge_muon1","Charge_HEEPele1*Charge_HEEPele2", "Combined charge " +xtag, znorm, ttscaler,filetag)

    #return
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele1", "Charge_HEEPele1","Charge_HEEPele1", "Ele 1 charge " +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, chargebinning, "Charge_HEEPele2", "Charge_muon1","Charge_HEEPele2", "Ele 2 charge " +xtag, znorm, ttscaler,filetag)


    #return
   

    #return



    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, vertexbinning, "N_Vertices", "N_Vertices", "N_Vertices", "N_{Vertices}" +xtag, znorm, ttscaler,filetag)	



    





    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_HEEPele2", "Eta_muon1*(Pt_muon1<Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1<Pt_muon1)","Eta_QCDele2", "#eta (e_{2}) " +xtag,  znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_HEEPele1", "Eta_muon1*(Pt_muon1>Pt_HEEPele1)+Eta_HEEPele1*(Pt_HEEPele1>Pt_muon1)","Eta_QCDele1", "#eta (e_{1}) " +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, etabinning, "Eta_pfjet1", "Eta_pfjet1", "Eta_pfjet1","#eta (jet_{1}) " +xtag, znorm, ttscaler,filetag)

    #return

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltarbinning, "deltaR_HEEPele1ele2", "deltaR_HEEPele1ele2", "deltaR_HEEPele1ele2", "#Delta R_{e1 e2}" +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltarbinning, "deltaR_HEEPele1pfjet1", "deltaR_HEEPele1pfjet1", "deltaR_HEEPele1pfjet1", "#Delta R_{e1 jet}" +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltarbinning, "deltaR_HEEPele2pfjet1", "deltaR_HEEPele2pfjet1", "deltaR_HEEPele2pfjet1", "#Delta R_{e2 jet}" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltaphibinning, "deltaPhi_HEEPele1ele2", "deltaPhi_HEEPele1ele2", "deltaPhi_HEEPele1ele2", "#Delta #phi_{e1 e2}" +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltaphibinning, "deltaPhi_HEEPele1pfjet1", "deltaPhi_HEEPele1pfjet1", "deltaPhi_HEEPele1pfjet1", "#Delta #phi_{e1 jet}" +xtag, znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, deltaphibinning, "deltaPhi_HEEPele2pfjet1", "deltaPhi_HEEPele2pfjet1", "deltaPhi_HEEPele2pfjet1", "#Delta #phi_{e2 jet}" +xtag, znorm, ttscaler,filetag)


    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, mbinning, "M_HEEPele1pfjet1", "M_HEEPele1pfjet1", "M_QCDele1pfjet1","M_{e jet} " +xtag,znorm, ttscaler,filetag)
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "TrkIso_HEEPele2", "TrkIso_HEEPele2", "TrkIso_HEEPele2", "Track Iso e2" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, relisobinning, "RelIso_HEEPele2", "RelIso_HEEPele2", "RelIso_HEEPele2", "Rel Iso e2" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, hcalisobinning, "HcalIsoD1_HEEPele2", "HcalIsoD1_HEEPele2", "HcalIsoD1_HEEPele2", "Hcal IsoD1 e2" +xtag, znorm, ttscaler,filetag)	
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, hcalisobinning, "HcalIsoD2_HEEPele2", "HcalIsoD2_HEEPele2", "HcalIsoD1_HEEPele2", "Hcal IsoD2 e2" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "EcalIsoPAT_HEEPele2", "EcalIsoPAT_HEEPele2", "EcalIsoPAT_HEEPele2", "Ecal IsoPAT e2" +xtag, znorm, ttscaler,filetag)	
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "EcalIsoDR03_HEEPele2", "EcalIsoDR03_HEEPele2", "EcalIsoD1_HEEPele2", "EcalIsoDR03 e2" +xtag, znorm, ttscaler,filetag)



    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "TrkIso_HEEPele1", "TrkIso_HEEPele1", "TrkIso_HEEPele1", "Track Iso e1" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, relisobinning, "RelIso_HEEPele1", "RelIso_HEEPele1", "RelIso_HEEPele1", "Rel Iso e1" +xtag, znorm, ttscaler,filetag)	

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, hcalisobinning, "HcalIsoD1_HEEPele1", "HcalIsoD1_HEEPele1", "HcalIsoD1_HEEPele1", "Hcal IsoD1 e1" +xtag, znorm, ttscaler,filetag)	
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, hcalisobinning, "HcalIsoD2_HEEPele1", "HcalIsoD2_HEEPele1", "HcalIsoD1_HEEPele1", "HcalIsoD2 e1" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "EcalIsoPAT_HEEPele1", "EcalIsoPAT_HEEPele1", "EcalIsoPAT_HEEPele1", "Ecal IsoPAT e1" +xtag, znorm, ttscaler,filetag)	
    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, isobinning, "EcalIsoDR03_HEEPele1", "EcalIsoDR03_HEEPele1", "EcalIsoD1_HEEPele1", "EcalIsoDR03 e1" +xtag, znorm, ttscaler,filetag)

	




    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, ptbinning, "MET_pf", "MET_pf", "MET_pf", "MET_pf" +xtag, znorm, ttscaler,filetag)

    DrawHisto(JustIntegrate,lq_choice, Selection, Selection_emu, Selection_qcd, use_emu, drawSub, stbinning, "(Pt_HEEPele1+Pt_HEEPele2)", "(Pt_HEEPele1+Pt_muon1", "Pt_HEEPele1+Pt_HEEPele2", "Pt_HEEPele1+Pt_HEEPele2" +xtag, znorm, ttscaler,filetag)
   

def main():
    if PlotHistos:
        plot()
    if IntegrateOnly:
        integrate()
    if PreselIntegrateOnly:
        integrate()
    if FiducialIntegrateOnly:
        fidintegrate()

main()
