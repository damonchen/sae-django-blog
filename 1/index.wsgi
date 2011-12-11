#! /usr/bin/env python
#coding=utf-8

# DamonChen 2011-12-9

import sae
from wsgi_app import application as app

application = sae.create_wsgi_app( app )


