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

import datetime
import json
import requests

from flask import current_app
from bs4 import BeautifulSoup

from sjtuannouncements.model import Announcement
from sjtuannouncements.db import db
from sjtuannouncements.data import *
from sjtuannouncements.api import *


def load_announcement_page():
    r = requests.get('http://onlinesjtu.com/SeaboardList.aspx?iid=1')
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.find("ul", "asideNewsList").find_all('p'):
        print(item)


def refresh_announcements(listener=None):
    old_announcements = get_the_latest_announcements()

    announcement = Announcement()
    pass
