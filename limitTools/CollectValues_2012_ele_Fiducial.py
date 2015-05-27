import os
import sys
import math

a=sys.argv

for n in range(len(a)):
    if a[n]=='-i' or a[n]=='--input':
        InputRescales=a[n+1]

#File = os.popen('cat CMU_Template_2012.cfg').readlines()
File = os.popen('cat CMU_Template.cfg').readlines()
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
InputFile = 'Feb19Redo.txt'

#InputFile = 'EleCheckNewZRescale.txt'
Rates = open('Rates_2012_ele.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{$M_{LQ}$} & \\textbf{$Data$} & \\textbf{$Signal$} & \\textbf{$Total Background$} & \\textbf{$Z-Jets$} & \\textbf{$ttbar$} & \\textbf{$VV + W-Jets + QCD$}\\\\\n")
Rates.write("\\hline\n")



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
trigerr=1.027
recoerr=1.012
lumierr=1.044
#Z normalization error here
znormerr = 0.00682462
#ttbar ratio error here
ttratioerr = 0.00890401
#Various statistics
Data = -1
MC=-1
tt=-1
tterror=-1
z=-1
zerror=-1
diboson=-1
dibosonerror=-1
singtop=-1
singtoperror=-1
wjets=-1
wjetserror=-1
gjets=-1
gjetserror=-1
qcd=-1
#qcderror=-1
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

LumiImpact_sig300= -1
LumiImpact_MC300= -1
PUImpact_sig300= -1
PUImpact_MC300= -1
IDImpact_sig300= -1
IDImpact_MC300= -1
TriggerImpact_sig300= -1
TriggerImpact_MC300= -1

BGleftover = -1
#Iterators
x=-1
coupling="blah"

def SetValues(y):
    global Data
    global MC
    global tt
    global tterror
    global z
    global zerror
    global sig
    global sigerror
    global diboson
    global dibosonerror
    global singtop
    global singtoperror
    global wjets
    global wjetserror
    global gjets
    global gjetserror
    global qcd
    #global qcderror
    global MC_MuScaleDown
    global MC_MuScaleUp
    global MC_JetScaleDown
    global MC_JetScaleUp
    global MC_JetSmear
    global MC_MuSmear
    global MC_PUup
    global MC_PUdown
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
    
    global MuScaleUpError_sig
    global MuScaleDownError_sig
    global JetScaleUpError_sig
    global JetScaleDownError_sig
    global MuSmearError_sig
    global JetSmearError_sig
    global PUupError_sig
    global PUdownError_sig

    global BGleftover

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $1}'"
    #print String
    print x
    Data=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    tt=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $1}'"
    tterror=float(os.popen(String).readline().replace('\n',''))
    print str(tt) + " +/- "+str(tterror)
    if tt != 0:
        tterror = (tterror / tt) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $2}'"
    zerror=float(os.popen(String).readline().replace('\n',''))
    if z != 0:
        zerror = (zerror / z) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    diboson=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $3}'"
    dibosonerror=float(os.popen(String).readline().replace('\n',''))
    if diboson != 0:
        dibosonerror = (dibosonerror / diboson) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    singtop=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $4}'"
    singtoperror=float(os.popen(String).readline().replace('\n',''))
    if singtop != 0:
        singtoperror = (singtoperror / singtop) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $6}'"
    wjets=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $5}'"
    wjetserror=float(os.popen(String).readline().replace('\n',''))
    if wjets != 0:
        wjetserror = (wjetserror / wjets) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $7}'"
    gjets=float(os.popen(String).readline().replace('\n',''))
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $6}'"
    gjetserror=float(os.popen(String).readline().replace('\n',''))
    if gjets != 0:
        gjetserror = (gjetserror / gjets) + 1

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $8}'"
    qcd=float(os.popen(String).readline().replace('\n',''))

    String = "gawk '(NR=="+str(y)+")' "+InputRescales
    CurrentRescaler=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $9}'"
    sig=float(os.popen(String).readline().replace('\n',''))
    #sig = sig / CurrentRescaler
    String = "grep -A 226 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(int(y+113)) +") {print $7}'"
    sigerror=float(os.popen(String).readline().replace('\n',''))
    if sig != 0:
        sigerror = (sigerror / sig) + 1

        #sigerror = sigerror / CurrentRescaler

    MC = qcd+gjets+wjets+singtop+diboson+z+tt

    MC_MuScaleDown=GetTotalMC("MuScaleDown",y)

    MC_MuScaleUp=GetTotalMC("MuScaleUp",y)

    MC_JetScaleDown=GetTotalMC("JetScaleDown",y)

    MC_JetScaleUp=GetTotalMC("JetScaleUp",y)

    MC_JetSmear=GetTotalMC("JetSmear",y)

    MC_MuSmear=GetTotalMC("MuSmear",y)

    MC_PUup=GetTotalMC("PU_up",y)

    MC_PUdown=GetTotalMC("PU_down",y)


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

    MuScaleUpError_sig = 1+  (abs(sig_MuScaleUp - sig) / sig)
    MuScaleDownError_sig = 1+  (abs(sig_MuScaleDown - sig) / sig)
    JetScaleUpError_sig = 1+  (abs(sig_JetScaleUp - sig) / sig)
    JetScaleDownError_sig = 1+  (abs(sig_JetScaleDown - sig) / sig)
    MuSmearError_sig =   1+ (abs(sig_MuSmear-sig) / sig)
    JetSmearError_sig =   1+ ((abs(sig_JetSmear-sig)) / sig)
    PUupError_sig = 1+  (abs(sig_PUup - sig) / sig)
    PUdownError_sig = 1+  (abs(sig_PUdown - sig) / sig)

    BGleftover = MC - tt- z

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

