#!/bin/bash
sudo touch /home/ubuntu/airtxt/airtxt/ip
sudo chmod 766 /home/ubuntu/airtxt/airtxt/ip
sudo ifconfig | grep "inet" | awk '{print $2}'| head -n 1| sed -e 's/addr://g' > /home/ubuntu/airtxt/airtxt/ip
sudo chmod 755 /home/ubuntu/airtxt/airtxt/ip
sudo cp /home/ubuntu/airtxt/airtxt/ip /home/ubuntu/airtxt/ucut/ip

sudo chown www-data:www-data /home/ubuntu/airtxt/db.sqlite3
sudo chown www-data:www-data /home/ubuntu/airtxt

directory="/home/ubuntu/development"
source /home/ubuntu/airtxt/venv/bin/activate
sudo python3 /home/ubuntu/airtxt/manage.py makemigrations

if [ -d "$directory" ]; then
    sudo cp /home/ubuntu/development/airtxt/wsgi.py /home/ubuntu/airtxt/airtxt/wsgi.py
    sudo cp /home/ubuntu/development/ucut/wsgi.py /home/ubuntu/airtxt/ucut/wsgi.py
    sudo cp /home/ubuntu/development/manage.py /home/ubuntu/airtxt/manage.py
    sudo python3 /home/ubuntu/airtxt/manage.py migrate
    echo "File $directory exists."
else
    sudo python3 /home/ubuntu/airtxt/manage.py migrate --database=auth_master
    sudo python3 /home/ubuntu/airtxt/manage.py migrate --database=skill_master
    sudo python3 /home/ubuntu/airtxt/manage.py migrate --database=shorturl_master
    echo "File $directory does not exist."
fi

sudo python3 /home/ubuntu/airtxt/manage.py collectstatic --noinput
sudo python3 /home/ubuntu/airtxt/manage.py runscript migrate_entity -v3