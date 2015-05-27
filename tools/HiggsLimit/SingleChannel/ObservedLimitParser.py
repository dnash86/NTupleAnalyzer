import os
import sys

f = open('ObservedLimitLog.txt','r')

types = []
Limits = []
count = 0
for line in f:
	if 'Limit:' in line:
		count += 1
		if count == 2:
			Limits.append(line)
			count = 0
	
limitfigs = []
for limit in Limits:
	limit = (limit.split()[3])
	limitfigs.append(limit)

length = len(limitfigs)
length = length/2

mumu = limitfigs[0:length]
munu = limitfigs[length:]

X_th=[ 3.47, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00215,.000732]

for x in range(len(mumu)):

	mumu[x] = str(float(mumu[x])*X_th[x])
	munu[x] = str(float(munu[x])*0.5*X_th[x])

mumu = str(mumu).replace('\'','')
mumu = mumu.replace('[','{')
mumu = mumu.replace(']','}')

munu = str(munu).replace('\'','')
munu = munu.replace('[','{')
munu = munu.replace(']','}')


print '\nObserved limits for MuMu:\n'

print ' Double_t xsUp_observed['+str(length)+'] = '+mumu+' ; ' 


print '\n\nObserved limits for MuNu:\n'

print ' Double_t xsUp_observed['+str(length)+'] = '+munu+' ; ' 

print '\n\n'
