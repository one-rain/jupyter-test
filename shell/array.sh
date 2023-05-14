#!/usr/bin/env bash

# 数组

CURRENT_DIR=$(cd "$(dirname "$0")" && pwd)
#shellcheck disable=SC1091
source "${CURRENT_DIR}/common.sh"

array=('v1' 'v2' 'v3')

center_print 访问数组 20 =
echo "${array[2]}" # 访问数组（bash下标是从0开始）
echo "${array[*]}" # 使用*号访问数组所有的值
echo  "${#array[@]}" # 数组长度

echo ""
center_print 遍历数组 20 =
for v in "${array[@]}";
do
  echo "${v}"
done

