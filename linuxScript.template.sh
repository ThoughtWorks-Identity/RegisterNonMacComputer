#!/usr/bin/env bash

function cleanup() {
    rm -rf /tmp/twregister    
}

function exitWithPythonError(){
  echo "Python version 3 and above required to run this program. Please install Python 3 and retry"
  exit 1
}


function checkIfPythonInstalled() {
  pythonLocation=$1  
  pythonVersion=`$pythonLocation -c 'import sys; print(sys.version_info[:][0])'`
  exitCodeOfPythonCommand=$?

  if [[ "$exitCodeOfPythonCommand" -ne "0" || "$pythonVersion" -ne "3" ]]
  then
    exitWithPythonError
  fi
}

function downloadSourceCode() {
  commitId=$1
  mkdir -p /tmp/twregister
  curl -LkSs "https://api.github.com/repos/ThoughtWorks-Identity/RegisterNonMacComputer/tarball?ref=${commitId}" -o /tmp/twregister/RegisterNonMacComputer.tar.gz
  tar -C /tmp/twregister -xvf /tmp/twregister/RegisterNonMacComputer.tar.gz
}

function createVirtualEnv() {
    pythonLocation=$1  
    commitId=$2
    $pythonLocation -m venv /tmp/twregister/.venv
    source  /tmp/twregister/.venv/bin/activate
    pip3 install -r /tmp/twregister/ThoughtWorks-Identity-RegisterNonMacComputer-${commitId}/requirements-linux.txt
}

function createConfigurationProperties() {
    commitId=$1
    registration_url=$2
    sumo_logic_url=$3
    echo "registration_url=${registration_url}" > /tmp/twregister/ThoughtWorks-Identity-RegisterNonMacComputer-${commitId}/src/configuration.properties
    echo "sumo_logic_url=${sumo_logic_url}" >> /tmp/twregister/ThoughtWorks-Identity-RegisterNonMacComputer-${commitId}/src/configuration.properties
}


function executeProgram() {
    commitId=$1
    /tmp/twregister/.venv/bin/python3 /tmp/twregister/ThoughtWorks-Identity-RegisterNonMacComputer-${commitId}/src/RegisterYourComputer.py    
}

# Default Location of python3. Change here if its not the same on your machine!
pythonLocation=/usr/bin/python3
commitId=#commitId#
registration_url="#registration_url#"
sumo_logic_url="#sumo_logic_url#"
cleanup
checkIfPythonInstalled $pythonLocation
downloadSourceCode $commitId
createVirtualEnv $pythonLocation $commitId
createConfigurationProperties $commitId $registration_url $sumo_logic_url
executeProgram $commitId
cleanup

