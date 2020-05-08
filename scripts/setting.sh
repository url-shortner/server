#!/bin/bash
sudo touch /home/ubuntu/airtxt/ucut/ip
sudo chmod 766 /home/ubuntu/airtxt/ucut/ip
sudo ifconfig | grep "inet" | awk '{print $2}'| head -n 1| sed -e 's/addr://g' > /home/ubuntu/server/ucut/ip
sudo chmod 755 /home/ubuntu/server/ucut/ip
sudo cp /home/ubuntu/airtxt/airtxt/ip /home/ubuntu/server/ucut/ip

sudo chown www-data:www-data /home/ubuntu/server/db.sqlite3
sudo chown www-data:www-data /home/ubuntu/server

directory="/home/ubuntu/development"
source /home/ubuntu/airtxt/venv/bin/activate
sudo python3 /home/ubuntu/airtxt/manage.py makemigrationsrl

if [ -d "$directory" ]; then
    sudo cp /home/ubuntu/development/server/wsgi.py /home/ubuntu/server/ucut/wsgi.py
    sudo cp /home/ubuntu/development/manage.py /home/ubuntu/server/manage.py
    sudo python3 /home/ubuntu/server/manage.py migrate
    echo "File $directory exists."
else
    sudo python3 /home/ubuntu/airtxt/manage.py migrate --database=auth_master
    sudo python3 /home/ubuntu/airtxt/manage.py migrate --database=shorturl_master
    echo "File $directory does not exist."
fi

sudo python3 /home/ubuntu/server/manage.py collectstatic --noinput
sudo python3 /home/ubuntu/server/manage.py runscript migrate_entity -v3