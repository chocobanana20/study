import sys
n , k = map(int,input().split())
sys.setrecursionlimit(1000000007) 



arr= {}

def factorial(x):
    if x in arr:
        return arr[x]
    elif x==1:
        return 1
    else:
        arr[x]=(x*factorial(x-1))%1000000007
        return arr[x]
    
ans = (factorial(n)/factorial(k))/factorial(n-k)
print(int(ans))