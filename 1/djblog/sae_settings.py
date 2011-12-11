#! /usr/bin/env python
#coding=utf-8

import sae.const
import os

PROJECT_PATH = os.path.dirname( os.path.abspath( __file__ ) )

db = sae.const.MYSQL_DB
user = sae.const.MYSQL_USER
password = sae.const.MYSQL_PASS
host = sae.const.MYSQL_HOST
port = sae.const.MYSQL_PORT   #请根据框架要求自行转换为int
host_s = sae.const.MYSQL_HOST_S #salve mysql server

# 数据库信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql 可以改成 'postgresql_psycopg2', 'postgresql', 'sqlite3' or 'oracle'.
        'NAME':  db,                      # 数据库名
        'USER':  user,                      # sqlite3 不使用此配置
        'PASSWORD': password,                  # sqlite3 不使用此配置
        'HOST': host,
        'PORT': port,
    }
}

MEDIA_URL = '/media/'

# SAE中没有用处，由SAE系统指定
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_PATH , "static")

DEBUG  = False
TEMPLATE_DEBUG = DEBUG
