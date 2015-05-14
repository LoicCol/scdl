"""
Copied from https://github.com/davidfischer-ch/pytoolbox/blob/master/pytoolbox/logging.py
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
from termcolor import colored


class ColorizeFilter(logging.Filter):

    color_by_level = {
        logging.DEBUG: 'yellow',
        logging.ERROR: 'red',
        logging.INFO: 'white'
    }

    def filter(self, record):
        record.raw_msg = record.msg
        color = self.color_by_level.get(record.levelno)
        if color:
            record.msg = colored(record.msg, color)
        return True
