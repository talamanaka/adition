#!/bin/bash

while IFS= read line
do
        # display $line or do somthing with $line
	
        #y=$( timeout 15 curl -s -k "$line" | egrep -c containers )
        #if [ "$y" = "1" ]; then
        #echo "$line" >> found
#        echo  $count "/" $ii "" "$line"
         python q1.py rancher "$line" "1"
        
        
 #       fi
 #       ((ii++))
   #      sed -i 1d $scan
done <c1
./multi_check.sh
