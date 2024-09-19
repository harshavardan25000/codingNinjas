# Read input as sepcified in the question
# Print output as specified in the question
def sum_method(n,arr):
    
    result=0
    for ele in arr:
        result+=ele
    return result
n=int(input())
arr=list(map(int,input().split()))
print(arr)
print(sum_method(n,arr))