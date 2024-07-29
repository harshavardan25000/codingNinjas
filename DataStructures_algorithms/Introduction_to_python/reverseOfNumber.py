num=int(input())
#1234
result=0
while num>0:
    digit=num%10
    result*=10
    result+=digit
    num=num//10

print(result)

