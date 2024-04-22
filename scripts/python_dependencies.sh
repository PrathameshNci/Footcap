#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/shoecom/requirements.txt
sudo chmod 777 /home/ubuntu/shoecom
sudo chmod 777 /home/ubuntu/shoecom/db.sqlite3
