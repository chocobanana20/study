# 배열 두개 만들어서 이거까지 하는데 하얀색 기준으로 바꿔야되는 개수 , 파란색을 기준으로 바꿔야되는 개수
# 기준이 애매하니까 0,0이 하얀색 이런식으로 가자
import sys
input=sys.stdin.readline
n , m ,t =map(int,input().split())
arr=[]
for i in range(n):
    a=input().rstrip()
    arr.append(a)

blue=[[0]*(m+1) for _ in range(n+1)]
white=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for k in range(1,m+1):
        
        if (i+k)%2==0:  
            if arr[i-1][k-1]=="W":
                blue[i][k]=1
            else:
                white[i][k]=1
        else:
            if arr[i-1][k-1]=="B":
                blue[i][k]=1
            else:
                white[i][k]=1
        white[i][k]=white[i][k]+white[i-1][k]+white[i][k-1]-white[i-1][k-1]
        blue[i][k]=blue[i][k]+blue[i-1][k]+blue[i][k-1]-blue[i-1][k-1]
        
        
ans=[]
for i in range(t,n+1):
    for k in range(t,m+1):
        check1=white[i][k]-white[i-t][k]-white[i][k-t]+white[i-t][k-t]
        check2=blue[i][k]-blue[i-t][k]-blue[i][k-t]+blue[i-t][k-t]
        ans.append(check1)
        ans.append(check2)
    
print(min(ans))
        