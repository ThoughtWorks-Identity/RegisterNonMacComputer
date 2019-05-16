#!/usr/bin/env bash
echo registration_url=$1 > configuration.properties
echo sumo_logic_url=$2 >> configuration.properties
python3 -m pyinstaller --onefile --add-data "configuration.properties:." -n RegisterLinuxComputer src/RegisterYourComputer.py
