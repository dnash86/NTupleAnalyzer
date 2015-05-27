import os
import sys


these=os.popen("cat Rates_2012_ele.tex").readlines()

theseothers = os.popen("cat SignalTable.csv").readlines()
if False:
    for line in these:
        if '\hline' not in line:
            print line.replace('&',',').replace('\n','')
    

if True:
    for line in theseothers:
        print line.replace(',','&').replace('"','').replace('\n','')+'\\\\'
    


