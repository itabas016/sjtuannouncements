#!/usr/bin/env python
# coding: utf-8

'''
File: env.py
Project: sjtuannouncements
File Created: 2019/06/03 11:00
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 11:00
Copyright 2019
'''

import os

APP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/sjtuannouncements'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + APP_PATH + '/sjtuannouncements.db'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