def MakeConfigFile():
    
    
    NewFile = []
    output = open(str(x)+'_'+coupling+'_2012temp.cfg','w') 
    for Z in range(len(File)): 
        NewFile.append(File[Z])
    for Z in range(len(File)): 
        NewFile[Z] = NewFile[Z].replace('signalerror',str(sigerror))
        NewFile[Z] = NewFile[Z].replace('signalerror',str(sigerror))
        NewFile[Z] = NewFile[Z].replace('zerror',str(zerror))
        NewFile[Z] = NewFile[Z].replace('tterror',str(tterror))
        NewFile[Z] = NewFile[Z].replace('Data',str(Data))
        NewFile[Z] = NewFile[Z].replace('signal',str(sig))
        NewFile[Z] = NewFile[Z].replace('z',str(z))
        NewFile[Z] = NewFile[Z].replace('tt',str(tt))
        NewFile[Z] = NewFile[Z].replace('BGleftover',str(BGleftover))
        NewFile[Z] = NewFile[Z].replace('recoerr',str(recoerr))
        NewFile[Z] = NewFile[Z].replace('trigerr',str(trigerr))
        NewFile[Z] = NewFile[Z].replace('lumierr',str(lumierr))
        NewFile[Z] = NewFile[Z].replace('PUupError_sig',str(PUupError_sig))
        NewFile[Z] = NewFile[Z].replace('PUupError_MC',str(PUupError_MC))
        NewFile[Z] = NewFile[Z].replace('PUdownError_MC',str(PUdownError_MC))
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

    MuScaleImpact_sig = (abs(1-MuScaleUpError_sig)/2.+abs(1-MuScaleDownError_sig)/2.)
    JetScaleImpact_sig = (abs(1-JetScaleUpError_sig)/2.+abs(1-JetScaleDownError_sig)/2.)
    MuSmearImpact_sig = abs(1-MuSmearError_sig)
    JetSmearImpact_sig = abs(1-JetSmearError_sig)
    MuScaleImpact_MC = (abs(1-MuScaleUpError_MC)/2.+abs(1-MuScaleDownError_MC)/2.)
    JetScaleImpact_MC = (abs(1-JetScaleUpError_MC)/2.+abs(1-JetScaleDownError_MC)/2.)
    MuSmearImpact_MC = abs(1-MuSmearError_MC)
    JetSmearImpact_MC = abs(1-JetSmearError_MC)  

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
    IDImpact_sig300 = (recoerr-1)*100
    IDImpact_MC300 = ( ( (recoerr-1)*BGleftover) / MC)*100
    TriggerImpact_sig300 = (trigerr-1)*100
    TriggerImpact_MC300 = ( ( (trigerr-1)*BGleftover) / MC)*100


