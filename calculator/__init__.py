""" This is the Calculator Class"""
from calculator.calculation import Addition, Subtraction, Multiplication


class Calculator:
    """ This is the default result property"""
    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculations = Addition.create(tuple_list)
        return calculations.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calculations = Subtraction.create(tuple_list)
        return calculations.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the subtract method"""
        calculations = Multiplication.create(tuple_list)
        return calculations.get_result()
