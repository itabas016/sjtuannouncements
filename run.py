#!/usr/bin/env python
# coding: utf-8

'''
File: run.py
Project: sjtuannouncements
File Created: 2019/06/03 10:57
Author: Roger Cui (itabas016@gmail.com)
Last Modified: 2019/06/03 10:57
Copyright 2019
'''

from sjtuannouncements import create_app

app = create_app('env')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'], debug=app.config['DEBUG'])
