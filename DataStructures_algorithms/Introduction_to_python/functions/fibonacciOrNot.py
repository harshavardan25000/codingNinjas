def checkMember(n):
    # write your code logic here !!!!

    first,second=0,1
    if first==n or second==n:
        return True

    while second <=n:
        if second==n:
            return True
        first,second=second,first+second
    return False



        




    