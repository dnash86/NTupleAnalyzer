import os
import sys


a=sys.argv


for n in range(len(a)):

    if a[n] =='-i':
        FileIn = a[n+1]


Lines=os.popen('cat '+FileIn).readlines()

Mass = []
Mcut = []
STcut = []
for line in Lines:
    if "Mass = " in line:
        Mass.append(line.split('= ')[1].replace('\n',''))
    if "ST" in line:
        Mcut.append(line.split('> ')[1].split(')')[0])
        STcut.append(line.split('> ')[2].split(')')[0])



for i in range(len(Mass)):
    print "{"+str(Mass[i])+"} & {"+str(Mcut[i])+"} & {"+str(STcut[i])+"}\\\\"
    print "\\hline"
