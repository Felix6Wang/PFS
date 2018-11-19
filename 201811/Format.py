#!/usr/bin/env python
# encoding: utf-8

"""
@author:Felix
@date:2018-11-19
"""

name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = int(input("Salary:"))

print(name, age, job, salary)

msg = '''
----------info----------
Name:   %s
Age :   %s
Job :   %s
Salary: %.2f
----------end-----------
'''

print(msg % (name, age, job, salary))

iAge = int(age)
print("You will be retired in %d years" % (65 - iAge))

