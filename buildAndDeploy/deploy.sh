#!/usr/bin/env bash
set -e

bucket=$1
filename=$2

aws s3 sync ${filename} s3://${bucket}/laptop-registration/${filename} --delete
