from math import *
from collections import *
from sys import *
from os import *

raw_input=input()
basic=int(raw_input.split(' ')[0])
grade=raw_input.split(' ')[1]
total_salary=basic

total_salary+=round(0.2*basic,2)
print(total_salary)
total_salary+=round(0.5*basic,2)
print(total_salary)
if grade=='A':
    total_salary+=1700
elif grade=='B':
    total_salary+=1500
else:
    total_salary+=1300
total_salary-=0.11*basic

print(round(total_salary))