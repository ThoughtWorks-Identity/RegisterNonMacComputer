#!/usr/bin/env bash
set -e
reg_url=$1
reg_url_cleaned="${reg_url%\"}"
reg_url_cleaned="${reg_url_cleaned#\"}"
sumo_url=$2
sumo_url_cleaned="${sumo_url%\"}"
sumo_url_cleaned="${sumo_url_cleaned#\"}"
echo registration_url=${reg_url_cleaned} > configuration.properties
echo sumo_logic_url=${sumo_url_cleaned} >> configuration.properties
echo "version of python"
python3 --version
echo "showing path"
echo $PATH
echo "showing usr local bin"
echo $(ls /usr/local/bin)
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements-linux.txt
pyinstaller --onefile --paths="src" --hidden-import "src/LinuxComputer" --add-data "configuration.properties:." -n RegisterLinuxComputer src/RegisterYourComputer.py
