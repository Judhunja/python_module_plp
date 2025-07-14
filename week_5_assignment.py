#!/usr/bin/env python3
""" This module contains a custom user file and a Animals class """


class BaseGeometry:
    """ Initializes a BseGeometry class """

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemeted")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Initializes a class Rectangle """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ str method that prints the width and height of the
        rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Dog(Animal):
    def move(self):
        return "Running on four legs"


class Fish(Animal):
    def move(self):
        return "Swimming through water"


class Bird(Animal):
    def move(self):
        return "Flying through the air"


class Snake(Animal):
    def move(self):
        return "Slithering on the ground"


class Kangaroo(Animal):
    def move(self):
        return "Hopping on two legs"


class Car:
    def move(self):
        return "Driving on the road"


class Plane:
    def move(self):
        return "Flying through the sky"
