#encoding:utf-8
#name:mod_config.py

import configparser
import os

#获取config配置文件
def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/db.conf'
    config.read(path)
    return config.get(section, key)