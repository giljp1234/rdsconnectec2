#!bin/bash
#root

sudo -i 
cd /var/www/html
vim index.html


#ec2-user

rm /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime

sudo echo "ZONE="Asia/Seoul" 
UTC=true /etc/sysconfig/clock"


#### httpd apache

sudo yum update -y

sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd


###mysql 
## https://dev-kwon.tistory.com/78

sudo yum install wget


sudo wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo yum -y install https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
sudo yum -y install mysql-community-server
-------------------------------------------------------


sudo systemctl enable mysqld
sudo systemctl start mysqld

###Pip

sudo yum install pip
sudo python3 -m pip install pymysql
pip install mysql-connector-python

python3 rds.py




