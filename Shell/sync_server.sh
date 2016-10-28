#!/bin/bash

#遇到任何错误则终止脚本
set -e
set -o pipefail

echo "参数个数:" $#

if [ $# -lt 2 ]; then
    echo "target or user is invalid, target:[staging|alpha|bravo,delta|gamma|echo], ext:sh sync_server.sh xiaodong staging"
    exit 1
fi

build_user=$1
build_target=$2
build_client=$3

echo "build_user:" $build_user
echo "build_target:" $build_target
echo "build_client:" $build_client

#初始化参数
port=4000
path_git=${pwd}
path_server=${pwd}/Server/ #Server端代码根目录
path_config=${pwd}/game_dev.json #项目配置
path_deploy_client=/data/app/static/${build_target}
path_deploy=/data/work/game/${build_target}

#检查参数
target_list=("staging" "alpha" "bravo" "delta" "gamma" "echo" "kappa" "sigma" "omega")
port_list=("4000" "4100" "4200" "4300" "4400" "4500" "4600" "4700" "4800")

#检查target_list中是否存在 build_target
if [[ " ${target_list[@]} " =~ " ${build_target} " ]] ;then
        echo "build target: ${build_target}"
else
    echo "invalid target ${build_target}"
    exit 1
fi

#  @ is all params
echo "@: ${@}"
targetListNum=${#target_list[@]}
echo "targetListNum: ${targetListNum}"

for ((i = 0 ; i < targetListNum; i++))
{
    if echo "${target_list[i]}" | grep -q "${build_target}"; then
        port="${port_list[i]}"
    fi
}
