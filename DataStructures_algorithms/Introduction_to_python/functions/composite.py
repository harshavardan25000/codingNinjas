def is_prime(n):

    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

def print_composite(n):

    for i in range(n+1):
        if is_prime(i)==False:
            print(i)
