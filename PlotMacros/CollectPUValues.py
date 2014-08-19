import os
import sys
import math


CentralFile='CentralValues_125GeVCut.txt'

def collectcentralvalues(directory,bgstodo):
    CurrentFile = os.popen('cat '+directory+'/'+CentralFile).readlines()
    BackgroundValues=[]
    SignalValues=[]
    for i in range(len(CurrentFile)):
        Background=0
        #for bg_i in [1,2,3,4,5]:
        for bg_i in bgstodo:
            print CurrentFile[i].replace('\n','').split(',')[bg_i]
            Background += float(CurrentFile[i].replace('\n','').split(',')[bg_i])
        Signal = float(CurrentFile[i].replace('\n','').split(',')[8])
        BackgroundValues.append(Background)
        SignalValues.append(Signal)
    return [BackgroundValues,SignalValues]


def GetReNormalizations(pdftype,directory):

    SignalFile=os.popen('cat '+directory+'/'+CentralFile).readlines()
    SignalValues=[]
    for i in range(len(SignalFile)):
        Signal = float(SignalFile[i].replace('\n','').split(',')[7])
        SignalValues.append(Signal)

    FileList = os.popen('ls '+directory+'/*'+pdftype+'*.txt').readlines()
    
    SignalRenormalizations=[]
    for i in range(len(FileList)):
        SignalRenormalizations.append([])
        CurrentFile = os.popen('cat '+FileList[i].replace('\n','')).readlines()
        for j in range(len(CurrentFile)):
            ThisSignal = float(CurrentFile[j].replace('\n','').split(',')[7])
            SignalRenormalizations[i].append(SignalValues[j]/ThisSignal)

    return SignalRenormalizations
            

    


def collect(pdftype,directory,bgstodo):
    FileList = os.popen('ls '+directory+'/*'+pdftype+'*.txt').readlines()
    print directory
    SmallestBackgroundEventCount = [99999.]*113
    SmallestSignalEventCount = [99999.]*113
    LargestBackgroundEventCount = [0]*113
    LargestSignalEventCount = [0]*113
    BackgroundValuesHigh=[]
    BackgroundValuesLow=[]
    SignalValuesHigh=[]
    SignalValuesLow=[]
    for line in FileList:
        #print line
        CurrentFile = os.popen('cat '+line.replace('\n','')).readlines()
        #print CurrentFile
        for i in range(len(CurrentFile)):
            Background=0
            #for bg_i in [1,2,3,4,5]:
            for bg_i in bgstodo:
                Background += float(CurrentFile[i].replace('\n','').split(',')[bg_i])
            Signal = float(CurrentFile[i].replace('\n','').split(',')[8])

            if Background > LargestBackgroundEventCount[i]:
                #print LargestBackgroundEventCount[i]
                LargestBackgroundEventCount[i]=Background
            if Signal > LargestSignalEventCount[i]:
                LargestSignalEventCount[i]=Signal

                #print Background + ", " + str(SmallestBackgroundEventCount[i])
            if Background < SmallestBackgroundEventCount[i]:
                SmallestBackgroundEventCount[i]=Background
            if Signal < SmallestSignalEventCount[i]:
                SmallestSignalEventCount[i]=Signal
    for i in range(len(SmallestBackgroundEventCount)):
        #print "Range = " +str(SmallestBackgroundEventCount[i])+" - " +str(LargestBackgroundEventCount[i])
        BackgroundValuesHigh.append(LargestBackgroundEventCount[i])
        BackgroundValuesLow.append(SmallestBackgroundEventCount[i])
    for i in range(len(SmallestSignalEventCount)):
        #print "Range = " +str(SmallestSignalEventCount[i])+" - " +str(LargestSignalEventCount[i])
        SignalValuesHigh.append(LargestSignalEventCount[i])
        SignalValuesLow.append(SmallestSignalEventCount[i])

    return [BackgroundValuesLow,BackgroundValuesHigh,SignalValuesLow,SignalValuesHigh]



