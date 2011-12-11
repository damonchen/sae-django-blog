#!/usr/bin/env python
# coding: utf-8
# yc@2011/09/10

import os

#import sys
#sys.path.insert(0, os.path.dirname( os.path.abspath(__file__) ) )

#os.environ['DJANGO_SETTINGS_MODULE'] = 'djblog.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'djblog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
