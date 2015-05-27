from __future__ import print_function
import os
import sys
import math
import subprocess
End=31
Suffix="1p0"
for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print (str(x)+'};',end='')
    else:
        print (str(x)+',',end='')



print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('Obs'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('Obs'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('MinOne'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('MinOne'+str(x)+"_"+Suffix+',',end='')


print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('Center'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('Center'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('MinTwo'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('MinTwo'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('PlusOne'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('PlusOne'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')


for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('PlusTwo'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('PlusTwo'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')

for i in range(End):
    x = 300+100*i
    if i == (End-1):
        print ('ThCS'+str(x)+"_"+Suffix+'};',end='')
    else:
        print ('ThCS'+str(x)+"_"+Suffix+',',end='')

print ('\n',end='')
