############################################################################
# This script counts the number of events in a given folder of MC
# It makes use of FileList.txt
# In a text file, make a list of each folder you want to count, one per line
# Then run by typing "sh EventCounter.sh {Text file name}"
#############################################################################

cut -f1 -d',' $1 > SigType.txt
cut -f8 -d',' $1 > Folders.txt
# ^ Here I make text files out of the 1st and 8th columns of the input csv file

N=`wc SigType.txt | gawk '(NR==1){print $1}'`
echo $N

mkdir LogFiles

for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' Folders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`

    cmsLs $CurrentFolder  | gawk '{print $5}' > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    # ^ Here I take only files matching the current Signature and put them in a text file
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`

    mkdir LogFiles/$CurrentSig

    for ((j = 1; j <=M; j++))
    do
	CurrentFile=`gawk '(NR=='$j'){print $1}' CurrentFiles.txt`
	
	cat BlankScript.sh | sed -e 's,File=PLACEHOLDER,File='$CurrentFile',g
s,PLACE_TWO,/afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/'$CurrentSig'/Log_'$j'.txt,g' > /afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/$CurrentSig/Script_$j.sh
	# ^ This replaces the placeholders in BlankScript.sh

	bsub -o /tmp/dnash/Log/ -q 1nh -J Count < /afs/cern.ch/user/d/dnash/CMSSW_5_0_0/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/$CurrentSig/Script_$j.sh
    done
done

bjobs > check.txt
NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
until [ $NumRemaining -lt 1 ]
    do
        echo $NumRemaining jobs left
	rm check.txt
	sleep 300
	bjobs | grep Count > check.txt
	NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
    done
# ^ This until loop waits until all the jobs are done


for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' Folders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`
    cmsLs $CurrentFolder  | gawk '{print $5}' > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`
    Total=0
    for ((j = 1; j <=M; j++))
    do
	New=`gawk '(NR==1){print $1}' LogFiles/$CurrentSig/Log_$j.txt`

	if [[ "$New" =~ ^[0-9]+$ ]]
	then
	    let Total=$Total+$New	    
	else
	    echo Log_$j of $CurrentSig had no events > ErrorLog.txt
	fi
	# ^ This if/else statement checks for empty output files
    done
    echo -n "$CurrentSig = "
    echo $Total >> EventCountResults_3.txt
done
