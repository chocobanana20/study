# 범위가 나와있지 않아서 그냥 다 더하기 하면 시간초과 될 듯
# 행을 기준으로  누적합을 이용한다면 o(행의 개수) 와 비슷할 것임으로 시간초과 나지 않을듯
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
arr=[]
for _ in range(n):
    arr1=list(map(int,input().split()))
    for i in range(1,len(arr1)):
        arr1[i]=arr1[i-1]+arr1[i]
    arr.append(arr1)

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    x1,y1,x2,y2= x1-1,y1-1,x2-1,y2-1
    ans=0
    for i in range(y1,y2+1):
        if x1>0:
            ans+=arr[i][x2]-arr[i][x1-1]
        else:
            ans+=arr[i][x2]
    print(ans)
    
    
