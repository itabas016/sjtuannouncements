#!/usr/bin/env python
# coding: utf-8

'''
File: __init__.py
Project: sjtuannouncements
File Created: 2019/06/03 11:05
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 11:05
Copyright 2019
'''

import logging
from logging.handlers import RotatingFileHandler


def init_logger(app):
    handler = RotatingFileHandler(
        'sjtuannouncements.log', maxBytes=1024 * 1024 * 2, backupCount=2)
    logging_format = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
