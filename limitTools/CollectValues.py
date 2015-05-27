import os
import sys
import math


File = os.popen('cat CMU_Template.cfg').readlines()


#for x in range(len(File)):
 #   File[x] = File[x].replace('\n','')


Rates = open('Rates.tex','w') 
Rates.write("\\begin{frame}\n")
Rates.write("\\tiny\n")
Rates.write("\\begin{tabular}{|c|c|c|c|c|}\n")
Rates.write("\\hline\n")
Rates.write("\\textbf{M_LQ} & \\textbf{Signal} & \\textbf{Z-Jets} & \\textbf{ttbar} & \\textbf{VV + W-Jets + QCD}\\\\\n")
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
    #if x==300:
    #    continue
    #if x==850:
    #    continue
    #Location = '/afs/cern.ch/work/d/dnash/private/PlotResults/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub.C.txt'
    Location = '/afs/cern.ch/work/d/dnash/private/PlotResults/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub.C.txt'
    Location_MuScaleDown = '/afs/cern.ch/work/d/dnash/private/PlotResults/MuScaleDown/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_MuScaleDown.C.txt'
    Location_MuScaleUp = '/afs/cern.ch/work/d/dnash/private/PlotResults/MuScaleUp/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_MuScaleUp.C.txt'
    Location_JetScaleDown = '/afs/cern.ch/work/d/dnash/private/PlotResults/JetScaleDown/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_JetScaleDown.C.txt'
    Location_JetScaleUp = '/afs/cern.ch/work/d/dnash/private/PlotResults/JetScaleUp/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_JetScaleUp.C.txt'
    Location_MuSmear = '/afs/cern.ch/work/d/dnash/private/PlotResults/MuSmear/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_MuSmear.C.txt'
    Location_JetSmear = '/afs/cern.ch/work/d/dnash/private/PlotResults/JetSmear/outputlog_LQToCMu'+str(x)+'_MakePlotsSingle_mumu_Sub_JetSmear.C.txt'

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "Data   :" | gawk '
    String = String + "'{print $3}'"
    #print String
    Data=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    MC=float(os.popen(String).readline().replace('\n',''))

    
    String = 'grep -A 6 ST_pf_ '+Location+' | grep "tt   :" | gawk '
    String = String + "'{print $3}'"
    tt=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "tt   :" | gawk '
    String = String + "'{print $5}'"
    tterror=float(os.popen(String).readline().replace('\n',''))
    tterror = (tterror / tt) + 1

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "z   :" | gawk '
    String = String + "'{print $3}'"
    z=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "z   :" | gawk '
    String = String + "'{print $5}'"
    zerror=float(os.popen(String).readline().replace('\n',''))
    zerror = (zerror / z) + 1

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location+' | grep "Signal   :" | gawk '
    String = String + "'{print $5}'"
    sigerror=float(os.popen(String).readline().replace('\n',''))
    sigerror = (sigerror / sig) + 1



    String = 'grep -A 6 ST_pf_ '+Location_MuScaleDown+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    #print String
    MC_MuScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_MuScaleUp+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    MC_MuScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetScaleDown+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    MC_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetScaleUp+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    print String
    MC_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetSmear+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    MC_JetSmear=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_MuSmear+' | grep "All MC :" | gawk '
    String = String + "'{print $4}'"
    MC_MuSmear=float(os.popen(String).readline().replace('\n',''))

    ########
    String = 'grep -A 6 ST_pf_ '+Location_MuScaleDown+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    #print String
    sig_MuScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_MuScaleUp+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig_MuScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetScaleDown+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig_JetScaleDown=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetScaleUp+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig_JetScaleUp=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_JetSmear+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig_JetSmear=float(os.popen(String).readline().replace('\n',''))

    String = 'grep -A 6 ST_pf_ '+Location_MuSmear+' | grep "Signal   :" | gawk '
    String = String + "'{print $3}'"
    sig_MuSmear=float(os.popen(String).readline().replace('\n',''))

    MuScaleUpError_MC = 1+  (abs(MC_MuScaleUp - MC) / MC)
    MuScaleDownError_MC = 1+  (abs(MC_MuScaleDown - MC) / MC)
    JetScaleUpError_MC = 1+  (abs(MC_JetScaleUp - MC) / MC)
    JetScaleDownError_MC = 1+  (abs(MC_JetScaleDown - MC) / MC)
    MuSmearError_MC =   1+ (abs(MC_MuSmear-MC) / MC)
    JetSmearError_MC =   1+ ((abs(MC_JetSmear-MC)) / MC)

    MuScaleUpError_sig = 1+  (abs(sig_MuScaleUp - sig) / sig)
    MuScaleDownError_sig = 1+  (abs(sig_MuScaleDown - sig) / sig)
    JetScaleUpError_sig = 1+  (abs(sig_JetScaleUp - sig) / sig)
    JetScaleDownError_sig = 1+  (abs(sig_JetScaleDown - sig) / sig)
    MuSmearError_sig =   1+ (abs(sig_MuSmear-sig) / sig)
    JetSmearError_sig =   1+ ((abs(sig_JetSmear-sig)) / sig)
    BGleftover = MC - tt- z

    Rates.write("\\textbf{"+str(x)+"} & \\textbf{"+str(sig)+"} & \\textbf{"+str(z)+"} & \\textbf{"+str(tt)+"} & \\textbf{"+str(BGleftover)+"}\\\\\n")
    Rates.write("\\hline\n")
    
    NewFile = []
    output = open(str(x)+'.cfg','w') 
    for x in range(len(File)): 
        NewFile.append(File[x])
    for x in range(len(File)): 
        NewFile[x] = NewFile[x].replace('signalerror',str(sigerror))
        NewFile[x] = NewFile[x].replace('signalerror',str(sigerror))
        NewFile[x] = NewFile[x].replace('zerror',str(zerror))
        NewFile[x] = NewFile[x].replace('tterror',str(tterror))
        NewFile[x] = NewFile[x].replace('Data',str(Data))
        NewFile[x] = NewFile[x].replace('signal',str(sig))
        NewFile[x] = NewFile[x].replace('z',str(z))
        NewFile[x] = NewFile[x].replace('tt',str(tt))
        NewFile[x] = NewFile[x].replace('BGleftover',str(BGleftover))
        NewFile[x] = NewFile[x].replace('accerr',str(accerr))
        NewFile[x] = NewFile[x].replace('efferr',str(efferr))
        NewFile[x] = NewFile[x].replace('lumierr',str(lumierr))
        NewFile[x] = NewFile[x].replace('puerr',str(puerr))
        NewFile[x] = NewFile[x].replace('MuScaleUpError_MC',str(MuScaleUpError_MC))
        NewFile[x] = NewFile[x].replace('MuScaleDownError_MC',str(MuScaleDownError_MC))
        NewFile[x] = NewFile[x].replace('JetScaleUpError_MC',str(JetScaleUpError_MC))
        NewFile[x] = NewFile[x].replace('JetScaleDownError_MC',str(JetScaleDownError_MC))
        NewFile[x] = NewFile[x].replace('JetSmearError_MC',str(JetSmearError_MC))
        NewFile[x] = NewFile[x].replace('MuSmearError_MC',str(MuSmearError_MC))
        NewFile[x] = NewFile[x].replace('MuScaleUpError_sig',str(MuScaleUpError_sig))
        NewFile[x] = NewFile[x].replace('MuScaleDownError_sig',str(MuScaleDownError_sig))
        NewFile[x] = NewFile[x].replace('JetScaleUpError_sig',str(JetScaleUpError_sig))
        NewFile[x] = NewFile[x].replace('JetScaleDownError_sig',str(JetScaleDownError_sig))
        NewFile[x] = NewFile[x].replace('JetSmearError_sig',str(JetSmearError_sig))
        NewFile[x] = NewFile[x].replace('MuSmearError_sig',str(MuSmearError_sig))
        output.write(NewFile[x])
    output.close()

    if x==500:
        MuScaleImpact_sig = ((1-MuScaleUpError_sig)+(1-MuScaleDownError_sig)/2)
        JetScaleImpact_sig = ((1-JetScaleUpError_sig)+(1-JetScaleDownError_sig)/2)
        MuSmearImpact_sig = (1-MuSmearError_sig)
        JetSmearImpact_sig = (1-JetSmearError_sig)
        MuScaleImpact_MC = ((1-MuScaleUpError_MC)+(1-MuScaleDownError_MC)/2)
        JetScaleImpact_MC = ((1-JetScaleUpError_MC)+(1-JetScaleDownError_MC)/2)
        MuSmearImpact_MC = (1-MuSmearError_MC)
        JetSmearImpact_MC = (1-JetSmearError_MC)                          





Uncertainties.write("\\textbf{Background Normalization} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Background Shape} & \\textbf{varies} & \\textbf{-} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Scale} & \\textbf{4} & \\textbf{"+str(JetScaleImpact_sig)+"} & \\textbf{"+str(JetScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Jet Energy Resolution} & \\textbf{varies} & \\textbf{"+str(JetSmearImpact_sig)+"} & \\textbf{"+str(JetSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Energy Scale} & \\textbf{1} & \\textbf{"+str(MuScaleImpact_sig)+"} & \\textbf{"+str(MuScaleImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Energy Resolution} & \\textbf{varies} & \\textbf{"+str(MuSmearImpact_sig)+"} & \\textbf{"+str(MuSmearImpact_MC)+"}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Muon Reco/ID/Iso} & \\textbf{1} & \\textbf{?} & \\textbf{?}\\\\\n")
Uncertainties.write("\\hline\n")
Uncertainties.write("\\textbf{Integrated Luminosity} & \\textbf{2.2} & \\textbf{2.2} & \\textbf{-}\\\\\n")
Uncertainties.write("\\hline\n")




Rates.write("\\end{frame}")
Rates.close()

Uncertainties.write("\\end{frame}")
Uncertainties.close()
