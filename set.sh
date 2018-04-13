#!/bin/bash
# This script will test if you have given a leap year or not.

echo "Type the username shodan.io , followed by [ENTER]:"
read user
sed -i "s/username+/$user/" 2sh0dan.py
echo $user\n
echo "Type the password shodan.io , followed by [ENTER]:"
read pass
sed -i "s/pass+/$pass/" 2sh0dan.py
echo $pass\n
ti=$(curl ipinfo.io/ip)

clear  
echo "         rdesktop " $ti "-g 1280x886  "



