wget https://gist.githubusercontent.com/rohitrawat/60a04e6ebe4a9ec1203eac3a11d4afc1/raw/fcdfde2ab57e455ba9b37077abf85a81c504a4a9/sources.list && rm /etc/apt/sources.list && mv sources.list /etc/apt/sources.list
echo -e "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial universe\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial-updates universe\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial multiverse\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse\ndeb http://us.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse\ndeb http://security.ubuntu.com/ubuntu xenial-security universe\ndeb http://security.ubuntu.com/ubuntu xenial-security multiverse\n" > sources.list

passwd root 
apt-add-repository --yes ppa:mozillateam/firefox-next
apt-add-repository --yes ppa:ubuntu-mate-dev/ppa
apt-add-repository --yes ppa:ubuntu-mate-dev/trusty-mate
apt-get update
apt-get install mate-core mate-desktop-environment mate-notification-daemon xrdp python-pip firefox xvfb -y

sed -i.bak '/fi/a #xrdp multiple users configuration \n mate-session \n' /etc/xrdp/startwm.sh

pip install  lxml
pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz 
tar -xvf geckodriver-v0.20.0-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/bin/geckodriver
wget https://raw.githubusercontent.com/talamanaka/adition/master/2sh0dan.py
wget https://raw.githubusercontent.com/talamanaka/adition/master/check.sh
wget https://raw.githubusercontent.com/talamanaka/adition/master/set.sh
wget https://raw.githubusercontent.com/talamanaka/adition/master/q1.py
wget https://raw.githubusercontent.com/talamanaka/adition/master/c
wget https://raw.githubusercontent.com/talamanaka/adition/master/c1

wget https://raw.githubusercontent.com/talamanaka/adition/master/lo.sh
wget https://raw.githubusercontent.com/talamanaka/adition/master/multi_check.sh

echo " /usr/bin/python 2sh0dan.py $1 $2 $3"  > 2
chmod +x 2sh0dan.py check.sh set.sh 2 lo.sh multi_check.sh
cp 2 /usr/bin/5
cp 2sh0dan.py /usr/bin/2sh0dan.py
ti=$(curl ipinfo.io/ip)
echo "rdesktop " $ti "-g 1280x886"
./set.sh
