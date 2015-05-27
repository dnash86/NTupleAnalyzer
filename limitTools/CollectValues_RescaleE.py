import os
import sys
import math


File = os.popen('cat UE_Template.cfg').readlines()



Rates = open('Rates_eleRESCALE.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{M_LQ} & \\textbf{Data} & \\textbf{Signal} & \\textbf{Z-Jets} & \\textbf{ttbar} & \\textbf{VV + W-Jets + QCD}\\\\\n")
Rates.write("\\hline\n")


Uncertainties = open('Uncertainties_eleRESCALE.tex','w') 
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


EleScaleImpact_sig= -1
EleScaleImpact_MC= -1
EleSmearImpact_sig= -1
EleSmearImpact_MC= -1


efferr=1.00
puerr=1.08
accerr=1.01
lumierr=1.022

#muonscale=1.01
#jetscale=1.04

#muonres=1.04
#jetres="varies"
#jetres=1.10

List = [300+x*100 for x in range(6)]
for x in List:
    
    y = (x/50) - 3  #To start with a value of 2, for gawk '(NR==etc...


    String = "grep '"+str(x)+ " GeV' SLQ_request.csv | gawk -F ',' '{print $7}'"
    print String
    NewCS=float(os.popen(String).readline().replace('\n',''))
    
    String = "grep ue LQinfo.csv | grep " +str(x)+" | gawk -F ',' '{print $5}'"
    print String
    OldCS=float(os.popen(String).readline().replace('\n',''))
    Rescaler=(NewCS/1000)/OldCS
    print Rescaler
    LumiRescaler = 4

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $1}'"
    #print String
    Data=float(os.popen(String).readline().replace('\n',''))
    Data = Data * LumiRescaler

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    MC=float(os.popen(String).readline().replace('\n',''))
    MC = MC * LumiRescaler
    
    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $2}'"
    tt=float(os.popen(String).readline().replace('\n',''))
    tt = tt * LumiRescaler

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $1}'"
    tterror=float(os.popen(String).readline().replace('\n',''))
    if tt != 0:
        tterror = (tterror / tt) + 1
    else:
        tterror = 0

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))
    z = z * LumiRescaler

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $2}'"
    zerror=float(os.popen(String).readline().replace('\n',''))
    if z != 0:
        zerror = (zerror / z) + 1
    else:
        zerror = 0

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    sig=float(os.popen(String).readline().replace('\n',''))
    sig = sig * Rescaler * LumiRescaler

    String = "grep -A 26 NoSystematics elelog.txt | gawk -F ',' '(NR==" + str(int(y+13)) +") {print $3}'"
    sigerror=float(os.popen(String).readline().replace('\n',''))
    if sig != 0:
        sigerror = (sigerror / sig) + 1
    else:
        sigerror = 0



    #String = "grep -A 26 EleScaleDown elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_EleScaleDown=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 EleScaleUp elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_EleScaleUp=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetScaleDown elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetScaleUp elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetSmear elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_JetSmear=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 EleSmear elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $4}'"
    #MC_EleSmear=float(os.popen(String).readline().replace('\n',''))

    ########
    #String = "grep -A 26 EleScaleDown elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_EleScaleDown=float(os.popen(String).readline().replace('\n',''))
 
    #String = "grep -A 26 EleScaleUp elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_EleScaleUp=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetScaleDown elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetScaleUp elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 JetSmear elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_JetSmear=float(os.popen(String).readline().replace('\n',''))

    #String = "grep -A 26 EleSmear elelog.txt | gawk -F ',' '(NR==" + str(y) +") {print $5}'"
    #sig_EleSmear=float(os.popen(String).readline().replace('\n',''))

    #EleScaleUpError_MC = 1+  (abs(MC_EleScaleUp - MC) / MC)
    #EleScaleDownError_MC = 1+  (abs(MC_EleScaleDown - MC) / MC)
    #JetScaleUpError_MC = 1+  (abs(MC_JetScaleUp - MC) / MC)
    #JetScaleDownError_MC = 1+  (abs(MC_JetScaleDown - MC) / MC)
    #EleSmearError_MC =   1+ (abs(MC_EleSmear-MC) / MC)
    #JetSmearError_MC =   1+ ((abs(MC_JetSmear-MC)) / MC)

    #EleScaleUpError_sig = 1+  (abs(sig_EleScaleUp - sig) / sig)
    #EleScaleDownError_sig = 1+  (abs(sig_EleScaleDown - sig) / sig)
    #JetScaleUpError_sig = 1+  (abs(sig_JetScaleUp - sig) / sig)
    #JetScaleDownError_sig = 1+  (abs(sig_JetScaleDown - sig) / sig)
    #EleSmearError_sig =   1+ (abs(sig_EleSmear-sig) / sig)
    #JetSmearError_sig =   1+ ((abs(sig_JetSmear-sig)) / sig)

    EleScaleUpError_MC = 1
    EleScaleDownError_MC = 1
    JetScaleUpError_MC = 1
    JetScaleDownError_MC = 1
    EleSmearError_MC =   1
    JetSmearError_MC =   1

    EleScaleUpError_sig = 1
    EleScaleDownError_sig = 1
    JetScaleUpError_sig = 1
    JetScaleDownError_sig = 1
    EleSmearError_sig =   1
    JetSmearError_sig =   1


    BGleftover = MC - tt- z

    Rates.write("\\textbf{"+str(x)+"} & \\textbf{"+str("%.2f" % Data)+"} & \\textbf{"+str("%.2f" % sig)+"} & \\textbf{"+str("%.2f" % z)+"} & \\textbf{"+str("%.2f" % tt)+"} & \\textbf{"+str("%.2f" % BGleftover)+"}\\\\\n")
    Rates.write("\\hline\n")
    
    NewFile = []
    output = open(str(x)+'_eleRESCALE.cfg','w') 
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
        NewFile[Z] = NewFile[Z].replace('EleScaleUpError_MC',str(EleScaleUpError_MC))
        NewFile[Z] = NewFile[Z].replace('EleScaleDownError_MC',str(EleScaleDownError_MC))
        NewFile[Z] = NewFile[Z].replace('JetScaleUpError_MC',str(JetScaleUpError_MC))
        NewFile[Z] = NewFile[Z].replace('JetScaleDownError_MC',str(JetScaleDownError_MC))
        NewFile[Z] = NewFile[Z].replace('JetSmearError_MC',str(JetSmearError_MC))
        NewFile[Z] = NewFile[Z].replace('EleSmearError_MC',str(EleSmearError_MC))
        NewFile[Z] = NewFile[Z].replace('EleScaleUpError_sig',str(EleScaleUpError_sig))
        NewFile[Z] = NewFile[Z].replace('EleScaleDownError_sig',str(EleScaleDownError_sig))
        NewFile[Z] = NewFile[Z].replace('JetScaleUpError_sig',str(JetScaleUpError_sig))
        NewFile[Z] = NewFile[Z].replace('JetScaleDownError_sig',str(JetScaleDownError_sig))
        NewFile[Z] = NewFile[Z].replace('JetSmearError_sig',str(JetSmearError_sig))
        NewFile[Z] = NewFile[Z].replace('EleSmearError_sig',str(EleSmearError_sig))
        output.write(NewFile[Z])
    output.close()


    if x==500:
        print "Saving values..."
        EleScaleImpact_sig = (math.fabs(1-EleScaleUpError_sig)+math.fabs(1-EleScaleDownError_sig)/2)
        JetScaleImpact_sig = (math.fabs(1-JetScaleUpError_sig)+math.fabs(1-JetScaleDownError_sig)/2)
        EleSmearImpact_sig = math.fabs(1-EleSmearError_sig)
        JetSmearImpact_sig = math.fabs(1-JetSmearError_sig)
        EleScaleImpact_MC = (math.fabs(1-EleScaleUpError_MC)+math.fabs(1-EleScaleDownError_MC)/2)
        JetScaleImpact_MC = (math.fabs(1-JetScaleUpError_MC)+math.fabs(1-JetScaleDownError_MC)/2)
        EleSmearImpact_MC = math.fabs(1-EleSmearError_MC)
        JetSmearImpact_MC = math.fabs(1-JetSmearError_MC)                          





Uncertainties.write("\\textbf{Background Normalization} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Background Shape} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Scale} & \\textbf{4} & \\textbf{"+str("%.2f" % JetScaleImpact_sig)+"} & \\textbf{"+str("%.2f" % JetScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Resolution} & \\textbf{varies} & \\textbf{"+str("%.2f" % JetSmearImpact_sig)+"} & \\textbf{"+str("%.2f" % JetSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Electron Energy Scale} & \\textbf{1} & \\textbf{"+str("%.2f" % EleScaleImpact_sig)+"} & \\textbf{"+str("%.2f" % EleScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Electron Energy Resolution} & \\textbf{varies} & \\textbf{"+str("%.2f" % EleSmearImpact_sig)+"} & \\textbf{"+str("%.2f" % EleSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Electron Reco/ID/Iso} & \\textbf{1} & \\textbf{?} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Integrated Luminosity} & \\textbf{2.2} & \\textbf{2.2} & \\textbf{-}\\\\\n")
Uncertainties.write("\\hline\n")




Rates.write("\\end{frame}")
Rates.close()

Uncertainties.write("\\end{frame}")
Uncertainties.close()
