import os
import sys
import math
import numpy


#File = os.popen('cat CMU_Template_2012.cfg').readlines()
#File = os.popen('cat CMU_Template.cfg').readlines()
File = os.popen('cat CMU_Template_Rescaled.cfg').readlines()


InputAccErrors=os.popen('cat ElectronAccErrors0p66.txt').readlines()
print InputAccErrors
#InputFile = "Ele2012Numbers.txt"
#InputFile = "Ele2012FixedNumbersTest.csv"
#InputFile = "Ele2012Numbers_SmoothSB.txt"
#InputFile = "ElectronPreselectionNumbers.txt"
#InputFile = "EleOut2.txt"
#InputFile = "ElectronLowerDileptonCut.txt"
#InputFile = "StandardEleOutput.txt"
#InputFile = "TempStoreage.txt"
#InputFile = "~/CMSSW_5_0_0/src/NTupleAnalyzer/ParallelCounter/TotalOutput.txt"
#InputFile = 'RedoElePU.txt'
#InputFile = 'Feb19Redo.txt'
#InputFile = 'EleNumbers_July16.txt'
#InputFile = 'EleNumbers_Fiducial_July31.txt'
#InputFile = 'EleNumbers_Fiducial_Aug6.txt'
#InputFile = 'ElectronNumbers_Aug7.txt'
#InputFile = 'FiducialLog.txt'
#InputFile = '125GeVCut_Electrons.txt'
#InputFile = 'ForFiducialCuts.txt'
#InputFile='FiducialLog_Again.txt'
#InputFile='125GeVCut_Electrons_Fiducial.csv'

#InputFile = 'Electrons_Sep8.txt'
#InputFile = 'Electrons_Sep8_CorrPU.txt'
#InputFile = 'FiducialElectrons_Sep10.csv'
#InputFile = 'FiducialElectrons_Sep18.csv'

#InputFile = 'ElectronNumbers_125GeVJetCut_Aug12.txt'

#InputFile='125GeVCut2.txt'


#InputFile='Electrons_Sep22Just1p0Sel.txt'
#InputFile = 'Electrons_Sep30.txt'
#InputFile='TestEleNorm2.txt'


#InputFile='ElectronsFinal1p0Sel.txt'
#InputFile='ElectronsFiducialFinal1p0Sel.csv'

#InputFile='ElectronsFiducial0p66.csv'
#InputFile='ElectronsFiducial0p66_FixedEleSysts.csv'
InputFile='ElectronsFiducial0p66_FixedEleSysts_Rescaled.csv'
#InputFile='ElectronsFiducial0p75.csv'

#InputFile='FiducialElectrons_Sep23.csv'
#InputFile='FiducialElectrons_Sep25.csv'




#EntriesFile='CentralValuesForEntries_Entries.txt'

#EntriesFile='CentralValues_Electrons_Entries.txt'
#EntriesFile='CentralValues_FiducialElectrons_Entries.csv'
#EntriesFile='CentralValues_Electrons_Entries_Sep18.txt'

#EntriesFile = 'CentralValues_Electrons_Entries_Sep22Just1p0Sel.txt'
#EntriesFile='CentralValues_Electrons_Entries_Sep30.txt'
#EntriesFile='TestEleNorm2_Entries.txt'
#EntriesFile='ElectronsFinal1p0Sel_Entries.txt'
#EntriesFile='ElectronsFiducialFinal1p0Sel_Entries.csv'

EntriesFile='ElectronsFiducial0p66_Entries.csv'
#EntriesFile='ElectronsFiducial0p75_Entries.csv'

#EntriesFile='CentralValues_Electrons_FiducialSep23_Entries.csv'
#EntriesFile='CentralValues_Electrons_FiducialSep25_Entries.csv'

#InputFile = '125GeVCut.txt'


RescaleErrorsFile = 'CentralValues_Electrons_RescaleError.txt'

#InputFile = 'ElectronNumbers_Fiducial_Aug12.txt'
#InputFile = 'EleCheckNewZRescale.txt'

Sigs=open('Significances_ee.txt','w')

#Rates = open('#Rates_2012_ele.tex','w') 
#Rates.write("\\begin{frame}\n")
#Rates.write("\\tiny\n")
#Rates.write("\\begin{tabular}{|c|c|c|c|c|c|c|}\n")
#Rates.write("\\hline\n")
#Rates.write("\\textbf{$M_{LQ}$} & \\textbf{$Signal$} & \\textbf{$Data$} & \\textbf{$Total Background$} & \\textbf{$Z-Jets$} & \\textbf{$ttbar$} & \\textbf{$VV + W-Jets + single top + QCD$}\\\\\n")
#Rates.write("\\hline\n")


