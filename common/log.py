# -*- coding:utf-8 -*-
# !/usr/bin/python
# log.py
# Created by Vic on 2019-10-11
# Python: 3.7.2

import logging


class Log:
    @classmethod
    def set_logger(cls, udid, file):
        logger = logging.getLogger('iOS')
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(file, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s'
                                      + ' - %s' % udid
                                      + ' - %(levelname)s'
                                      + ' - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        cls.logger = logger

    def d(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


