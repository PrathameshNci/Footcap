#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/shoecom/requirements.txt
sudo chmod 777 /home/ubuntu/clothing
sudo chmod 777 /home/ubuntu/clothing/db.sqlite3