Rates = open('Rates_2012_ele.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{$M_{LQ}$} & \\textbf{$Data$} & \\textbf{$Total Background$} & \\textbf{$Z-Jets$} & \\textbf{$ttbar$} & \\textbf{$VV + W-Jets + single top + QCD$}\\\\\n")
Rates.write("\\hline\n")


SignalRates = open('SignalRates_2012_ele.csv','w') 
#SignalRates.write("\\begin{frame}\n")
#SignalRates.write("\\tiny\n")
#SignalRates.write("\\begin{tabular}{|c|c|c|c|c|c|c|}\n")
#SignalRates.write("\\hline\n")
#SignalRates.write("\\textbf{$M_{LQ}$} & \\textbf{$\lambda=0.4$} & \\textbf{$\lambda=0.6$} & \\textbf{$\lambda=0.8$} & \\textbf{$\lambda=1.0$} & \\\\\n")
#SignalRates.write("\\hline\n")




#========== Defining global variables here============#
#300 GeV stuff
JetScaleImpact_sig300= -1
JetScaleImpact_MC300= -1
JetSmearImpact_sig300= -1
JetSmearImpact_MC300= -1
MuScaleImpact_sig300= -1
MuScaleImpact_MC300= -1
MuSmearImpact_sig300= -1
MuSmearImpact_MC300= -1
#misc errors
#trigerr=1.027
trigerr=1.0
recoerr=1.012
lumierr=1.026
#Z normalization error here
znormerr = 0.006
#ttbar ratio error here
ttratioerr = 0.005
#qcd normalization error here
qcdratioerr = 0.004

#Defining a list of average weights at preselection:
# [ttbar,Z+Jets,DiBoson,SingleTop,W+Jets,QCD]
AvgW=[.272,.146,.0488,.440,.631,.089]

#Various statistics
Data = -1
MC=-1
tt=-1
tterror=-1
z=-1
zerror=-1
zrescale=-1
diboson=-1
dibosonerror=-1
singtop=-1
singtoperror=-1
wjets=-1
wjetserror=-1

sigratio=-1
sigentries=-1
dibosonratio=-1
dibosonentries=-1
singtopratio=-1
singtopentries=-1
wjetsratio=-1
wjetsentries=-1
zjetsratio=-1
zjetsentries=-1
ttbarratio=-1
ttbarentries=-1
qcdratio=-1
qcdentries=-1

gjets=-1
gjetserror=-1
qcd=-1
qcderror=-1
sig=-1
sigerror=-1
MC_MuScaleDown=-1
MC_MuScaleUp=-1
MC_JetScaleDown=-1
MC_JetScaleUp=-1
MC_JetSmear=-1
MC_MuSmear=-1
MC_PUup=-1
MC_PUdown=-1
MC_ZMatchDown=-1
MC_ZScaleUp=-1
MC_ZScaleDown=-1
MC_ZMatchUp=-1
sig_MuScaleDown=-1
sig_MuScaleUp=-1
sig_JetScaleDown=-1
sig_JetScaleUp=-1
sig_JetSmear=-1
sig_MuSmear=-1
sig_PUup=-1
sig_PUdown=-1

MuScaleUpError_MC=-1
MuScaleDownError_MC=-1
JetScaleUpError_MC=-1
JetScaleDownError_MC=-1
MuSmearError_MC=-1
JetSmearError_MC=-1
PUupError_MC=-1
PUdownError_MC=-1
ZMatchDownError_MC=-1
ZScaleUpError_MC=-1
ZScaleDownError_MC=-1
ZMatchUpError_MC=-1
ZMatchDownError_Z=-1
ZScaleUpError_Z=-1
ZScaleDownError_Z=-1
ZMatchUpError_Z=-1


MuScaleUpError_sig=-1
MuScaleDownError_sig=-1
JetScaleUpError_sig=-1
JetScaleDownError_sig=-1
MuSmearError_sig=-1
JetSmearError_sig=-1
PUupError_sig=-1
PUdownError_sig=-1

JetScaleImpact_sig= -1
JetScaleImpact_MC= -1
JetSmearImpact_sig= -1
JetSmearImpact_MC= -1
MuScaleImpact_sig= -1
MuScaleImpact_MC= -1
MuSmearImpact_sig= -1
MuSmearImpact_MC= -1
LumiImpact_sig= -1
LumiImpact_MC= -1
PUImpact_sig= -1
PUImpact_MC= -1
ZMatchImpact_MC= -1
ZScaleImpact_MC= -1
ZShapeImpact_MC= -1
IDImpact_sig= -1
IDImpact_MC= -1
TriggerImpact_sig= -1
TriggerImpact_MC= -1
QCDNormImpact_MC= -1
TTNormImpact_MC= -1
ZNormImpact_MC= -1
ZNNPDFImpact= -1
SigNNPDFImpact= -1
TotalUncertainty_MC =-1
TotalUncertainty_Sig=-1
ZRescaleImpact_MC=-1


LumiImpact_sig300= -1
LumiImpact_MC300= -1
PUImpact_sig300= -1
PUImpact_MC300= -1
IDImpact_sig300= -1
IDImpact_MC300= -1
TriggerImpact_sig300= -1
TriggerImpact_MC300= -1

QCDNormImpact=-1
TTNormImpact=-1
ZNormImpact=-1

Z_NNPDFdown=-1
Z_NNPDFup=-1

sig_NNPDFdown=-1
sig_NNPDFup=-1

W_NNPDFdown=-1
W_NNPDFup=-1

DiBoson_NNPDFdown=-1
DiBoson_NNPDFup=-1

SingleTop_NNPDFdown=-1
SingleTop_NNPDFup=-1

#Z_CTEQdown=-1
#Z_CTEQup=-1
#Z_MSTWdown=-1
#Z_MSTWup=-1

sigcouplingacc=1.0
previouscoupling=1.0

NNPDFdown_Z=-1
NNPDFup_Z=-1


NNPDFdown_sig=-1
NNPDFup_sig=-1

NNPDFdown_W=-1
NNPDFup_W=-1

NNPDFdown_SingleTop=-1
NNPDFup_SingleTop=-1

NNPDFdown_DiBoson=-1
NNPDFup_DiBoson=-1

#CTEQdown_Z=-1
#CTEQup_Z=-1
#MSTWdown_Z=-1
#MSTWup_Z=-1

localTotalSystError_MC300 =-1
localTotalSystError_Sig300 =-1
localTotalStatError_MC300=-1
localTotalStatError_Sig300=-1

localTotalSystError_MC =-1
localTotalSystError_Sig =-1


BGleftover = -1
Z=-1
TT=-1
QCD=-1

#Iterators
x=-1
i=-1
coupling="blah"

def SetValues(y):
    global Data
    global MC
    global tt
    global tterror
    global z
    global zerror
    global zrescale
    global sig
    global sigerror
    global diboson
    global dibosonerror
    global singtop
    global singtoperror
    global wjets
    global wjetserror

    global sigratio
    global sigentries
    global dibosonratio
    global dibosonentries
    global singtopratio
    global singtopentries
    global wjetsratio
    global wjetsentries
    global zjetsratio
    global zjetsentries
    global ttbarratio
    global ttbarentries
    global qcdratio
    global qcdentries


    #global gjets
    #global gjetserror
    global qcd
    global qcderror
    global MC_MuScaleDown
    global MC_MuScaleUp
    global MC_JetScaleDown
    global MC_JetScaleUp
    global MC_JetSmear
    global MC_MuSmear
    global MC_PUup
    global MC_PUdown
    global MC_ZMatchDown
    global MC_ZScaleUp
    global MC_ZScaleDown
    global MC_ZMatchUp
    global sig_MuScaleDown
    global sig_MuScaleUp
    global sig_JetScaleDown
    global sig_JetScaleUp
    global sig_JetSmear
    global sig_MuSmear
    global sig_PUup
    global sig_PUdown

    global MuScaleUpError_MC
    global MuScaleDownError_MC
    global JetScaleUpError_MC
    global JetScaleDownError_MC
    global MuSmearError_MC
    global JetSmearError_MC
    global PUupError_MC
    global PUdownError_MC

    global ZMatchDownError_MC
    global ZScaleUpError_MC
    global ZScaleDownError_MC
    global ZMatchUpError_MC

    global ZMatchDownError_Z
    global ZScaleUpError_Z
    global ZScaleDownError_Z
    global ZMatchUpError_Z

    global ZMatchDownError_Z
    global ZScaleUpError_Z
    global ZScaleDownError_Z
    global ZMatchUpError_Z

    
    global MuScaleUpError_sig
    global MuScaleDownError_sig
    global JetScaleUpError_sig
    global JetScaleDownError_sig
    global MuSmearError_sig
    global JetSmearError_sig
    global PUupError_sig
    global PUdownError_sig

    global BGleftover
    global TT
    global Z
    global QCD

    global Z_NNPDFdown
    global Z_NNPDFup

    global sig_NNPDFdown
    global sig_NNPDFup

    global W_NNPDFdown
    global W_NNPDFup

    global DiBoson_NNPDFdown
    global DiBoson_NNPDFup

    global SingleTop_NNPDFdown
    global SingleTop_NNPDFup

    #global Z_CTEQdown
    #global Z_CTEQup
    #global Z_MSTWdown
    #global Z_MSTWup

    global NNPDFdown_Z
    global NNPDFup_Z
    global NNPDFdown_sig
    global NNPDFup_sig

    global NNPDFdown_W
    global NNPDFup_W

    global NNPDFdown_SingleTop
    global NNPDFup_SingleTop

    global NNPDFdown_DiBoson
    global NNPDFup_DiBoson

    global sigcouplingacc
    global previouscoupling

    #global CTEQdown_Z
    #global CTEQup_Z
    #global MSTWdown_Z
    #global MSTWup_Z

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $1}'"
    #print String
    print x
    Data=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    tt=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $2}'"
    tterror=float(os.popen(String).readline().replace('\n',''))
    if tt > 0:
        tterror = (tterror / tt) + 1
    else:
        tt=0
        tterror = 1.51*AvgW[0] + 1
    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $2}' " +EntriesFile
    ttbarentries=float(os.popen(String).readline().replace('\n',''))
    if ttbarentries !=0:
        ttbarratio=tt/ttbarentries
    else:
        ttbarratio=tt
        ttbarentries=1.0
    #print "tterror = " + str(tterror)

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $3}'"
    zerror=float(os.popen(String).readline().replace('\n',''))
    if z > 0:
        zerror = (zerror / z) + 1
    else:
        print "---------> REPLACING Z <--------------"
        z=0
        zerror = 1.51*AvgW[1] + 1
        print zerror

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $3}' " +EntriesFile
    zjetsentries=float(os.popen(String).readline().replace('\n',''))
    if zjetsentries !=0:
        zjetsratio=z/zjetsentries
    else:
        zjetsratio=z
        zjetsentries=1.0

    String="cat " +RescaleErrorsFile+" | gawk '(NR=="+str(y-1)+")'"
    zrescale=float(os.popen(String).readline().replace('\n',''))
    if z!=0:
        zrescale=1+zrescale/z
    else:
        zrescale=1.0


    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    diboson=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $4}'"
    dibosonerror=float(os.popen(String).readline().replace('\n',''))
    if diboson > 0:
        dibosonerror = (dibosonerror / diboson) + 1
    else:
        diboson=0
        dibosonerrorerror = 1.51*AvgW[2] + 1

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $4}' " +EntriesFile
    print String
    dibosonentries=float(os.popen(String).readline().replace('\n',''))
    if dibosonentries !=0:
        dibosonratio=diboson/dibosonentries
    else:
        dibosonratio=diboson
        dibosonentries=1.0

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    singtop=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $5}'"
    singtoperror=float(os.popen(String).readline().replace('\n',''))
    if singtop > 0:
        singtoperror = (singtoperror / singtop) + 1
    else:
        singtop=0
        singtoperror = 1.51*AvgW[3] + 1

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $5}' " +EntriesFile
    singtopentries=float(os.popen(String).readline().replace('\n',''))
    if singtopentries !=0:
        singtopratio=singtop/singtopentries
    else:
        singtopratio=singtop
        singtopentries=1.0

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $6}'"
    wjets=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $6}'"
    wjetserror=float(os.popen(String).readline().replace('\n',''))
    if wjets > 0:
        wjetserror = (wjetserror / wjets) + 1
    else:
        wjets=0
        wjetserror = 1.51*AvgW[4] + 1

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $6}' " +EntriesFile
    wjetsentries=float(os.popen(String).readline().replace('\n',''))
    if wjetsentries !=0:
        wjetsratio=wjets/wjetsentries
    else:
        wjetsratio=wjets
        wjetsentries=1.0



    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $8}'"
    qcd=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $8}'"
    qcderror=float(os.popen(String).readline().replace('\n',''))
    if qcd > 0:
        qcderror = (qcderror / qcd) + 1
    else:
        qcd=0
        qcderror = 1.51*AvgW[5] + 1

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $8}' " +EntriesFile
    qcdentries=float(os.popen(String).readline().replace('\n',''))
    if qcdentries !=0:
        qcdratio=qcd/qcdentries
    else:
        qcdratio=qcd
        qcdentries=1.0

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $7}'"
    gjets=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $7}'"
    gjetserror=float(os.popen(String).readline().replace('\n',''))
    if gjets != 0:
        gjetserror = (gjetserror / gjets) + 1


    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $9}'"
    sigerror=float(os.popen(String).readline().replace('\n',''))
    if sig != 0:
        sigerror = (sigerror / sig) + 1

    String=" gawk -F ','  '(NR==" + str(y-1) +") {print $9}' " +EntriesFile
    sigentries=float(os.popen(String).readline().replace('\n',''))
    if sigentries !=0:
        sigratio=sig/sigentries
    else:
        sigratio=sig
        sigentries=1.0

    MC = qcd+gjets+wjets+singtop+diboson+z+tt

    MC_MuScaleDown=GetTotalMC("MuScaleDown",y)

    MC_MuScaleUp=GetTotalMC("MuScaleUp",y)

    MC_JetScaleDown=GetTotalMC("JetScaleDown",y)

    MC_JetScaleUp=GetTotalMC("JetScaleUp",y)

    MC_JetSmear=GetTotalMC("JetSmear",y)

    MC_MuSmear=GetTotalMC("MuSmear",y)

    MC_PUup=GetTotalMC("PU_up",y)

    MC_PUdown=GetTotalMC("PU_down",y)

    #MC_ZMatchDown=GetTotalMC("ZMatchDown",y)
    #MC_ZMatchUp=GetTotalMC("ZMatchUp",y)

    #MC_ZScaleUp=GetTotalMC("ZScaleUp",y)
    #MC_ZScaleDown=GetTotalMC("ZScaleDown",y)
    
    String = "grep -A 226 ZScaleUp " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    MC_ZScaleUp=float(os.popen(String).readline().replace('\n',''))


    String = "grep -A 226 ZScaleDown " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    MC_ZScaleDown=float(os.popen(String).readline().replace('\n',''))
    print "MC_ZScaleUp/MC_ZScaleDown = " +str(MC_ZScaleUp)+"/"+str(MC_ZScaleDown)
    if (MC_ZScaleUp+MC_ZScaleDown ==0):
        TotalZScaleUncertainty = 0.01
    else:
        TotalZScaleUncertainty = math.fabs(MC_ZScaleUp-MC_ZScaleDown)/(MC_ZScaleUp+MC_ZScaleDown)
    print "TotalZScaleUncertainty = " + str(TotalZScaleUncertainty)
    

    ########
    String = "grep -A 226 MuScaleDown " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_MuScaleDown=float(os.popen(String).readline().replace('\n',''))
 
    String = "grep -A 226 MuScaleUp " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_MuScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 JetScaleDown " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 JetScaleUp " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 JetSmear " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_JetSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 MuSmear " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_MuSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 PU_up " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_PUup=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 PU_down " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig_PUdown=float(os.popen(String).readline().replace('\n',''))

    MuScaleUpError_MC = 1+  (abs(MC_MuScaleUp - MC) / MC)
    MuScaleDownError_MC = 1+  (abs(MC_MuScaleDown - MC) / MC)
    JetScaleUpError_MC = 1+  (abs(MC_JetScaleUp - MC) / MC)
    JetScaleDownError_MC = 1+  (abs(MC_JetScaleDown - MC) / MC)
    MuSmearError_MC =   1+ (abs(MC_MuSmear-MC) / MC)
    JetSmearError_MC =   1+ ((abs(MC_JetSmear-MC)) / MC)
    PUupError_MC = 1+  (abs(MC_PUup - MC) / MC)
    PUdownError_MC = 1+  (abs(MC_PUdown - MC) / MC)


    ZMatchDownError_MC = .08 * (z/MC) + 1
    ZMatchUpError_MC =.09 * (z/MC)+1

    ZScaleUpError_MC = (z/MC)*TotalZScaleUncertainty+1
    ZScaleDownError_MC = (z/MC)*TotalZScaleUncertainty+1
    print "z = " +str(z)
    print "MC = "+str(MC)
    print "ZScale = " +str(ZScaleUpError_MC)

    ZMatchDownError_Z = 1.08
    ZScaleUpError_Z =  TotalZScaleUncertainty+1
    ZScaleDownError_Z =  TotalZScaleUncertainty+1
    ZMatchUpError_Z =  1.09



    MuScaleUpError_sig = 1+  (abs(sig_MuScaleUp - sig) / sig)
    MuScaleDownError_sig = 1+  (abs(sig_MuScaleDown - sig) / sig)
    JetScaleUpError_sig = 1+  (abs(sig_JetScaleUp - sig) / sig)
    JetScaleDownError_sig = 1+  (abs(sig_JetScaleDown - sig) / sig)
    MuSmearError_sig =   1+ (abs(sig_MuSmear-sig) / sig)
    JetSmearError_sig =   1+ ((abs(sig_JetSmear-sig)) / sig)
    PUupError_sig = 1+  (abs(sig_PUup - sig) / sig)
    PUdownError_sig = 1+  (abs(sig_PUdown - sig) / sig)

    Z_pdfs=GetPDFError('Ele_PDF_Z.txt',y)
    Z_NNPDFdown = Z_pdfs[0]
    Z_NNPDFup = Z_pdfs[1]

    NNPDFdown_Z = Z_pdfs[0]+1
    NNPDFup_Z = Z_pdfs[1]+1

    W_pdfs=GetPDFError('Ele_PDF_W.txt',y)
    W_NNPDFdown = W_pdfs[0]
    W_NNPDFup = W_pdfs[1]

    NNPDFdown_W = W_pdfs[0]+1
    NNPDFup_W = W_pdfs[1]+1

    SingleTop_pdfs=GetPDFError('Ele_PDF_SingleTop.txt',y)
    SingleTop_NNPDFdown = SingleTop_pdfs[0]
    SingleTop_NNPDFup = SingleTop_pdfs[1]

    NNPDFdown_SingleTop = SingleTop_pdfs[0]+1
    NNPDFup_SingleTop = SingleTop_pdfs[1]+1

    DiBoson_pdfs=GetPDFError('Ele_PDF_DiBoson.txt',y)
    DiBoson_NNPDFdown = DiBoson_pdfs[0]
    DiBoson_NNPDFup = DiBoson_pdfs[1]

    NNPDFdown_DiBoson = DiBoson_pdfs[0]+1
    NNPDFup_DiBoson = DiBoson_pdfs[1]+1


    sig_pdfs=GetPDFError('Ele_SignalAcceptance_PDF.txt',y)

    sig_NNPDFdown = sig_pdfs[0]
    sig_NNPDFup = sig_pdfs[1]


    NNPDFdown_sig = sig_pdfs[0]+1
    NNPDFup_sig = sig_pdfs[1]+1





    #Z_CTEQdown = Z_pdfs[2]
    #Z_CTEQup = Z_pdfs[3]
    #Z_MSTWdown = Z_pdfs[4]
    #Z_MSTWup = Z_pdfs[5]
    #CTEQdown_Z = Z_pdfs[2]+1
    #CTEQup_Z = Z_pdfs[3]+1
    #MSTWdown_Z = Z_pdfs[4]+1
    #MSTWup_Z = Z_pdfs[5]+1

    BGleftover = MC - tt- z
    Z = z
    TT = tt
    QCD = qcd

    if coupling == "1p0":
        #sigcouplingacc
        print i
        thiscoupling=InputAccErrors[i-1].replace('\n','')
        if float(thiscoupling)!=1.0:
            previouscoupling=thiscoupling
            sigcouplingacc=1.0+float(thiscoupling)
        else:
            sigcouplingacc=1.0+float(previouscoupling)
        print "My coupling is"+str(thiscoupling)
            



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

    
def GetTotalMC(UncertaintyType,y):
    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    TotalMC=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $6}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))
    
    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $7}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 "+UncertaintyType+" " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $8}'"
    TotalMC+=float(os.popen(String).readline().replace('\n',''))

    return TotalMC
    

