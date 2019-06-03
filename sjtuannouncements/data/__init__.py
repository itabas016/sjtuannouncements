#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 14:41
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 14:42
Copyright 2019
'''

from sjtuannouncements.model import Announcement


def get_announcements():
    return Announcement.query.all()


def get_the_latest_announcements(number=10):
    return Announcement.query.order_by(Announcement.create_time.desc()).limit(number).all()


def get_announcement(announcement_id):
    return Announcement.query.get(announcement_id)
