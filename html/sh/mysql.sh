rm /etc/localtime



ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime

sudo echo "ZONE="Asia/Seoul" 
UTC=true /etc/sysconfig/clock"


###mysql 
## https://dev-kwon.tistory.com/78

sudo yum install wget

wget http://repo.mysql.com/mysql57-community-release-el7-11.noarch.rpm

sudo yum install http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
sudo yum install mysql-community-server -y

sudo systemctl enable mysqld
sudo systemctl start mysqld