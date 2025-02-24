#!/usr/bin/python3
"""
This module defines a class - Rectangle
"""


class Rectangle:
    """
    This class has two attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        function to return width if setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        function to return height if setter checks have passed
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        counter = 0
        output = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            while counter < self.__height:
                output += str(self.print_symbol) * self.__width
                if counter == (self.__height - 1):
                    break
                output += "\n"
                counter += 1
        return output

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            if rect_1.area() > rect_2.area():
                return rect_1.area()
            else:
                return rect_2.area()
