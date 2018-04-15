#!/bin/bash

while IFS= read line
do
        # display $line or do somthing with $line
	
        #y=$( timeout 15 curl -s -k "$line" | egrep -c containers )
        #if [ "$y" = "1" ]; then
        #echo "$line" >> found
#        echo  $count "/" $ii "" "$line"
        echo "$line"
        
        
 #       fi
 #       ((ii++))
   #      sed -i 1d $scan
done <c
