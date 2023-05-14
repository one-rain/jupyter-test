#!/usr/bin/env bash


########################
# 居中打印
# 参数：
#   1、打印内容
#   2、打印的总长度
#   3、填充的符号，默认位空格
########################
function center_print() {
  local text="$1"
  local column_width="$2"
  local padding_char=''
  if [ $# -ge 3 ]; then
    padding_char="${3}"
  fi

  local text_width=${#text}
  local padding_width=0 # 左右填充符号的长度
  if [[ $text_width -lt $column_width ]]; then
    padding_width=$(((column_width-text_width)/2))
  fi

  if [[ $padding_width -ge $column_width ]]; then
    column_width=$padding_width
  fi

  #padding=$(eval echo "{1..${padding_width}}")
  local padding=''
  #for c in $(eval "echo {1..$padding_width}"); do padding+="${padding_char}"; done
  for ((i=0; i<"${padding_width}"; i++)); do padding+="${padding_char}"; done
  printf "%s%s%s\n" "${padding}" "${text}" "${padding}"
  #printf "%0-*s\n" 10 "${text}"
}
