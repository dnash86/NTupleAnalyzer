


cut -f1 -d',' $1 > SigType.txt
cut -f8 -d',' $1 > CastorFolders.txt

N=`wc SigType.txt | gawk '(NR==1){print $1}'`
#let N=$N+1

Home=`pwd`

mkdir LogFiles

for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' CastorFolders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`
    nsls $CurrentFolder > TotalFolderContents_$i.txt
    grep $CurrentSig TotalFolderContents_$i.txt > CurrentFiles_$i.txt
    echo $CurrentSig >> Sigs.txt
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`
    mkdir LogFiles/$CurrentSig
    for ((j = 1; j <=M; j++))
    do
	CurrentFile=`gawk '(NR=='$j'){print $1}' CurrentFiles.txt`
	cat BlankScript.sh | sed -e 's,File=PLACEHOLDER,File='$CurrentFolder'/'$CurrentFile',g
s,PLACEHOLDER_TWO,/afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/'$CurrentSig'/Log_'$j'.txt,g' > /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/$CurrentSig/Script_$j.sh
	# ^ This replaces the placeholders in BlankScript.sh

	#bsub -q 1nh -J Count < /afs/cern.ch/user/d/dnash/CMSSW_4_2_8/src/NTupleAnalyzer/tools/EventCountCheck/LogFiles/Folder_$i/Script_$j.sh
    done
done

bjobs > check.txt
NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
until [ $NumRemaining -lt 1 ]
    do
        echo $NumRemaining jobs left
	rm check1.txt
	rm check2.txt
	sleep 300
	bjobs > check.txt
	NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
    done
# ^ This until loop waits until all the jobs are done


for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' CastorFolders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`
    nsls $CurrentFolder > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`
    Total=0
    for ((j = 1; j <=M; j++))
    do
	New=`gawk '(NR==1){print $1}' LogFiles/$CurrentSig/Log_$j.txt`
	let Total=$Total+$New
    done
    echo $Total >> EventCountResults.txt
done
