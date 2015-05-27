import os
import sys
from ROOT import *
import csv

table=[]

csvfile = sys.argv[1]
csvfile = open(csvfile,'r')

for row in csv.reader(csvfile):
	if len(row) == 0:
		continue
	if row[0][0]=='#':
		continue
	table.append(row)
for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=(table[r][c])
table2= map(list,zip(*table[1:]))
for x in range(0,len(table2)):
	exec (table[0][x]+'='+`table2[x]`)	
for x in range(0,len(HLTBit)):
	HLTBit[x]=int(HLTBit[x])
	SigOrBG[x]=int(SigOrBG[x])

castors = CastorDirectory

for c in castors:
	files = os.popen('nsls '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append('rfio://'+c+'/'+x.replace('\n',''))
	for x in cfiles:
		print x
		f = TFile.Open(x)
		t = f.Get("rootTupleTree/tree")
		t.GetEntries()


