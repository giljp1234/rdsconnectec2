#!/bin/bash

sudo python3 -m pip install flask
sudo python3 -m pip install boto3

aws configure

aws dynamodb scan --table-name test --region ap-northeast-2




$ sudo yum install mod_wsgi -y



#root계정으로 
echo "<VirtualHost *:80>
    ServerName ec2-3-34-46-59.ap-northeast-2.compute.amazonaws.com
    WSGIDaemonProcess app user=ec2-user group=ec2-user threads=5
    WSGIScriptAlias / /home/ec2-user/project/app.wsgi

    <Directory /home/ec2-user/project>  # Flask 애플리케이션의 경로로 수정
        Options FollowSymLinks
	AllowOverride All
	Require all granted
    </Directory>
</VirtualHost>" >> /etc/httpd/conf/httpd.conf
