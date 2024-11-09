#!/usr/bin/python3
'''create a base geometry class'''


class BaseGeometry:
    '''raise an exception and validate value'''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
