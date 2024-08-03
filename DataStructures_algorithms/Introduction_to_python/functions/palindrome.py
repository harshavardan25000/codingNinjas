from typing import List

def palindromeNumber(n: int) -> bool: 
    # Write your code here

    if n<0:
        return False
    
    sum=0
    while n>0:
        digit=n%10
        sum=(sum*10)+digit
        n//=10
    return sum
    


n=323
print(n==palindromeNumber(n))