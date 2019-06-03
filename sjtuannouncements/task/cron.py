#!/usr/bin/env python
# coding: utf-8

'''
File: cron.py
Project: sjtuannouncements
File Created: 2019/06/03 15:30
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 15:31
Copyright 2019
'''

from celery.schedules import crontab
from celery.task import periodic_task

from sjtuannouncements import create_app
from sjtuannouncements.task import *
from sjtuannouncements.task import task


app = create_app('env', False)
celery = create_celery(app)


@periodic_task(run_every=(crontab(minute=0, hours='*/6,8-20')), name="scheduled_refresh_announcements_task", ignore_result=True)
def scheduled_refresh_announcements_task():
    with app.app_context():
        task.refresh_announcements()


@celery.task(bind=True)
def refresh_announcements_task(self):
    def listener(current, total, result):
        self.update_state(state='PROGRESS', meta={'progress': current / total})

    with app.app_context():
        return {'progress': 1, 'result': task.refresh_announcements(listener)}
