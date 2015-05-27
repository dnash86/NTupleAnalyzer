import os
import sys
import math
import numpy


CentralFile='CentralValues_125GeVCut.txt'

def collectcentralvalues(directory,bgstodo):
    CurrentFile = os.popen('cat '+directory+'/'+CentralFile).readlines()
    BackgroundValues=[]
    SignalValues=[]
    for i in range(len(CurrentFile)):
        Background=0
        #for bg_i in [1,2,3,4,5]:
        for bg_i in bgstodo:
            #print CurrentFile[i].replace('\n','').split(',')[bg_i]
            Background += float(CurrentFile[i].replace('\n','').split(',')[bg_i])
        Signal = float(CurrentFile[i].replace('\n','').split(',')[-1])
        BackgroundValues.append(Background)
        SignalValues.append(Signal)
    return [BackgroundValues,SignalValues]


def GetReNormalizations(pdftype,directory):

    SignalFile=os.popen('cat '+directory+'/'+CentralFile).readlines()
    SignalValues=[]
    #print directory
    #print CentralFile
    for i in range(len(SignalFile)):
        Signal = float(SignalFile[i].replace('\n','').split(',')[-1])
        SignalValues.append(Signal)

    FileList = os.popen('ls '+directory+'/*'+pdftype+'*.txt').readlines()
    #print SignalValues
    
    SignalRenormalizations=[]
    for i in range(len(FileList)):
        SignalRenormalizations.append([])
        CurrentFile = os.popen('cat '+FileList[i].replace('\n','')).readlines()
        for j in range(len(CurrentFile)):
            ThisSignal = float(CurrentFile[j].replace('\n','').split(',')[-1])
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
            #print CurrentFile[i].split(',')
            #for bg_i in [1,2,3,4,5]:
            for bg_i in bgstodo:
                Background += float(CurrentFile[i].replace('\n','').split(',')[bg_i])
            Signal = float(CurrentFile[i].replace('\n','').split(',')[-1])

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

    #print [BackgroundValuesLow,BackgroundValuesHigh,SignalValuesLow,SignalValuesHigh]
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
            Signal = float(CurrentFile[i].replace('\n','').split(',')[-1])
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
    
    #print centralvalues
    #print nnpdfvalues
    #print mstwvalues
    #print cteqvalues

    for i in range(len(centralvalues[0])):
        cteqbottom = cteqvalues[0][i]
        cteqtop = cteqvalues[1][i]
        averagecteq = (cteqbottom+cteqtop)/2.
        
        cteqvalues[0][i] = averagecteq + ( (cteqbottom-averagecteq) /1.645)
        cteqvalues[1][i] = averagecteq + ( (cteqtop-averagecteq) /1.645)

        #print "Minima = "+str([nnpdfvalues[0][i],mstwvalues[0][i],cteqvalues[0][i]])
        #print "Maxima = "+str([nnpdfvalues[1][i],mstwvalues[1][i],cteqvalues[1][i]])
        #print "Central = "+str(centralvalues[0][i])
        MinVariation = min([nnpdfvalues[0][i],mstwvalues[0][i],cteqvalues[0][i]])
        MaxVariation = max([nnpdfvalues[1][i],mstwvalues[1][i],cteqvalues[1][i]])
        if centralvalues[0][i]!=0:
            #nnpdf_bg_variation_up = (nnpdfvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            #nnpdf_bg_variation_down = (-nnpdfvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]
            
            #cteq_bg_variation_up = (cteqvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            #cteq_bg_variation_down = (-cteqvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]
            
            #print str(nnpdfvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(nnpdfvalues[1][i])
            #print str(cteqvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(cteqvalues[1][i])
            #print str(mstwvalues[0][i])+", "+str(centralvalues[0][i])+", "+str(mstwvalues[1][i])
       
            #cteq_bg_variation_up /= 1.645
            #cteq_bg_variation_down /= 1.645
            
            #mstw_bg_variation_up = (mstwvalues[1][i]-centralvalues[0][i])/centralvalues[0][i]
            #mstw_bg_variation_down = (-mstwvalues[0][i]+centralvalues[0][i])/centralvalues[0][i]

            bg_variation_up = (MaxVariation-centralvalues[0][i])/centralvalues[0][i]
            bg_variation_down = (-MinVariation+centralvalues[0][i])/centralvalues[0][i]

        else:
            #nnpdf_bg_variation_up = 0
            #nnpdf_bg_variation_down =0 
            
            #cteq_bg_variation_up = 0
            #cteq_bg_variation_down =0 
            
            
            #mstw_bg_variation_up = 0
            #mstw_bg_variation_down = 0
            bg_variation_up = 0
            bg_variation_down = 0
   
        #logfile.write(str(nnpdf_bg_variation_down)+','+str(nnpdf_bg_variation_up)+','+str(cteq_bg_variation_down)+','+str(cteq_bg_variation_up)+','+str(mstw_bg_variation_down)+','+str(mstw_bg_variation_up)+'\n')
        logfile.write(str(bg_variation_down)+','+str(bg_variation_up)+'\n')


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

    print centralvalues[1]
    for i in range(len(centralvalues[1])):

        cteqbottom = cteqvalues[2][i]
        cteqtop = cteqvalues[3][i]
        averagecteq = (cteqbottom+cteqtop)/2.
        
        cteqvalues[2][i] = averagecteq + ( (cteqbottom-averagecteq) /1.645)
        cteqvalues[3][i] = averagecteq + ( (cteqtop-averagecteq) /1.645)

        MinVariation = min([nnpdfvalues[2][i],mstwvalues[2][i],cteqvalues[2][i]])
        MaxVariation = max([nnpdfvalues[3][i],mstwvalues[3][i],cteqvalues[3][i]])

        print "Minima = "+str([nnpdfvalues[2][i],mstwvalues[2][i],cteqvalues[2][i]])
        print "Maxima = "+str([nnpdfvalues[3][i],mstwvalues[3][i],cteqvalues[3][i]])
        print "Central = "+str(centralvalues[1][i])
        sig_variation_up = (MaxVariation-centralvalues[1][i])/centralvalues[1][i]
        sig_variation_down = (-MinVariation+centralvalues[1][i])/centralvalues[1][i]

   
        logfile.write(str(sig_variation_down)+','+str(sig_variation_up)+'\n')

    logfile.close()
   

    nnpdfrenorms=GetReNormalizations('NNPDF',PreselDir)
    cteqrenorms=GetReNormalizations('CTEQ',PreselDir)
    mstwrenorms=GetReNormalizations('MSTW',PreselDir)

    nnpdfvalues=collectwithrenormalizations('NNPDF',MainDir,nnpdfrenorms)
    cteqvalues=collectwithrenormalizations('CTEQ',MainDir,cteqrenorms)
    mstwvalues=collectwithrenormalizations('MSTW',MainDir,mstwrenorms)

    centralvalues=collectcentralvalues(MainDir,[2])

    logfile = open('Ele_SignalAcceptance_PDF.txt','w')

     
     
    for i in range(len(centralvalues[1])):
        cteqbottom = cteqvalues[2][i]
        cteqtop = cteqvalues[3][i]
        averagecteq = (cteqbottom+cteqtop)/2.
        
        cteqvalues[2][i] = averagecteq + ( (cteqbottom-averagecteq) /1.645)
        cteqvalues[1][i] = averagecteq + ( (cteqtop-averagecteq) /1.645)

        MinVariation = min([nnpdfvalues[2][i],mstwvalues[2][i],cteqvalues[2][i]])
        MaxVariation = max([nnpdfvalues[3][i],mstwvalues[3][i],cteqvalues[3][i]])


        sig_variation_up = (MaxVariation-centralvalues[1][i])/centralvalues[1][i]
        sig_variation_down = (-MinVariation+centralvalues[1][i])/centralvalues[1][i]

   
        logfile.write(str(sig_variation_down)+','+str(sig_variation_up)+'\n')


    logfile.close()



main()
