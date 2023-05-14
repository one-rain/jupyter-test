#!/usr/bin/env bash

# 变量

CURRENT_DIR=$(cd "$(dirname "$0")" && pwd)
#shellcheck disable=SC1091
source "${CURRENT_DIR}/common.sh"

center_print "查看进程ID" 20 =
# 通过脚本执行的shell，$$ 就是这个pid
echo "当前bash的PID: ${BASHPID}"
echo "登入交互式shell的PID：$$"

echo ""
center_print "常量和变量" 20 =
# 只读的常量
readonly PATH_TO_FILES='/some/path'

# 声明只读的环境变量，可供shell以外的程序来使用
declare -xr BACKUP_SID='PROD'

# 只读变量，不可更改
readonly url="https://google.com"
echo "${url}"

echo ""
center_print "使用 local 来声明局部变量，以确保其只在函数内部和子函数中可见" 20 =


# 删除变量
v1="https://baidu.com"
echo "删除前：${v1}"
unset v1
echo "删除后：${v1}"

echo ""
center_print "特殊变量" 20 =
echo "当前脚本名称：$0"
echo "传递给脚本或函数的参数个数：$#"
echo "传递给脚本或函数的所有参数：$*"
echo "传递给脚本或函数的所有参数：$@"
echo "上个命令的退出状态，或函数的返回值：$?"

echo ""
center_print "*和@的区别" 20 =

# ∗和@ 都表示传递给函数或脚本的所有参数，不被双引号(" ")包含时，都以"1" "2" … "$n" 的形式输出所有参数。
# 但是当它们被双引号(" ")包含时，"∗"会将所有的参数作为一个整体，以"1 2…n"的形式输出所有参数；
# "@"会将各个参数分开，以"1" "2"…"n" 的形式输出所有参数。

function test_a() {
  echo "test * 1"
  for var in $*
  do
    echo "$var"
  done
  echo "test * 2"
  for var in "$*"
  do
    echo "$var"
  done
}

test_a a b c
echo ""

function test_b() {
  echo "test @ 1"
  for var in $@
  do
    echo "$var"
  done
  echo "test @ 2"
  for var in "$@"
  do
    echo "$var"
  done
}

test_b a b c
