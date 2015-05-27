wc FileList.txt > TempNumber.txt
N=`gawk '(NR==1){print $1}' TempNumber.txt` 
rm TempNumber.txt

for ((i = 1; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' FileList.txt`
    nsls $CurrentFolder > TempList.txt
    wc TempList.txt > TempNumber.txt
    M=`gawk '(NR==1){print $1}' TempNumber.txt` 
    Total=0
    mkdir TestScripts/Folder_$i
    for ((j = 1; j <=M; j++))
    do
	#echo File Number $j out of $M, Folder Number $i out of $N
	CurrentFile=`gawk '(NR=='$j'){print $1}' TempList.txt`
	#rfcp $CurrentFolder/$CurrentFile /tmp/dnash/Testing/CMSSW_4_2_8/data/$CurrentFile
	#NewNumber=`sh Script.sh /tmp/dnash/Testing/CMSSW_4_2_8/data/$CurrentFile`
	#let Total=$Total+$NewNumber
	#echo Running total of $CurrentFolder: $Total
	cat BlankScript.sh | sed -e 's,File=PLACEHOLDER,File='$CurrentFolder'/'$CurrentFile',g
s,PLACEHOLDER_TWO,/afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/TestScripts/Folder_'$i'/File_'$j'.sh,g' > /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/TestScripts/Folder_$i/Log_$j.txt
	bsub -q 1nh -J Count < /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/TestScripts/Folder_$i/File_$j.sh
    done
    #echo $Total > EventCount_$CurrentFolder.txt
done