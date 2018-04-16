#!/bin/bash
mkdir -p output
mkdir -p e_output

ls |grep shodan- >> res
while IFS= read line
do
        # display $line or do somthing with $line
        y=$(cat $line | wc -l)
        #y=$( timeout 15 curl -s -k "$line" | egrep -c containers )
        if [ "$y" == 0 ]; then
        mv $line e_output
        else
        mv $line output
        #echo "$line" >> found
        cc=$(echo $line |cut -d "-" -f 2)
        printf  $cc
        echo  " "$y 
         #python q1.py rancher "$line" "1"
        
        
       fi
 #       ((ii++))
   #      sed -i 1d $scan
done <res

rm res
