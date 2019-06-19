#!/usr/bin/env bash
set -e

bucket=$1
win_filename=$2
lin_filename=$3

aws s3 cp ${win_filename} s3://${bucket}/laptop-registration/RegisterYourComputer.exe
aws s3 cp ${lin_filename} s3://${bucket}/laptop-registration/RegisterYourComputer.sh


