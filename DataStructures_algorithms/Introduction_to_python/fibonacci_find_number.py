from math import *
from collections import *
from sys import *
from os import *

num=int(input())
## Read input as specified in the question.
## Print output as specified in the question.
first_num,second_num=1,1
iter_var=3
result=0
while iter_var<=num:
    result=first_num+second_num
    first_num,second_num=second_num,result
    iter_var+=1
if num not in [1,2]:
    print(result)
else:
    print(1)
