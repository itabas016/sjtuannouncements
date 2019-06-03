#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 15:30
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 15:42
Copyright 2019
'''

from celery import celery


def create_celery(app):
    celery = Celery('announcements_celery',
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery
