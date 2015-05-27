#fileinput=sys.argv[1] 

import os
import sys

jsons = []
#jsons = (os.popen('ls *JSON*.txt')).readlines()
jsons.append(sys.argv[1])
outputfile=sys.argv[2]
j = []
for x in jsons:
	x = x.replace('\n','')
	j.append(x)
jsons = j

#print jsons

contents = ''
for f in jsons:
	fc = open(f,'r')
	for line in fc:
		contents = contents + ((line.replace('\n','')).replace('}','')).replace('{','')

contents = contents.replace('":','')
contents = contents.replace(':','')
contents = contents.replace('"','\n')
contents = contents.replace(']],',']]')
#print contents

isfile = os.popen('ls JSONFilterFunction.h').readlines()

if len( isfile ) > 2:
	os.system('rm JSONFilterFunction.h')
	
h = open(outputfile,'w')

h.write('bool PassFilter(int irun, int ils)\n{\nbool keepevent = false;\n\n')

sets = contents.split('\n')

for x in sets:
	if len(x)<2:
		continue
	run =  (x.split('[[') [0])
	lumis = (((((x.split('[[') [-1])).replace(']','')).replace('[','')).replace(' ','')).split(',')
	print 'Parsing run:  ' + run
	print lumis

	for n in range(len(lumis)/2):
		h.write('if ((irun == ' +run+')&&(ils >= '+lumis[2*n]+')&&(ils <= '+lumis[2*n+1]+')) keepevent = true;\n' )
		
h.write('\n\nreturn keepevent;\n\n}\n\n')
#	print 	x.split('[[')
#	print run
print 'JSON Filtering function written to JSONFilterFunction.h. Please move this file to the main NTupleAnalyzerV2 directory'
