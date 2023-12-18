#!/usr/bin/env bash

service_name=""
command_tag=""

service_names=(mysql nginx)

function usage() {
  echo "
    Usage: args [-n service name] [-c service command start|stop|restart]
      -n 服务的名称
      -c 执行服务的命令，一般为start|stop|restart
  "
}

function init_mysql() {
    echo "----start restart mysql5.7 service----"
    if [ ! -f /var/run/mysqld/ ]; then
        mkdir -p /var/run/mysqld
        chown mysql:mysql /var/run/mysqld
    fi
    service mysql "${1}"
}

function init_nginx() {
    echo "----start restart nginx service----"
    service nginx "${1}"
}

while getopts "n:c:" arg; do
    case "$arg" in
        n)
            for value in "${service_names[@]}"; do
                if [ "${value}" == "${OPTARG}" ]; then
                    service_name="${value}"
                fi
            done
            if [ -z "${service_name}" ]; then
                echo "服务 ${OPTARG} 不存在"
                usage
                exit 1
            fi
            ;;
        c)
            command_tag="${OPTARG}"
            ;;
        :)
            echo ""
            echo "-s${OPTARG} 不存在."
            usage
            exit 1
          ;;
        *)
            echo ""
            echo "无效参数: -${OPTARG}"
            usage
            exit 1
            ;;
    esac
done

if [ -z "${service_name}" ]; then
    echo "服务名称缺失"
    usage
    exit 1
fi

if [ -z "${command_tag}" ]; then
    echo "服务命令缺失"
    usage
    exit 1
fi

init_"${service_name}" "${command_tag}"