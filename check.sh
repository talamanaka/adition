#!/bin/bash
file="$1"
scan="scan.txt"
cp $file $scan
count=$(cat $scan |wc -l)
ii=1
while IFS= read line
do
        # display $line or do somthing with $line
	
        y=$( curl -s -k "$line" | egrep -c containers )
        if [ "$y" = "1" ]; then
        echo "$line" >> found
        echo  $count "/" $ii "" "$line"
        
        
        fi
        ((ii++))
        sed -i 1d $scan
done <"$scan"