def SetIterators(y):
    global x
    global i
    global coupling

    if (y-2) < 16:
        x = 100 + y*100
        coupling = "0p2"
    if (y-2) >= 16:
        x = 100 + (y-16)*100
        coupling = "0p4"
    if (y-2) >= 32:
        x = 100 + (y-32)*100
        coupling = "0p6"
    if (y-2) >= 57:
        x = 100 + (y-57)*100
        coupling = "0p8"
    if (y-2) >= 82:
        x = 100 + (y-82)*100
        coupling = "1p0"
        print "setting coupling to " +coupling
        i = (y-82)-1

def MakeConfigFile():
    
    
    NewFile = []
    output = open(str(x)+'_'+coupling+'_2012temp.cfg','w') 
    for Z in range(len(File)): 
        NewFile.append(File[Z])
    for Z in range(len(File)): 

        NewFile[Z] = NewFile[Z].replace('sigcouplingacc',str(sigcouplingacc))

        NewFile[Z] = NewFile[Z].replace('NNPDFdown_Z',str(NNPDFdown_Z))
        NewFile[Z] = NewFile[Z].replace('NNPDFup_Z',str(NNPDFup_Z))

        NewFile[Z] = NewFile[Z].replace('NNPDFdown_sig',str(NNPDFdown_sig))
        NewFile[Z] = NewFile[Z].replace('NNPDFup_sig',str(NNPDFup_sig))

        NewFile[Z] = NewFile[Z].replace('NNPDFdown_W',str(NNPDFdown_W))
        NewFile[Z] = NewFile[Z].replace('NNPDFup_W',str(NNPDFup_W))

        NewFile[Z] = NewFile[Z].replace('NNPDFdown_SingleTop',str(NNPDFdown_SingleTop))
        NewFile[Z] = NewFile[Z].replace('NNPDFup_SingleTop',str(NNPDFup_SingleTop))

        NewFile[Z] = NewFile[Z].replace('NNPDFdown_DiBoson',str(NNPDFdown_DiBoson))
        NewFile[Z] = NewFile[Z].replace('NNPDFup_DiBoson',str(NNPDFup_DiBoson))


        NewFile[Z] = NewFile[Z].replace('znormerr',str(1+znormerr))
        NewFile[Z] = NewFile[Z].replace('ttratioerr',str(1+ttratioerr))
        NewFile[Z] = NewFile[Z].replace('qcdratioerr',str(1 +qcdratioerr))

        NewFile[Z] = NewFile[Z].replace('zrescale',str(zrescale))


        NewFile[Z] = NewFile[Z].replace('sigentries',str(int(sigentries)))
        NewFile[Z] = NewFile[Z].replace('dibosonentries',str(int(dibosonentries)))
        NewFile[Z] = NewFile[Z].replace('singtopentries',str(int(singtopentries)))
        NewFile[Z] = NewFile[Z].replace('wjetsentries',str(int(wjetsentries)))
        NewFile[Z] = NewFile[Z].replace('zjetsentries',str(int(zjetsentries)))
        NewFile[Z] = NewFile[Z].replace('ttbarentries',str(int(ttbarentries)))
        NewFile[Z] = NewFile[Z].replace('qcdentries',str(int(qcdentries)))

        NewFile[Z] = NewFile[Z].replace('sigratio',str(sigratio))
        NewFile[Z] = NewFile[Z].replace('dibosonratio',str(dibosonratio))
        NewFile[Z] = NewFile[Z].replace('singtopratio',str(singtopratio))
        NewFile[Z] = NewFile[Z].replace('wjetsratio',str(wjetsratio))
        NewFile[Z] = NewFile[Z].replace('zjetsratio',str(zjetsratio))
        NewFile[Z] = NewFile[Z].replace('ttbarratio',str(ttbarratio))
        NewFile[Z] = NewFile[Z].replace('qcdratio',str(qcdratio))


        NewFile[Z] = NewFile[Z].replace('signalerror',str(sigerror))
        NewFile[Z] = NewFile[Z].replace('signalerror',str(sigerror))
        NewFile[Z] = NewFile[Z].replace('zerror',str(zerror))
        NewFile[Z] = NewFile[Z].replace('tterror',str(tterror))
        NewFile[Z] = NewFile[Z].replace('Data',str(Data))
        NewFile[Z] = NewFile[Z].replace('signal',str(sig))
        NewFile[Z] = NewFile[Z].replace('z',str(z))
        NewFile[Z] = NewFile[Z].replace('tt',str(tt))


        NewFile[Z] = NewFile[Z].replace('diboson',str(diboson))
        NewFile[Z] = NewFile[Z].replace('singtop',str(singtop))
        NewFile[Z] = NewFile[Z].replace('wjets',str(wjets))
        NewFile[Z] = NewFile[Z].replace('qcd',str(qcd))

        #NewFile[Z] = NewFile[Z].replace('BGleftover',str(BGleftover))
        NewFile[Z] = NewFile[Z].replace('recoerr',str(recoerr))
        NewFile[Z] = NewFile[Z].replace('trigerr',str(trigerr))
        NewFile[Z] = NewFile[Z].replace('lumierr',str(lumierr))

        NewFile[Z] = NewFile[Z].replace('PUupError_sig',str(PUupError_sig))
        NewFile[Z] = NewFile[Z].replace('PUupError_MC',str(PUupError_MC))
        NewFile[Z] = NewFile[Z].replace('PUdownError_MC',str(PUdownError_MC))
        
        #ZMatchUpHolder = 1.05
        #ZMatchDownHolder = 1.05
        #ZScaleUpHolder = 1.05
        #ZScaleDownHolder = 1.05
        NewFile[Z] = NewFile[Z].replace('ZMatchDownError_Z',str(ZMatchDownError_Z))
        NewFile[Z] = NewFile[Z].replace('ZMatchUpError_Z',str(ZMatchUpError_Z))
        NewFile[Z] = NewFile[Z].replace('ZScaleDownError_Z',str(ZScaleDownError_Z))
        NewFile[Z] = NewFile[Z].replace('ZScaleUpError_Z',str(ZScaleUpError_Z))

        NewFile[Z] = NewFile[Z].replace('PUdownError_sig',str(PUdownError_sig))
        NewFile[Z] = NewFile[Z].replace('MuScaleUpError_MC',str(MuScaleUpError_MC))
        NewFile[Z] = NewFile[Z].replace('MuScaleDownError_MC',str(MuScaleDownError_MC))
        NewFile[Z] = NewFile[Z].replace('JetScaleUpError_MC',str(JetScaleUpError_MC))
        NewFile[Z] = NewFile[Z].replace('JetScaleDownError_MC',str(JetScaleDownError_MC))
        NewFile[Z] = NewFile[Z].replace('JetSmearError_MC',str(JetSmearError_MC))
        NewFile[Z] = NewFile[Z].replace('MuSmearError_MC',str(MuSmearError_MC))
        NewFile[Z] = NewFile[Z].replace('MuScaleUpError_sig',str(MuScaleUpError_sig))
        NewFile[Z] = NewFile[Z].replace('MuScaleDownError_sig',str(MuScaleDownError_sig))
        NewFile[Z] = NewFile[Z].replace('JetScaleUpError_sig',str(JetScaleUpError_sig))
        NewFile[Z] = NewFile[Z].replace('JetScaleDownError_sig',str(JetScaleDownError_sig))
        NewFile[Z] = NewFile[Z].replace('JetSmearError_sig',str(JetSmearError_sig))
        NewFile[Z] = NewFile[Z].replace('MuSmearError_sig',str(MuSmearError_sig))


        output.write(NewFile[Z])
    output.close()