def collectwithrenormalizations(pdftype,directory,renorms):
    #print directory
    #print pdftype
    FileList = os.popen('ls '+directory+'/*'+pdftype+'*.txt').readlines()
    SmallestBackgroundEventCount = [99999.]*113
    SmallestSignalEventCount = [99999.]*113
    LargestBackgroundEventCount = [0]*113
    LargestSignalEventCount = [0]*113
    BackgroundValuesHigh=[]
    BackgroundValuesLow=[]
    SignalValuesHigh=[]
    SignalValuesLow=[]
    #print FileList
    for list_i in range(len(FileList)):
        
        CurrentFile = os.popen('cat '+FileList[list_i].replace('\n','')).readlines()
        #print CurrentFile
        for i in range(len(CurrentFile)):
            Background=0
            #print CurrentFile[i]
            for bg_i in [1,2,3,4,5]:
                Background += float(CurrentFile[i].replace('\n','').split(',')[bg_i])
            Signal = float(CurrentFile[i].replace('\n','').split(',')[7])
            #Renormalizing to the presel normalization
            Signal *= renorms[list_i][i]

            if Background > LargestBackgroundEventCount[i]:
                #print LargestBackgroundEventCount[i]
                LargestBackgroundEventCount[i]=Background
            if Signal > LargestSignalEventCount[i]:
                LargestSignalEventCount[i]=Signal

                #print Background + ", " + str(SmallestBackgroundEventCount[i])
            if Background < SmallestBackgroundEventCount[i]:
                SmallestBackgroundEventCount[i]=Background
            if Signal < SmallestSignalEventCount[i]:
                SmallestSignalEventCount[i]=Signal
    for i in range(len(SmallestBackgroundEventCount)):
        #print "Range = " +str(SmallestBackgroundEventCount[i])+" - " +str(LargestBackgroundEventCount[i])
        BackgroundValuesHigh.append(LargestBackgroundEventCount[i])
        BackgroundValuesLow.append(SmallestBackgroundEventCount[i])
    for i in range(len(SmallestSignalEventCount)):
        #print "Range = " +str(SmallestSignalEventCount[i])+" - " +str(LargestSignalEventCount[i])
        SignalValuesHigh.append(LargestSignalEventCount[i])
        SignalValuesLow.append(SmallestSignalEventCount[i])

    return [BackgroundValuesLow,BackgroundValuesHigh,SignalValuesLow,SignalValuesHigh]


