#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import Blueprint


admin = Blueprint('admin', __name__)


@admin.route('/')
def v_index():
    return '''<li><a href="/shop">Here is admin you can go shop</a></li>'''
