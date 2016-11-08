#!/bin/bash

#install pip

sudo easy_install pip

#install virtualenv
sudo pip install virtualenv

#active virtualenv
virtualenv .env

# freeze 查看安装的库
pip freeze

#install request
sudo pip install request

#python 模式下 help(rqeuest) 查看文档

#httpbin.org test server
#抓取httpbin网络服务到本地
sudo pip install gunicorn httpbin

#启动httpbin
sudo gunicorn httpbin:app
