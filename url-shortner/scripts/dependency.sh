#!/bin/bash

sudo python3 -m virtualenv /home/ubuntu/airtxt/venv/
sudo chown -R ubuntu:ubuntu /home/ubuntu/airtxt/venv/
source /home/ubuntu/airtxt/venv/bin/activate
pip3 install -r /home/ubuntu/airtxt/requirements.txt
deactivate