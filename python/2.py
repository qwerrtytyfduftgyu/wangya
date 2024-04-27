# import math
# import random
# import posixpath as path
#
# print(math.sqrt(16))
# print(math.cos(math.pi/4))
# print(random.choices('abcd', k=8))
# A={35,45,55,62}
# B={45,55,62,85,95}
# print(A|B)
# !/usr/bin/python
# -*- coding: UTF-8 -*-

class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))