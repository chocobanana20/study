n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=arr[0]
for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]
    ans+=arr[i]
    
print(ans)
    