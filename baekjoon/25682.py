# 배열 두개 만들어서 이거까지 하는데 하얀색 기준으로 바꿔야되는 개수 , 파란색을 기준으로 바꿔야되는 개수
# 기준이 애매하니까 0,0이 하얀색 이런식으로 가자
import sys
input=sys.stdin.readline
n , m ,t =map(int,input().split())
arr=[]
for i in range(n):
    a=input().rstrip()
    arr.append(a)

def solve(color):
    arr1=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for k in range(1,m+1):
        
            if (i+k)%2==0:  
                if arr[i-1][k-1]==color:
                    arr1[i][k]=1  # 파란색이어야 할 자리가 w임으로 바꿔줘야함  바꿀 필요가 없다면 0이겠지
               
            else:
                if arr[i-1][k-1]!=color:
                    arr1[i][k]=1
            arr1[i][k]=arr1[i][k]+arr1[i-1][k]+arr1[i][k-1]-arr1[i-1][k-1]
    check = []
    for i in range(t,n+1):
        for k in range(t,m+1):
            check.append(arr1[i][k]-arr1[i-t][k]-arr1[i][k-t]+arr1[i-t][k-t])
    return min(check)
         
                    #위에 주석 1또는 0 // 11660 문제처럼 구하기
                    
print(min(solve("B"),solve("W")))

# 함수로 하니까 맞았땅 ㅎㅎ 근데 함수로 한다고 해서 시간이 줄어들지는 않을꺼 같은데? 왜그러지...