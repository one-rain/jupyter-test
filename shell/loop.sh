#!/usr/bin/env bash

# 循环

CURRENT_DIR=$(cd "$(dirname "$0")" && cd .. && pwd)
#shellcheck disable=SC1091
source "${CURRENT_DIR}/shell/common.sh"


center_print 字符串序列 20 =
for loop in 1 2 3 4 5
do
  echo "The value is: $loop"
done

echo ""
center_print 显示主目录下以.bash开头的文件 20 =
for file in "$HOME/".bash*
do
  echo "$file"
done

echo ""
center_print while循环 20 =
counter=0
while [[ $counter -lt 10 ]]
do
  counter=$((counter+1))
  echo -n "index: ${counter}，"
  if [[ $counter -lt 5 ]]; then
    echo "继续循环."
    continue
  fi

  if [[ $counter -ge 5 ]]; then
    echo "即将跳出循环."
    break
  fi
done

echo ""
center_print 输入重定向 20 =
while read -r line
do
  echo "${line}"
done < "${CURRENT_DIR}"/data/mingri/product_type.csv

