

n=int(input())
num=2

while num<n:
    i=2
    while i<=num//2:

        if num%i==0:
            break
        i+=1
    else:
        print(f"{num} is a prime number")
    num+=1

