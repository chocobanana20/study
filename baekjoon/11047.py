n , k = map(int,input().split())
arr=[]
for _ in range(n):
    num=int(input())
    if num<=k:
        arr.append(num)

arr=list(reversed(arr))
ans=0
for i in arr:
    if k>=i:
        ans+=k//i
        k=k%i
        
       
print(ans)