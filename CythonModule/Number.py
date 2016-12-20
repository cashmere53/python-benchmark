# -*- coding: utf-8 -*-

import random

class Number(object):
    def __init__(self):
        self.num1 = self.random_number()

    @classmethod
    def random_number(cls):
        return random.randint(1, 100)
