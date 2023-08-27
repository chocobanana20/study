n=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    
    check=[]
    for k in range(i):
        if arr[k][-1]<arr[i] and len(check)<len(arr[k]):
            check=arr[k]
    arr[i]=check+[arr[i]]
ans=[]
for i in arr:

    ans.append(len(i))


print(max(ans))