def DoBackgrounds(bgs,filename):
    MainDir='ParallelFiles2'

    nnpdfvalues=collect('NNPDF',MainDir,bgs)
    cteqvalues=collect('CTEQ',MainDir,bgs)
    mstwvalues=collect('MSTW',MainDir,bgs)
    centralvalues=collectcentralvalues(MainDir,bgs)

    logfile = open(filename,'w')
    #sigfile = open('Mu_Signal_PDF.txt','w')
    
    for i in range(len(centralvalues[0])):
        if centralvalues[0][i]!=0:
            nnpdf_bg_variation_up = (nnpdfvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            nnpdf_bg_variation_down = (-nnpdfvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]
            
            cteq_bg_variation_up = (cteqvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            cteq_bg_variation_down = (-cteqvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]
            
            print str(nnpdfvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(nnpdfvalues[1][i])
            print str(cteqvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(cteqvalues[1][i])
            print str(mstwvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(mstwvalues[1][i])
       
            cteq_bg_variation_up /= 1.645
            cteq_bg_variation_down /= 1.645
            
            mstw_bg_variation_up = (mstwvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            mstw_bg_variation_down = (-mstwvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]
        else:
            nnpdf_bg_variation_up = 0
            nnpdf_bg_variation_down =0 
            
            cteq_bg_variation_up = 0
            cteq_bg_variation_down =0 
            
            
            mstw_bg_variation_up = 0
            mstw_bg_variation_down = 0
   
        logfile.write(str(nnpdf_bg_variation_down)+','+str(nnpdf_bg_variation_up)+','+str(cteq_bg_variation_down)+','+str(cteq_bg_variation_up)+','+str(mstw_bg_variation_down)+','+str(mstw_bg_variation_up)+'\n')


    logfile.close()

def main():
    MainDir='ParallelFiles2'
    
    


    #logfile = open('Mu_PDF.txt','w')
    #sigfile = open('Mu_Signal_PDF.txt','w')
    
    DoBackgrounds([2],'Ele_PDF_Z.txt')
    DoBackgrounds([3],'Ele_PDF_DiBoson.txt')
    DoBackgrounds([4],'Ele_PDF_SingleTop.txt')
    DoBackgrounds([5],'Ele_PDF_W.txt')

    PreselDir='ParallelFiles2Presel'


    
    nnpdfvalues=collect('NNPDF',PreselDir,[2])
    cteqvalues=collect('CTEQ',PreselDir,[2])
    mstwvalues=collect('MSTW',PreselDir,[2])
    centralvalues=collectcentralvalues(PreselDir,[2])


    logfile = open('Ele_SignalNormalization_PDF.txt','w')

    #print centralvalues[1]
    #print cteqvalues[3] 
    #print cteqvalues[2] 
    for i in range(len(centralvalues[1])):

        nnpdf_sig_variation_up = (nnpdfvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        nnpdf_sig_variation_down = (-nnpdfvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]

        cteq_sig_variation_up = (cteqvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        cteq_sig_variation_down = (-cteqvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]
       
        print str(nnpdfvalues[2][i])+", "+str(centralvalues[1][i])+", "+str(nnpdfvalues[3][i])
        print str(cteqvalues[2][i])+", "+str(centralvalues[1][i])+", "+str(cteqvalues[3][i])
        print str(mstwvalues[2][i])+", "+str(centralvalues[1][i])+", "+str(mstwvalues[3][i])

        cteq_sig_variation_up /= 1.645
        cteq_sig_variation_down /= 1.645
     
        mstw_sig_variation_up = (mstwvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        mstw_sig_variation_down = (-mstwvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]
   
        logfile.write(str(nnpdf_sig_variation_down)+','+str(nnpdf_sig_variation_up)+','+str(cteq_sig_variation_down)+','+str(cteq_sig_variation_up)+','+str(mstw_sig_variation_down)+','+str(mstw_sig_variation_up)+'\n')


    logfile.close()
   

    nnpdfrenorms=GetReNormalizations('NNPDF',PreselDir)
    cteqrenorms=GetReNormalizations('CTEQ',PreselDir)
    mstwrenorms=GetReNormalizations('MSTW',PreselDir)

    nnpdfvalues=collectwithrenormalizations('NNPDF',MainDir,nnpdfrenorms)
    cteqvalues=collectwithrenormalizations('CTEQ',MainDir,cteqrenorms)
    mstwvalues=collectwithrenormalizations('MSTW',MainDir,mstwrenorms)


    logfile = open('Ele_SignalAcceptance_PDF.txt','w')

     
     
    for i in range(len(centralvalues[1])):
        nnpdf_sig_variation_up = (nnpdfvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        nnpdf_sig_variation_down = (-nnpdfvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]

        cteq_sig_variation_up = (cteqvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        cteq_sig_variation_down = (-cteqvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]
       
        cteq_sig_variation_up /= 1.645
        cteq_sig_variation_down /= 1.645
     
        mstw_sig_variation_up = (mstwvalues[3][i]-centralvalues[1][i])/centralvalues[1][i]
        mstw_sig_variation_down = (-mstwvalues[2][i]+centralvalues[1][i])/centralvalues[1][i]
   
        logfile.write(str(nnpdf_sig_variation_down)+','+str(nnpdf_sig_variation_up)+','+str(cteq_sig_variation_down)+','+str(cteq_sig_variation_up)+','+str(mstw_sig_variation_down)+','+str(mstw_sig_variation_up)+'\n')


    logfile.close()



main()
