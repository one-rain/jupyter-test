#!/usr/bin/env bash

# 打印

CURRENT_DIR=$(cd "$(dirname "$0")" && pwd)
#shellcheck disable=SC1091
source "${CURRENT_DIR}/common.sh"

# printf  format-string  [arguments...]
# %s %c %d %f 都是格式替代符，％s 输出一个字符串，％d 整型输出，％c 输出一个字符，％f 输出实数，以小数形式输出。
# %-10s 指一个宽度为 10 个字符（- 表示左对齐，没有则表示右对齐）,任何字符都会被显示在 10 个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来
# %-4.2f 指格式化为小数，其中 .2 指保留2位小数


center_print test 20 =
ds=''
printf "%10s${ds}\n" {1..10}

echo ""
center_print 单元表格 20 =
printf "|%-10s|%-8s|%-4s|\n" 姓名 性别 体重kg

echo ""
center_print "8个宽度,右对齐，小数点保留2位" 20 ==
printf "|%8.2f|\n" 1.11
echo ""

echo "多个参数仍然按照指定格式输出"
printf "%s" abc def
echo ""
echo "带换行符"
printf "%s\n" abc def

echo ""
center_print 带有颜色的 20 =
echo -e "\e[1;33mOK\e[0m" #红色显示
echo -e "\e[34mOK\e[0m" #蓝色显示
echo -e "\033[1mOK" #加粗显示
echo -e "\e[4mOK\e[0m"
echo -e "\e[5mOK\e[0m"
echo -e "\e[32;44mOK\e[0m" #绿色字体，蓝色背景显示 OK

echo ""
center_print echo不换行 20 =
echo -n "这里的echo不换行，"
echo "看看结果。"

COLOR_ERROR="\e[38;5;198m"
COLOR_NONE="\e[0m"
COLOR_SUCC="\e[92m"

echo "error: ${COLOR_ERROR}"
echo "none: ${COLOR_NONE}"
echo "succ: ${COLOR_SUCC}"
