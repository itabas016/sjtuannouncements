#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 11:09
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 11:09
Copyright 2019
'''

from sjtuannouncements.db import db


class Announcement(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(256), nullable=False)
    link = db.Column(db.String(1024), nullable=False)
    publish_time = db.Column(db.DateTime, nullable=True)
