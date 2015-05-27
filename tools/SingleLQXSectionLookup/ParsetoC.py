import sys
import os
import csv

csvfile = open("CrossSections[pb].csv",'r')


Info=[]
Xsection=[]
EventCount=[]

for row in csv.reader(csvfile):
    Info.append(row[0])
    Xsection.append(row[1])
    EventCount.append(row[2])


h = open('GetCSFunction.h','w')

h.write('double GetCS(int mass, double lambda)\n{\ndouble CS = 0.0;\n\n')

for i in range(len(Info)):
    Mass = str(int(Info[i].split(",")[0].split("=")[1].split("GeV")[0]))
    Lambda_OnesPlace = Info[i].split(",")[1].split("L-")[1].split("_M")[0].split("p")[0]
    Lambda_DecimalPlace = Info[i].split(",")[1].split("L-")[1].split("_M")[0].split("p")[1]
    Lookup = "if (mass == "+Mass+" && lambda == "+Lambda_OnesPlace+"."+Lambda_DecimalPlace +") {CS = " + Xsection[i]+";Count = "+EventCount[i]+";}"
    h.write(Lookup+"\n")
    print Info[i].split(",")[1].split("_GeV")[0].replace(" ","")
    
h.write('\n\nreturn CS;\n\n}\n\n')
h.close()
