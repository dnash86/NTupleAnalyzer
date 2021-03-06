import os
import sys
import math


#File = os.popen('cat CMU_Template.cfg').readlines()
File = os.popen('cat CMU_Template_2012.cfg').readlines()
#InputFile = "2012MuonOutput.txt"
#InputFile = "MuonPreselectionNumbers.txt"
#InputFile = "MuonPtChoice.txt"
InputFile = "NewMuonNumbers.txt"
InputFile = "MuonLowerDileptonMassCut.txt"

Rates = open('Rates_2012temp.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{$M_{LQ}$} & \\textbf{Data} & \\textbf{Signal} & \\textbf{Total BG} & \\textbf{Z-Jets} & \\textbf{ttbar} & \\textbf{VV + W-Jets + QCD}\\\\\n")
Rates.write("\\hline\n")


Uncertainties = open('Uncertainties_2012temp.tex','w') 
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

List = [300+x*100 for x in range(16)]
for x in List:
    
    y = (x/100) - 1  #To start with a value of 2, for gawk '(NR==etc...

    String = "grep -A 16 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $1}'"
    print String
    Data=float(os.popen(String).readline().replace('\n',''))

    String = "grep -A 16 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC=float(os.popen(String).readline().replace('\n',''))
    
    String = "grep -A 16 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    tt=float(os.popen(String).readline().replace('\n',''))

    if tt != 0:
        tterror = 1.05
    else:
        tterror = 0

    String = "grep -A 16 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))

    if z != 0:
        zerror = 1.05
    else:
        zerror = 0

    String = "grep -A 16 NoSystematics " + InputFile + " | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig=float(os.popen(String).readline().replace('\n',''))

    if sig != 0:
        sigerror = 1.1
    else:
        sigerror = 0


    MuScaleUpError_MC = 1.05
    MuScaleDownError_MC = 1.05
    JetScaleUpError_MC = 1.05
    JetScaleDownError_MC = 1.05
    MuSmearError_MC =   1.05
    JetSmearError_MC =   1.05

    MuScaleUpError_sig = 1.05
    MuScaleDownError_sig = 1.05
    JetScaleUpError_sig = 1.05
    JetScaleDownError_sig = 1.05
    MuSmearError_sig =   1.05
    JetSmearError_sig =   1.05
    BGleftover = MC - tt- z

    Rates.write("\\textbf{"+str(x)+"} & \\textbf{"+str("%.2f" % Data)+"} & \\textbf{"+str("%.2f" % sig)+"} & \\textbf{"+str("%.2f" % MC)+"} & \\textbf{"+str("%.2f" % z)+"} & \\textbf{"+str("%.2f" % tt)+"} & \\textbf{"+str("%.2f" % BGleftover)+"}\\\\\n")
    Rates.write("\\hline\n")
    
    NewFile = []
    output = open(str(x)+'_2012temp.cfg','w') 
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
        NewFile[Z] = NewFile[Z].replace('puerr',str(puerr))
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
Uncertainties.write("\\textbf{Integrated Luminosity} & \\textbf{2.2} & \\textbf{2.2} & \\textbf{-}\\\\\n")
Uncertainties.write("\\hline\n")




Rates.write("\\end{frame}")
Rates.close()

Uncertainties.write("\\end{frame}")
Uncertainties.close()