def SaveValuesForCards():
    #print "MC = " +str(MC)
    #print "MC scaleup = " +str(MC_JetScaleUp)
    #print "MC scaledown = " +str(MC_JetScaleDown)
    global MuScaleImpact_sig
    global JetScaleImpact_sig
    global MuSmearImpact_sig
    global JetSmearImpact_sig
    global MuScaleImpact_MC
    global JetScaleImpact_MC
    global MuSmearImpact_MC
    global JetSmearImpact_MC
    global LumiImpact_sig
    global LumiImpact_MC
    global PUImpact_sig
    global PUImpact_MC
    global ZMatchImpact_MC
    global ZScaleImpact_MC
    global ZShapeImpact_MC
    global IDImpact_sig
    global IDImpact_MC
    global TriggerImpact_sig
    global TriggerImpact_MC
    global QCDNormImpact_MC
    global TTNormImpact_MC
    global ZNormImpact_MC
    global ZNNPDFImpact
    global SigNNPDFImpact
    global TotalUncertainty_MC 
    global TotalUncertainty_Sig
    global ZRescaleImpact_MC

    MuScaleImpact_sig = (abs(1-MuScaleUpError_sig)/2.+abs(1-MuScaleDownError_sig)/2.)
    JetScaleImpact_sig = (abs(1-JetScaleUpError_sig)/2.+abs(1-JetScaleDownError_sig)/2.)
    MuSmearImpact_sig = abs(1-MuSmearError_sig)
    JetSmearImpact_sig = abs(1-JetSmearError_sig)
    MuScaleImpact_MC = (abs(1-MuScaleUpError_MC)/2.+abs(1-MuScaleDownError_MC)/2.)
    JetScaleImpact_MC = (abs(1-JetScaleUpError_MC)/2.+abs(1-JetScaleDownError_MC)/2.)
    MuSmearImpact_MC = abs(1-MuSmearError_MC)
    JetSmearImpact_MC = abs(1-JetSmearError_MC)  

    LumiImpact_sig = (lumierr-1)
    LumiImpact_MC = ( ( (lumierr-1)*BGleftover) / MC)
    PUImpact_sig = (abs(1-PUupError_sig)/2.+abs(1-PUdownError_sig)/2.)
    PUImpact_MC = (abs(1-PUupError_MC)/2.+abs(1-PUdownError_MC)/2.)

    ZMatchImpact_MC = (abs(1-ZMatchUpError_MC)/2.+abs(1-ZMatchDownError_MC)/2.)
    ZScaleImpact_MC = (abs(1-ZScaleUpError_MC)/2.+abs(1-ZScaleDownError_MC)/2.)

    ZRescaleImpact_MC=((zrescale-1)*(Z/MC))

    ZShapeImpact_MC = max(ZMatchImpact_MC,ZScaleImpact_MC)

    IDImpact_sig = (recoerr-1)*100
    IDImpact_MC = ( ( (recoerr-1)*BGleftover) / MC)
    TriggerImpact_sig = (trigerr-1)*100
    TriggerImpact_MC = ( ( (trigerr-1)*BGleftover) / MC)

    QCDNormImpact_MC = ( ( (qcdratioerr)*QCD) / MC)
    TTNormImpact_MC = ( ( (ttratioerr)*TT) / MC)
    ZNormImpact_MC = ( ( (znormerr)*Z) / MC)

    ZNNPDFImpact = numpy.mean([( ( (Z_NNPDFdown)*Z) / MC),( ( (Z_NNPDFup)*Z) / MC)])
    SigNNPDFImpact = numpy.mean([( ( (sig_NNPDFdown))),( ( (sig_NNPDFup)) )])

    print ZShapeImpact_MC

    TotalUncertainty_MC = (MuScaleImpact_MC**2+JetScaleImpact_MC**2+MuSmearImpact_MC**2+JetSmearImpact_MC**2+LumiImpact_MC**2+PUImpact_MC**2+ZShapeImpact_MC**2+ZNNPDFImpact**2+ZRescaleImpact_MC**2)**(0.5)

    TotalUncertainty_Sig = (MuScaleImpact_sig**2+JetScaleImpact_sig**2+MuSmearImpact_sig**2+JetSmearImpact_sig**2+PUImpact_sig**2+SigNNPDFImpact**2)**(0.5)

