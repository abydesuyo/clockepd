#!/bin/sh

sudo cp clockepd.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable clockepd.service
sudo systemctl start clockepd.service
