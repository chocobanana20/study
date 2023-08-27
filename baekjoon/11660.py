# 범위가 나와있지 않아서 그냥 다 더하기 하면 시간초과 될 듯
# 행을 기준으로  누적합을 이용한다면 o(행의 개수) 와 비슷할 것임으로 시간초과 나지 않을듯
# 구해야 할 개수가 10000 개나 되고 , n 도 1024 임으로 시간 초과가 난듯 
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
arr=[]
for _ in range(n):
    arr1=list(map(int,input().split()))
    arr.append(arr1)

dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for k in range(1,n+1):
        dp[i][k]=arr[i-1][k-1]+dp[i-1][k]+dp[i][k-1]-dp[i-1][k-1]
# arr만으로 가능할것같은데?

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    
    ans=dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
    print(ans)


    
# 부분을 구하기 보다 전체에서 구하기 쉬운 부분들을 빼기
# 일차원 배열처럼 행으로만 누적합을 만들었더니 어차피 나중에 열도 사용해야됨.