def SaveValuesForExample():
    #print "MC = " +str(MC)
    #print "MC scaleup = " +str(MC_JetScaleUp)
    #print "MC scaledown = " +str(MC_JetScaleDown)
    global MuScaleImpact_sig300
    global JetScaleImpact_sig300
    global MuSmearImpact_sig300
    global JetSmearImpact_sig300
    global MuScaleImpact_MC300
    global JetScaleImpact_MC300
    global MuSmearImpact_MC300
    global JetSmearImpact_MC300

    global LumiImpact_sig300
    global LumiImpact_MC300
    global PUImpact_sig300
    global PUImpact_MC300
    global IDImpact_sig300
    global IDImpact_MC300
    global TriggerImpact_sig300
    global TriggerImpact_MC300

    global QCDNormImpact_MC300
    global TTNormImpact_MC300
    global ZNormImpact_MC300
    global ZRescaleImpact_MC300
    global ZMatchImpact_MC300
    global ZShapeImpact_MC300
    global ZScaleImpact_MC300
    global ZNNPDFImpact300
    global SigNNPDFImpact300
    global ZCTEQImpact
    global ZMSTWImpact
    global localTotalSystError_MC300 
    global localTotalSystError_Sig300 
    global localTotalStatError_MC300
    global localTotalStatError_Sig300


    print "Saving values..."


    MuScaleImpact_sig300 = (abs(1-MuScaleUpError_sig)/2.+abs(1-MuScaleDownError_sig)/2.)*100
    JetScaleImpact_sig300 = (abs(1-JetScaleUpError_sig)/2.+abs(1-JetScaleDownError_sig)/2.)*100
    MuSmearImpact_sig300 = abs(1-MuSmearError_sig)*100
    JetSmearImpact_sig300 = abs(1-JetSmearError_sig)*100
    MuScaleImpact_MC300 = (abs(1-MuScaleUpError_MC)/2.+abs(1-MuScaleDownError_MC)/2.)*100
    JetScaleImpact_MC300 = (abs(1-JetScaleUpError_MC)/2.+abs(1-JetScaleDownError_MC)/2.)*100
    MuSmearImpact_MC300 = abs(1-MuSmearError_MC)*100
    JetSmearImpact_MC300 = abs(1-JetSmearError_MC)  *100

    LumiImpact_sig300 = (lumierr-1)*100
    LumiImpact_MC300 = ( ( (lumierr-1)*BGleftover) / MC)*100
    PUImpact_sig300 = (abs(1-PUupError_sig)/2.+abs(1-PUdownError_sig)/2.)*100
    PUImpact_MC300 = (abs(1-PUupError_MC)/2.+abs(1-PUdownError_MC)/2.)*100

    ZMatchImpact_MC300 = (abs(1-ZMatchUpError_MC)/2.+abs(1-ZMatchDownError_MC)/2.)*100
    ZScaleImpact_MC300 = (abs(1-ZScaleUpError_MC)/2.+abs(1-ZScaleDownError_MC)/2.)*100

    ZRescaleImpact_MC300=((zrescale-1) *(Z/MC))*100

    ZShapeImpact_MC300 = max(ZMatchImpact_MC300,ZScaleImpact_MC300)

    IDImpact_sig300 = (recoerr-1)*100
    IDImpact_MC300 = ( ( (recoerr-1)*BGleftover) / MC)*100
    TriggerImpact_sig300 = (trigerr-1)*100
    TriggerImpact_MC300 = ( ( (trigerr-1)*BGleftover) / MC)*100

    QCDNormImpact_MC300 = ( ( (qcdratioerr)*QCD) / MC)*100
    TTNormImpact_MC300 = ( ( (ttratioerr)*TT) / MC)*100
    ZNormImpact_MC300 = ( ( (znormerr)*Z) / MC)*100

    ZNNPDFImpact300 = numpy.mean([( ( (Z_NNPDFdown)*Z) / MC)*100,( ( (Z_NNPDFup)*Z) / MC)*100])
    SigNNPDFImpact300 = numpy.mean([( ( (sig_NNPDFdown)))*100,( ( (sig_NNPDFup)) )*100])


    print "TOTAL UNCERTAINTY = "+str(TotalUncertainty_MC)

    #localTotalSystError_MC300 = ( (((trigerr-1)**2+(recoerr-1)**2+(lumierr-1)**2+znormerr**2+qcdratioerr**2+ttratioerr**2+TotalUncertainty_MC)**(0.5))*100)

    #localTotalSystError_MC300 =  (ZNNPDFImpact300**2+ZShapeImpact_MC300**2+PUImpact_sig300**2+TriggerImpact_MC300**2+IDImpact_MC300**2+LumiImpact_MC300**2+ZNormImpact_MC300**2+QCDNormImpact_MC300**2+TTNormImpact_MC300**2+(TotalUncertainty_MC*100)**2)**0.5

    localTotalSystError_MC300 =  (TriggerImpact_MC300**2+IDImpact_MC300**2+ZNormImpact_MC300**2+ZRescaleImpact_MC300**2+QCDNormImpact_MC300**2+TTNormImpact_MC300**2+(TotalUncertainty_MC*100)**2)**0.5

    tterrorimpact=(tterror-1)*(tt/MC)
    zerrorimpact=(zerror-1)*(z/MC)
    dibosonerrorimpact=(dibosonerror-1)*(diboson/MC)
    singtoperrorimpact=(singtoperror-1)*(singtop/MC)
    wjetserrorimpact=(wjetserror-1)*(wjets/MC)
    qcderrorimpact=(qcderror-1)*(qcd/MC)
    localTotalStatError_MC300 = (((tterrorimpact)**2+(zerrorimpact)**2+(dibosonerrorimpact)**2+(singtoperrorimpact)**2+(wjetserrorimpact)**2+(qcderrorimpact)**2)**(0.5))*100
    
    print str(tterror)+","+str(zerror)+","+str(dibosonerror)+","+str(singtoperror)+","+str(wjetserror)+","+str(qcderror)
    localTotalSystError_MC300=(localTotalSystError_MC300**2+localTotalStatError_MC300**2)**0.5

    #localTotalSystError_Sig300 =( (((trigerr-1)**2+(recoerr-1)**2+(lumierr-1)**2+znormerr**2+qcdratioerr**2+ttratioerr**2+TotalUncertainty_Sig)**(0.5))*100)

    #localTotalSystError_Sig300 =  (SigNNPDFImpact300**2+TriggerImpact_sig300**2+IDImpact_sig300**2+LumiImpact_sig300**2+(TotalUncertainty_Sig*100)**2)**0.5
    localTotalSystError_Sig300 =  (TriggerImpact_sig300**2+IDImpact_sig300**2+LumiImpact_sig300**2+(TotalUncertainty_Sig*100)**2)**0.5
    localTotalStatError_Sig300 = (sigerror-1)*100
    localTotalSystError_Sig300=(localTotalSystError_Sig300**2+localTotalStatError_Sig300**2)**0.5
    print "sig_NNPDFdown = "+str(sig_NNPDFdown)
    print "sig_NNPDFup = "+str(sig_NNPDFup)
    print "SigNNPDFImpact = "+str(SigNNPDFImpact)
    #ZMSTWImpact = numpy.mean([( ( (Z_MSTWdown)*Z) / MC)*100,( ( (Z_MSTWup)*Z) / MC)*100])
    #ZCTEQImpact = numpy.mean([( ( (Z_CTEQdown)*Z) / MC)*100,( ( (Z_CTEQup)*Z) / MC)*100])

