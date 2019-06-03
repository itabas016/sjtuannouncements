#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 14:48
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 14:48
Copyright 2019
'''

from sjtuannouncements import create_app
from sjtuannouncements.data import *

from flask_restful import reqparse, abort, Api, Resource

api = Api(create_app)


class Announcement(Resource):
    def get(self, announcement_id):
        return get_announcement(announcement_id)


class AnnouncementList(Resource):
    def get(self):
        return get_announcements()


class AnnouncementLatestList(Resource):
    def get(self, number):
        return get_the_latest_announcements(number)


api.add_resource(AnnouncementList, '/api/announcements')
api.add_resource(AnnouncementLatestList, '/api/announcements/latest/<number>')
api.add_resource(Announcement, '/api/announcements/<announcement_id>')
