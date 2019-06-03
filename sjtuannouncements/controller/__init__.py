#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 11:06
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 11:06
Copyright 2019
'''

import re
import requests

from sjtuannouncements.data import *

from flask import render_template, Blueprint, json, request, jsonify, url_for, flash

bp_announcement = Blueprint('announcement', __name__)


@bp_announcement.route('/')
def latest_announcements():
    announcements = get_the_latest_announcements()
    return render_template('latest.html', announcements=announcements)


@bp_announcement.route('/announcements')
def announcements():
    announcements = get_announcements()
    return render_template('announcements.html', announcements=announcements)


@bp_announcement.route('/announcements/<int:announcement_id>')
def announcement(announcement_id):
    announcements = get_announcement(announcement_id)
