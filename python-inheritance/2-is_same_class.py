#!/usr/bin/python3
'''Function to check if object is the same class'''


def is_same_class(obj, a_class):
    '''Check if obj is exactly an instance of the class'''
    return type(obj) is a_class
