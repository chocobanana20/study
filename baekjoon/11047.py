# 그리디 알고리즘으로 풀 수 있는 이유가 A1 = 1 i>=2 이면 Ai 는 Ai-1의 배수 라는 조건이 있기 때문

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