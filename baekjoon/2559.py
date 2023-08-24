n , k = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]

ans=arr[k-1]  # 제일 처음의 연속된 며칠의 합을 미리 넣음
for i in range(k,len(arr)):
    check=arr[i]-arr[i-k]
    ans=max(ans,check)
        

print(ans)