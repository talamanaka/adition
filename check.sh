#!/bin/bash
file="$1"
scan="scan.txt"
cp $file $scan
count=$(cat $scan |wc -l)
ii=1
while IFS= read line
do
        # display $line or do somthing with $line
	
        y=$( timeout 15 curl -s -k "$line" | egrep -c containers )
        if [ "$y" = "1" ]; then
        echo "$line" >> found
        echo  $count "/" $ii "" "$line"
        
        
        fi
        ((ii++))
        sed -i 1d $scan
done <"$scan"
fin=$(curl -s --upload-file found https://transfer.sh/found;echo)
echo -e "\n"
echo "     URL: "$fin
