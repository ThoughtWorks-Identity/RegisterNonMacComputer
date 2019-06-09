#!/usr/bin/env bash
set -e

bucket=$1
filename=$2

aws s3 cp ${filename} s3://${bucket}/laptop-registration/RegisterLinuxComputer
aws s3 cp ${filename} s3://${bucket}/laptop-registration/RegisterYourComputer.exe
