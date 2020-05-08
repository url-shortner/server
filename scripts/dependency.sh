#!/bin/bash

sudo python3 -m virtualenv /home/ubuntu/server/venv/
sudo chown -R ubuntu:ubuntu /home/ubuntu/server/venv/
source /home/ubuntu/server/venv/bin/activate
pip3 install -r /home/ubuntu/server/requirements.txt
deactivate