from math import log10, floor
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
    
def WriteCards():

    if tt==0:
        localtterror=(tterror-1)
    else:
        localtterror = (tt*(tterror-1))

    if z==0:
        localzerror=(zerror-1)
    else:
        localzerror = (z*(zerror-1))

    if diboson==0:
        localdibosonerror= (dibosonerror-1)
    else:
        localdibosonerror = (diboson*(dibosonerror-1))

    if singtop==0:
        localsingtoperror=(singtoperror-1)
    else:
        localsingtoperror = (singtop*(singtoperror-1))

    if wjets==0:
        localwjetserror=(wjetserror-1)
    else:
        localwjetserror = (wjets*(wjetserror-1))

    if qcd==0:
        localqcderror=(qcderror-1)
    else:
        localqcderror = (qcd*(qcderror-1))

    if sig==0:
        localsigerror=(sig*(sigerror-1))
    else:
        localsigerror = (sig*(sigerror-1))
    
    localTotalStatError = ((localtterror**2+localzerror**2+localdibosonerror**2+localsingtoperror**2+localwjetserror**2+localqcderror**2)**(0.5))

    print "Total statistical error is: "+str(localTotalStatError)

    localLeftoverStatError = (localdibosonerror**2+localsingtoperror**2+localwjetserror**2+localqcderror**2)**(0.5)

    ComputedSystematics2_MC = MuScaleImpact_MC**2+JetScaleImpact_MC**2+MuSmearImpact_MC**2+JetSmearImpact_MC**2+LumiImpact_MC**2+PUImpact_MC**2+ZShapeImpact_MC**2+ZNNPDFImpact**2+ZRescaleImpact_MC**2
    #print "ComputedSystematics2_MC = "+str(ComputedSystematics2_MC)

    ComputedSystematics2_Sig = MuScaleImpact_sig**2+JetScaleImpact_sig**2+MuSmearImpact_sig**2+JetSmearImpact_sig**2+PUImpact_sig**2+SigNNPDFImpact**2
    #print "ComputedSystematics2_Sig = "+str(ComputedSystematics2_Sig)

    print "Local zerror is = "+str(localzerror)
    print "Local z is = "+str(z)



    
    localTotalSystError_MC = MC*((trigerr-1)**2+(recoerr-1)**2+(lumierr-1)**2+znormerr**2+qcdratioerr**2+ttratioerr**2+ComputedSystematics2_MC)**(0.5)
    localTotalSystError_Sig = sig*((trigerr-1)**2+(recoerr-1)**2+(lumierr-1)**2+znormerr**2+qcdratioerr**2+ttratioerr**2+ComputedSystematics2_Sig)**(0.5)

    siground = NPlaces(round_sig(max(localsigerror,localTotalSystError_Sig),2))
    print "----------------------------------"
    print "Max is " + str(max(localsigerror,localTotalSystError_Sig))
    print "round_sig is "+ str(round_sig(max(localsigerror,localTotalSystError_Sig),2))
    print "NPlaces is " + str(NPlaces(round_sig(max(localsigerror,localTotalSystError_Sig),2)))
    print "----------------------------------"

    MCround = NPlaces(round_sig(max(localTotalStatError,localTotalSystError_MC),2))

    print "----------------------------------"
    print "Max is " + str(max(localTotalStatError,localTotalSystError_MC))
    print "round_sig is "+ str(round_sig(max(localTotalStatError,localTotalSystError_MC),2))
    print "NPlaces is " + str(NPlaces(round_sig(max(localTotalStatError,localTotalSystError_MC),2)))
    print "----------------------------------"

    #MCround = NPlaces(round_sig(localTotalSystError_MC,2))
    zround = NPlaces(round_sig(localzerror,2))
    ttround = NPlaces(round_sig(localtterror,2))
    BGleftoverround = NPlaces(round_sig(localLeftoverStatError,2))

    
    #SignalString = str(round(sig,siground))+"\pm "+str(round_sig(localsigerror,2))+"(Stat.)\pm "+str(round_sig(localTotalSystError_Sig,2))+"(Syst.)$"
    #SignalString = str(round(sig,siground))+"\pm "+str(round_sig(localsigerror,2))+"\pm "+str(round_sig(localTotalSystError_Sig,2))+"$"
    if siground <1:
        SignalString = str(int(round(sig,siground)))+"\pm "+str(int(round(localsigerror,siground)))+"\pm "+str(int(round(localTotalSystError_Sig,siground)))
    else:
        SignalString = str(round(sig,siground))+"\pm "+str(round(localsigerror,siground))+"\pm "+str(round(localTotalSystError_Sig,siground))
    DataString = str(int(Data))


    #This is a hack:
    # if round(MC,1) > localTotalSystError_MC:
    #     MCString+= "(Stat.)\pm "+str(round_sig(localTotalSystError_MC,2))+"(Syst.)"
    # else:
    #     #MCString+= "(Stat.)^{+"+str(round_sig(localTotalSystError_MC,2))+"}_{-"+str(round_sig(MC,2))+"}"
    #     if MC==0:
    #         MCString+= "(Stat.)^{+"+str(round_sig(localTotalSystError_MC,2))+"}_{-0.0}(Syst.)"
    #     else:
    #         MCString+= "(Stat.)^{+"+str(round(localTotalSystError_MC,2))+"}_{-"+str(round(MC,MCround))+"}(Syst.)"


    if MCround < 1:
        MCString = str(int(round(MC,MCround)))
        if MC > localTotalStatError:
            MCString+= "\pm "+str(int(round(localTotalStatError,MCround)))
        else:
            MCString+= "^{+"+str(int(round(localTotalStatError,MCround)))+"}_{-"+str(int(round(MC,MCround)))+"}"
        if MC > localTotalSystError_MC:
            MCString+= "\pm "+str(int(round(localTotalSystError_MC,MCround)))
        else:
            if MC==0:
                MCString+= "^{+"+str(int(localTotalSystError_MC))+"}_{-0.0}"
            else:
                MCString+= "^{+"+str(int(localTotalSystError_MC))+"}_{-"+str(int(MC))+"}"
    else:
        MCString = str(round(MC,MCround))
        if MC > localTotalStatError:
            MCString+= "\pm "+str(round(localTotalStatError,MCround))
        else:
            MCString+= "^{+"+str(round(localTotalStatError,MCround))+"}_{-"+str(round(MC,MCround))+"}"
        if MC > localTotalSystError_MC:
            MCString+= "\pm "+str(round(localTotalSystError_MC,MCround))
        else:
            if MC==0:
                MCString+= "^{+"+str(round(localTotalSystError_MC,MCround))+"}_{-0.0}"
            else:
                MCString+= "^{+"+str(round(localTotalSystError_MC,MCround))+"}_{-"+str(round(MC,MCround))+"}"

    if zround < 1:
        if (z > localzerror):
            ZString = str(int(z))+"\pm "+str(int(round(localzerror,zround)))
        else:
            ZString = str(int(z))+"^{+"+str(int(round(localzerror,zround)))+"}_{-"+str(int(round(z,zround)))+"}"
    else:
        if (z > localzerror):
            ZString = str(round(z,zround))+"\pm "+str(round(localzerror,zround))
        else:
            ZString = str(round(z,zround))+"^{+"+str(round(localzerror,zround))+"}_{-"+str(round(z,zround))+"}"

    if ttround < 1:
        if (tt > localtterror):
            TTString = str(int(round(tt,ttround)))+"\pm "+str(int(round(localtterror,ttround)))
        else:
            TTString = str(int(round(tt,ttround)))+"^{+"+str(int(round(localtterror,ttround)))+"}_{-"+str(int(round(tt,ttround)))+"}"
    else:
        if (tt > localtterror):
            TTString = str(round(tt,ttround))+"\pm "+str(round(localtterror,ttround))
        else:
            TTString = str(round(tt,ttround))+"^{+"+str(round(localtterror,ttround))+"}_{-"+str(round(tt,ttround))+"}"

    if BGleftoverround < 1:
        if (BGleftover > localLeftoverStatError):
            LeftoverString = str(int(round(BGleftover,BGleftoverround)))+"\pm "+str(int(round(localLeftoverStatError,BGleftoverround)))
        else:
            LeftoverString = str(int(round(BGleftover,BGleftoverround)))+"^{+"+str(int(round(localLeftoverStatError,BGleftoverround)))+"}_{-"+str(int(round(BGleftover,BGleftoverround)))+"}"
    else:
        if (BGleftover > localLeftoverStatError):
            LeftoverString = str(round(BGleftover,BGleftoverround))+"\pm "+str(round(localLeftoverStatError,BGleftoverround))
        else:
            LeftoverString = str(round(BGleftover,BGleftoverround))+"^{+"+str(round(localLeftoverStatError,BGleftoverround))+"}_{-"+str(round(BGleftover,BGleftoverround))+"}"

    #Rates.write("\\textbf{$"+str(x)+"$} & \\textbf{$"+SignalString+"} & \\textbf{$"+DataString+"$} & \\textbf{$"+MCString+"$} & \\textbf{$"+ZString+"$} & \\textbf{$"+TTString+"$} & \\textbf{$"+LeftoverString+"$}\\\\\n")
    Rates.write("\\textbf{$"+str(x)+"$} & \\textbf{$"+DataString+"$} & \\textbf{$"+MCString+"$} & \\textbf{$"+ZString+"$} & \\textbf{$"+TTString+"$} & \\textbf{$"+LeftoverString+"$}\\\\\n")
    
    SignalRates.write("\\textbf{$"+SignalString+"$}\n" )

    #Rates.write("\\textbf{$"+str(x)+"$} & \\textbf{$"+str(round(sig,siground))+"\pm "+str(round_sig(localsigerror,2))+"(Stat.)\pm "+str(round_sig(localTotalSystError_Sig,2))+"(Syst.)$} & \\textbf{$"+str(Data)+"$} & \\textbf{$"+str(round(MC,MCround))+"\pm "+str(round_sig(localTotalStatError,2))+"(Stat.)\pm "+str(round_sig(localTotalSystError_MC,2))+"(Syst.)$} & \\textbf{$"+str(round(z,zround))+"\pm "+str(round_sig(localzerror,2))+"$} & \\textbf{$"+str(round(tt,ttround))+"\pm "+str(round_sig(localtterror,2))+"$} & \\textbf{$"+str(round(BGleftover,BGleftoverround))+"\pm "+str(round_sig(localLeftoverStatError,2))+"$}\\\\\n")
    #Rates.write("\\hline\n")
    Sigs.write(str(sig/math.sqrt(sig+MC))+'\n')


