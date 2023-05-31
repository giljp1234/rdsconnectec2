rm /etc/localtime

ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime

sudo echo "ZONE="Asia/Seoul" 
UTC=true /etc/sysconfig/clock"


###mysql 
## https://dev-kwon.tistory.com/78

sudo yum install wget

sudo wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo yum -y install https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
sudo yum -y install mysql-community-server

sudo systemctl enable mysqld
sudo systemctl start mysqld



mysql >>>
create database test;
use test;

create table number( id int(5) NOT NULL );