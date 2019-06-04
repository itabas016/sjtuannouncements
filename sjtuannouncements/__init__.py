#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 10:47
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 10:48
Copyright 2019
'''
from flask import Flask
from sjtuannouncements.db import db
from sjtuannouncements.logger import init_logger


def create_app(config, should_register_blueprints=True):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    db.init_app(app)
    init_logger(app)

    if should_register_blueprints:
        register_blueprints(app)

    return app


def register_blueprints(app):
    from sjtuannouncements.controller import bp_announcement
    app.register_blueprints(bp_announcement)
