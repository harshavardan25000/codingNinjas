def find_GCD(a, b):
    small=a if a<b else b
    for i in range(small,0,-1):
        print(i,'*')
        if a%i==0 and b%i==0:
            return i
        
    return 1

print(find_GCD(11,25))