def WriteExample():
    Uncertainties = open('Uncertainties_2012_'+coupling+'.tex','w') 

    Uncertainties.write("\\begin{frame}\n")
    Uncertainties.write("\\tiny\n")
    Uncertainties.write("\\begin{tabular}{|c|c|c|}\n")
    Uncertainties.write("\\hline\n")

    Uncertainties.write("\\textbf{Systematic Uncertainty} & \\textbf{Impact on Signal} & \\textbf{Impact on Background}\\\\\n")
    Uncertainties.write("\\hline\n")
    if False:
        Uncertainties.write("\\textbf{Luminosity} & \\textbf{"+str("%.2f" % LumiImpact_sig300)+"} & \\textbf{"+str("%.2f" % LumiImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Jet Energy Scale} & \\textbf{"+str("%.2f" % JetScaleImpact_sig300)+"} & \\textbf{"+str("%.2f" % JetScaleImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Jet Energy Resolution}  & \\textbf{"+str("%.2f" % JetSmearImpact_sig300)+"} & \\textbf{"+str("%.2f" % JetSmearImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Electron Energy Scale}  & \\textbf{"+str("%.2f" % MuScaleImpact_sig300)+"} & \\textbf{"+str("%.2f" % MuScaleImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Electron Energy Resolution}  & \\textbf{"+str("%.2f" % MuSmearImpact_sig300)+"} & \\textbf{"+str("%.2f" % MuSmearImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{PileUp}  & \\textbf{"+str("%.2f" % PUImpact_sig300)+"} & \\textbf{"+str("%.2f" % PUImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Electron ID/iso}  & \\textbf{"+str("%.2f" % IDImpact_sig300)+"} & \\textbf{"+str("%.2f" % IDImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")
        Uncertainties.write("\\textbf{Trigger}  & \\textbf{"+str("%.2f" % TriggerImpact_sig300)+"} & \\textbf{"+str("%.2f" % TriggerImpact_MC300)+"}\\\\\n")
        Uncertainties.write("\\hline\n")


    #Uncertainties.write("\\textbf{Background Normalization}  & \\textbf{-} & \\textbf{"+str("%.2f" % ZScaleImpact_MC300)+"}\\\\\n")
    #Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Background Shape}  & \\textbf{-} & \\textbf{"+str("%.2f" % ZShapeImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Luminosity} & \\textbf{"+str("%.2f" % LumiImpact_sig300)+"} & \\textbf{"+str("%.2f" % LumiImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Jet Energy Scale} & \\textbf{"+str("%.2f" % JetScaleImpact_sig300)+"} & \\textbf{"+str("%.2f" % JetScaleImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Jet Energy Resolution}  & \\textbf{"+str("%.2f" % JetSmearImpact_sig300)+"} & \\textbf{"+str("%.2f" % JetSmearImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Electron Energy Scale}  & \\textbf{"+str("%.2f" % MuScaleImpact_sig300)+"} & \\textbf{"+str("%.2f" % MuScaleImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Electron Energy Resolution}  & \\textbf{"+str("%.2f" % MuSmearImpact_sig300)+"} & \\textbf{"+str("%.2f" % MuSmearImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{PileUp}  & \\textbf{"+str("%.2f" % PUImpact_sig300)+"} & \\textbf{"+str("%.2f" % PUImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Electron ID/iso}  & \\textbf{"+str("%.2f" % IDImpact_sig300)+"} & \\textbf{"+str("%.2f" % IDImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Trigger}  & \\textbf{"+str("%.2f" % TriggerImpact_sig300)+"} & \\textbf{"+str("%.2f" % TriggerImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")

    Uncertainties.write("\\textbf{QCD Normalization}  & \\textbf{-} & \\textbf{"+str("%.2f" % QCDNormImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    
    Uncertainties.write("\\textbf{Z Normalization}  & \\textbf{-} & \\textbf{"+str("%.2f" % ZNormImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")

    Uncertainties.write("\\textbf{Z PtLL study}  & \\textbf{-} & \\textbf{"+str("%.2f" % ZRescaleImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")


    Uncertainties.write("\\textbf{t $\\bar{t}$ Normalization}  & \\textbf{-} & \\textbf{"+str("%.2f" % TTNormImpact_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{PDF Weight}  & \\textbf{"+str("%.2f" % SigNNPDFImpact300)+"} & \\textbf{"+str("%.2f" % ZNNPDFImpact300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\hline\n")

    Uncertainties.write("\\textbf{Statistical Uncertainty}  & \\textbf{"+str("%.2f" % localTotalStatError_Sig300)+"} & \\textbf{"+str("%.2f" % localTotalStatError_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Total Systematic Uncertainty}  & \\textbf{"+str("%.2f" % localTotalSystError_Sig300)+"} & \\textbf{"+str("%.2f" % localTotalSystError_MC300)+"}\\\\\n")
    Uncertainties.write("\\hline\n")

    Uncertainties.write("\\end{tabular}")
    Uncertainties.write("\\end{frame}")


    Uncertainties.close()
    
List = [y+2 for y in range(113)] #To start with a value of 2, for gawk

for y in List:
    SetIterators(y)
    SetValues(y)
    MakeConfigFile()

    SaveValuesForCards()
    if x==600:
        SaveValuesForExample()
        WriteExample()

    WriteCards()







Rates.write("\\end{tabular}")
Rates.write("\\end{frame}")
Rates.close()
SignalRates.close()
Sigs.close()