def WriteCards():

    if tt==0:
        localtterror=(tt*(tterror-1))
    else:
        localtterror = (tt*(tterror-1))

    if z==0:
        localzerror=(z*(zerror-1))
    else:
        localzerror = (z*(zerror-1))

    if diboson==0:
        localdibosonerror= (diboson*(dibosonerror-1))
    else:
        localdibosonerror = (diboson*(dibosonerror-1))

    if singtop==0:
        localsingtoperror=(singtop*(singtoperror-1))
    else:
        localsingtoperror = (singtop*(singtoperror-1))

    if wjets==0:
        localwjetserror=(wjets*(wjetserror-1))
    else:
        localwjetserror = (wjets*(wjetserror-1))

    if gjets==0:
        localgjetserror=(gjets*(gjetserror-1))
    else:
        localgjetserror = (gjets*(gjetserror-1))

    if sig==0:
        localsigerror=(sig*(sigerror-1))
    else:
        localsigerror = (sig*(sigerror-1))
    
    localTotalStatError = ((localtterror**2+localzerror**2+localdibosonerror**2+localsingtoperror**2+localwjetserror**2+localgjetserror**2)**(0.5))

    localLeftoverStatError = (localdibosonerror**2+localsingtoperror**2+localwjetserror**2+localgjetserror**2)**(0.5)

    ComputedSystematics2 = MuScaleImpact_sig**2+JetScaleImpact_sig**2+MuSmearImpact_sig**2+JetSmearImpact_sig**2+MuScaleImpact_MC**2+JetScaleImpact_MC**2+MuSmearImpact_MC**2+JetSmearImpact_MC**2

    localTotalSystError = MC*((trigerr-1)**2+(recoerr-1)**2+(lumierr-1)**2+znormerr**2+ttratioerr**2+ComputedSystematics2)**(0.5)
    Rates.write("\\textbf{$"+str(x)+"$} & \\textbf{$"+str(Data)+"$} & \\textbf{$"+str(round(sig,2))+"\pm "+str(round(localsigerror,3))+"$} & \\textbf{$"+str(round(MC,2))+"\pm "+str(round(localTotalStatError,3))+"(Stat.)\pm "+str(round(localTotalSystError,3))+"(Syst.)$} & \\textbf{$"+str(round(z,2))+"\pm "+str(round(localzerror,3))+"$} & \\textbf{$"+str(round(tt,2))+"\pm "+str(round(localtterror,3))+"$} & \\textbf{$"+str(round(BGleftover,2))+"\pm "+str(round(localLeftoverStatError,3))+"$}\\\\\n")
    Rates.write("\\hline\n")

def WriteExample():
    Uncertainties = open('Uncertainties_2012_'+coupling+'.tex','w') 
    Uncertainties.write("\\begin{frame}\n")
    Uncertainties.write("\\tiny\n")
    Uncertainties.write("\\begin{tabular}{|c|c|c|}\n")
    Uncertainties.write("\\hline\n")
    Uncertainties.write("\\textbf{Systematic Uncertainty} & \\textbf{Impact on Signal} & \\textbf{Impact on Background}\\\\\n")
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

    Uncertainties.write("\\end{tabular}")
    Uncertainties.write("\\end{frame}")
    Uncertainties.close()
    
List = [y+2 for y in range(113)] #To start with a value of 2, for gawk

for y in List:
    SetIterators(y)
    SetValues(y)
    MakeConfigFile()

    if x==300:
        SaveValuesForExample()
        WriteExample()
    SaveValuesForCards()
    WriteCards()




Rates.write("\\end{tabular}")
Rates.write("\\end{frame}")
Rates.close()

