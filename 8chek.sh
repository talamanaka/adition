#!/bin/bash



while IFS= read line
do

        echo  " "$line 
        python q1.py rancher "$line" "1"

done < c
