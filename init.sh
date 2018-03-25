apt-add-repository ppa:mozillateam/firefox-next
apt-get update &&  apt-get install mate-core mate-desktop-environment mate-notification-daemon xrdp python-pip firefox xvfb -y

sed -i.bak '/fi/a #xrdp multiple users configuration \n mate-session \n' /etc/xrdp/startwm.sh


pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz 
tar -xvf geckodriver-v0.20.0-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/bin/geckodriver
