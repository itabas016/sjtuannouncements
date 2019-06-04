#!/usr/bin/env python
# coding: utf-8

'''
File: task.py
Project: sjtuannouncements
File Created: 2019/06/03 15:30
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 15:31
Copyright 2019
'''


import json
import requests

from flask import current_app
from bs4 import BeautifulSoup
from datetime import datetime

from sjtuannouncements.model import Announcement
from sjtuannouncements.db import db
from sjtuannouncements.data import *
from sjtuannouncements.api import *


def load_announcement_page():
    r = requests.get('http://onlinesjtu.com/SeaboardList.aspx?iid=1')
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    for item in soup.find("ul", "asideNewsList").find_all('p'):
        soup_child = BeautifulSoup(str(item))
        announcement = Announcement()
        announcement.title = soup_child.a.text
        link = soup_child.a['href']
        announcement.link = 'http://onlinesjtu.com/' + \
            link if not link.startwith('http') else link
        announcement.publish_time = datetime.strptime(
            soup_child.span.text, '%Y-%d-%m')

        result.append(announcement)
    return result


def refresh_announcements(listener=None):
    try:
        old_announcements = get_the_latest_announcements()

        saved_announcements = 0
        for announcement in load_announcement_page():
            if announcement in old_announcements:
                current_app.logger.info(
                    'This announcement is already exist.\n' + announcement.publish_time + ',' + announcement.title)
            else:
                db.session.add(announcement)
                saved_announcements += 1
        db.session.commit()
        current_app.logger.info(
            'saved {} announcements.'.format(saved_announcements))
    except Exception as e:
        current_app.logger.error(e)
