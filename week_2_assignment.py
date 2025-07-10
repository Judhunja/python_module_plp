#!/usr/bin/env python3
""" Python list manipulation """

my_list = []
my_list.append(10)
print(my_list)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(2, 15)
my_list.extend([50, 60, 70])
print(my_list)
print(my_list.pop())
my_list.sort()
print(f"Sorted list: {my_list}")
print(my_list.index(30))
