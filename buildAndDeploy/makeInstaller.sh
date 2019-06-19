#!/usr/bin/env bash
set -e
reg_url=$1
reg_url_cleaned="${reg_url%\"}"
reg_url_cleaned="${reg_url_cleaned#\"}"
sumo_url=$2
sumo_url_cleaned="${sumo_url%\"}"
sumo_url_cleaned="${sumo_url_cleaned#\"}"
commitId=$3
commitId_cleaned="${commitId%\"}"
commitId_cleaned="${commitId_cleaned#\"}"
env=$4

cp linuxScript.template.sh RegisterYourComputer-${env}.sh
sed -i "s,#commitId#,${commitId},g" RegisterYourComputer-${env}.sh
sed -i "s,#registration_url#,${reg_url_cleaned},g" RegisterYourComputer-${env}.sh
sed -i "s,#sumo_logic_url#,${sumo_url_cleaned},g" RegisterYourComputer-${env}.sh

