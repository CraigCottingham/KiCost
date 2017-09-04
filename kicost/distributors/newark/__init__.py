# -*- coding: utf-8 -*-

__author__ = 'XESS Corporation'
__email__ = 'info@xess.com'

from .newark import *

from .. import distributors
distributors.update(
    {
        'newark': {
            'module': newark,
            'scrape': 'web',
            'function': 'newark',
            'label': 'Newark',
            'order_cols': ['part_num', 'purch', 'refs'],
            'order_delimiter': ','
        }
    }
)