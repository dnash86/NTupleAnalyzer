import os
import sys
import math


File = os.popen('cat CMU_Template.cfg').readlines()



Rates = open('Rates.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{M_LQ} & \\textbf{Data} & \\textbf{Signal} & \\textbf{Z-Jets} & \\textbf{ttbar} & \\textbf{VV + W-Jets + QCD}\\\\\n")
Rates.write("\\hline\n")


Uncertainties = open('Uncertainties.tex','w') 
Uncertainties.write("\\begin{frame}\n")
Uncertainties.write("\\tiny\n")
Uncertainties.write("\\begin{tabular}{|c|c|c|c|}\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Systematic Uncertainty} & \\textbf{Magnitude} & \\textbf{Impact on Signal} & \\textbf{Impact on Background}\\\\\n")
Uncertainties.write("\\hline\n")



JetScaleImpact_sig= -1
JetScaleImpact_MC= -1
JetSmearImpact_sig= -1
JetSmearImpact_MC= -1


MuScaleImpact_sig= -1
MuScaleImpact_MC= -1
MuSmearImpact_sig= -1
MuSmearImpact_MC= -1

  
efferr=1.00
puerr=1.08
accerr=1.01
lumierr=1.022

#muonscale=1.01
#jetscale=1.04

#muonres=1.04
#jetres="varies"
#jetres=1.10

List = [250+x*50 for x in range(13)]
for x in List:
    
    y = (x/50) - 3  #To start with a value of 2, for gawk '(NR==etc...

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $1}'"
    print String
    Data=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC=float(os.popen(String).readline().replace('\n',''))
    
    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    tt=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $1}'"
    tterror=float(os.popen(String).readline().replace('\n',''))
    if tt != 0:
        tterror = (tterror / tt) + 1
    else:
        tterror = 0

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $2}'"
    zerror=float(os.popen(String).readline().replace('\n',''))
    if z != 0:
        zerror = (zerror / z) + 1
    else:
        zerror = 0

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 NoSystematics MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $3}'"
    sigerror=float(os.popen(String).readline().replace('\n',''))
    if sig != 0:
        sigerror = (sigerror / sig) + 1
    else:
        sigerror = 0



    String = "grep -A 26 MuScaleDown MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_MuScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 MuScaleUp MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_MuScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetScaleDown MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetScaleUp MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetSmear MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_JetSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 MuSmear MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_MuSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 PU_up MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_PUup=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 PU_down MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC_PUdown=float(os.popen(String).readline().replace('\n',''))

    ########
    String = "grep -A 26 MuScaleDown MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_MuScaleDown=float(os.popen(String).readline().replace('\n',''))
 
    String = "grep -A 26 MuScaleUp MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_MuScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetScaleDown MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetScaleUp MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 JetSmear MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_JetSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 MuSmear MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_MuSmear=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 PU_up MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig_PUup=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 26 PU_down MuMuIntegrals.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
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

    Rates.write("\\textbf{"+str(x)+"} & \\textbf{"+str("%.2f" % Data)+"} & \\textbf{"+str("%.2f" % sig)+"} & \\textbf{"+str("%.2f" % z)+"} & \\textbf{"+str("%.2f" % tt)+"} & \\textbf{"+str("%.2f" % BGleftover)+"}\\\\\n")
    Rates.write("\\hline\n")
    
    NewFile = []
    output = open(str(x)+'.cfg','w') 
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
        NewFile[Z] = NewFile[Z].replace('accerr',str(accerr))
        NewFile[Z] = NewFile[Z].replace('efferr',str(efferr))
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


    if x==500:
        print "Saving values..."
        MuScaleImpact_sig = (math.fabs(1-MuScaleUpError_sig)+math.fabs(1-MuScaleDownError_sig)/2)
        JetScaleImpact_sig = (math.fabs(1-JetScaleUpError_sig)+math.fabs(1-JetScaleDownError_sig)/2)
        MuSmearImpact_sig = math.fabs(1-MuSmearError_sig)
        JetSmearImpact_sig = math.fabs(1-JetSmearError_sig)
        MuScaleImpact_MC = (math.fabs(1-MuScaleUpError_MC)+math.fabs(1-MuScaleDownError_MC)/2)
        JetScaleImpact_MC = (math.fabs(1-JetScaleUpError_MC)+math.fabs(1-JetScaleDownError_MC)/2)
        MuSmearImpact_MC = math.fabs(1-MuSmearError_MC)
        JetSmearImpact_MC = math.fabs(1-JetSmearError_MC)
        PUImpact_sig = (math.fabs(1-PUupError_sig)+math.fabs(1-PUdownError_sig)/2)
        PUImpact_MC = (math.fabs(1-PUupError_MC)+math.fabs(1-PUdownError_MC)/2)





Uncertainties.write("\\textbf{Background Normalization} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Background Shape} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Scale} & \\textbf{4} & \\textbf{"+str("%.2f" % JetScaleImpact_sig)+"} & \\textbf{"+str("%.2f" % JetScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Resolution} & \\textbf{varies} & \\textbf{"+str("%.2f" % JetSmearImpact_sig)+"} & \\textbf{"+str("%.2f" % JetSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Energy Scale} & \\textbf{1} & \\textbf{"+str("%.2f" % MuScaleImpact_sig)+"} & \\textbf{"+str("%.2f" % MuScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Energy Resolution} & \\textbf{varies} & \\textbf{"+str("%.2f" % MuSmearImpact_sig)+"} & \\textbf{"+str("%.2f" % MuSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Reco/ID/Iso} & \\textbf{1} & \\textbf{?} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Pile Up} & \\textbf{8} & \\textbf{"+str("%.2f" % PUImpact_sig)+"} & \\textbf{"+str("%.2f" % PUImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Integrated Luminosity} & \\textbf{2.2} & \\textbf{2.2} & \\textbf{-}\\\\\n")
Uncertainties.write("\\hline\n")




Rates.write("\\end{frame}")
Rates.close()

Uncertainties.write("\\end{frame}")
Uncertainties.close()
