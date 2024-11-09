#!/usr/bin/python3
'''Function to check if object is the same class'''


def inherits_from(obj, a_class):
    '''Check if obj is an instance of a class that inherited
    from the specified class'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
