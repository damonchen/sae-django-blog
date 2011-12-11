#!/usr/bin/env python
# coding: utf-8
# yc@2011/08/27

from django.conf import settings

def globals_vars(request):
	'''全局模板变量'''
	return {
		'request': request,
		'settings': settings,
		'STATIC_URL':settings.STATIC_URL,
		'PROJECT_PATH' : settings.ROOT_DIR,
		'STATIC_PATH' : settings.STATIC_ROOT,		
	}
