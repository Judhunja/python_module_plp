#!/usr/bin/env python3
""" Read and write to a python file """


def readwritefile(file):
    """ Reads a file and writes a modified version to a new file """
    try:
        with open(file, 'w') as f:
            content = "Hello"
            f.write(content)
    except Exception:
        print("An error occurred while writing to the file")


def accessfile(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file you requested does not exist")
    except IOError:
        print("The file can't be read")


readwritefile("./greeting.txt")
accessfile("none.txt")
