""" This is the Calculator Class"""
from operations import *


class Calculator:
    """ This is the default result property"""
    result = 0

    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return Addition.add(value_1 + value_2)

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return Subtract.subtract(value_1, value_2)

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the subtract method"""
        return Multiply.multiply(value_1, value_2)

    @staticmethod
    def get_result(self):
        """ This is the get result method"""
        return self.result
