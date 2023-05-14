#!/usr/bin/env bash

# 日期时间

CURRENT_DIR=$(cd "$(dirname "$0")" && pwd)
#shellcheck disable=SC1091
source "${CURRENT_DIR}/common.sh"

today1=$(date "+%Y-%m-%d")
today2=$(date "+%-m/%-d/%y")
yesterday=$(date -d "-1 day" "+%Y-%m-%d")
year=$(date -d "${JOB_DAY}" +%Y)
ym=$(date -d "${JOB_DAY}" +%Y%m)
week=$(date -d "${JOB_DAY}" +%w)
hour=$(date -d "-1 hour" +%H)
time=$()

echo "today: ${today1}, ${today2}"
echo "yesterday: ${yesterday}"
echo "time: $(date "+%Y-%m-%d %H:%M:%S")"
