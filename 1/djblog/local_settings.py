#!/usr/bin/env python
# coding: utf-8
# yc@2011/08/26

import os

# 时区
TIME_ZONE = 'Asia/Shanghai'

# 语言
LANGUAGE_CODE = 'zh-cn'

# 邮箱（报错时发送）
EMAIL = 'netubu@gmail.com'

# 数据库信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql 可以改成 'postgresql_psycopg2', 'postgresql', 'sqlite3' or 'oracle'.
        'NAME': 'djblog',                      # 数据库名
        'USER': 'root',                      # sqlite3 不使用此配置
        'PASSWORD': 'admin',                  # sqlite3 不使用此配置
        'HOST': '',
        'PORT': '',
    }
}

# 主题
THEME = 'classic'

# 站点名称
SITE_TITLE = 'Damon'
# 副标题
SITE_SUBTITLE = u'窗外……'
# 作者
SITE_AUTHOR = 'DamonChen'
# 描述
SITE_DESC = u'片片的思绪，在这儿生根发芽吧……'

# 分页大小
PER_PAGE = 5
# recent 个数
RECENT_COUNT = 5

# google 统计的 id
GA_ID = 'UA-18808400-2'

# google custom search id, see http://www.google.com/cse/
CSE_ID = '017823656936221718810:8oexw_fkbz0'

# 换一个安全的KEY
SECRET_KEY = 'pnmv#z_o+i3cy6h%d2oc+r%q)p$4f22v%@$(x2lb37pcm#9o9('

# disqus 评论 id
DISQUS_SHORTNAME = 'damonchen'


# GOOGLE +1按钮
GOOGLE_PLUS = True

#### 以下配置不要改动 ####
TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/' + THEME),
)
ADMINS = (
    ('admin', EMAIL),
)
MANAGERS = ADMINS


try:
    from sae_settings import *
except ImportError:
    pass
