
n,m = map(int,input().split())
arr=list(map(int,input().split()))
check=[0 for _ in range(m)]
check[arr[0]%m]+=1
ans=0

for i in range(1,len(arr)):
    arr[i]=(arr[i-1]+arr[i])%m # 어차피 중요한 것은 M으로 나눈 나머지니까
    check[arr[i]]+=1
# 여기서 이중 반복문으로 연속되는 것들의 합 n**2 /2 n이 10의 6승까지니까 안됨

# 다른 방법을 생각해야됨.
# 나머지가 같은 것끼리 묶어서 계산 해보자. 어떻게? 근데 애초에 각각이 m으로 나눠지는 것도 고려해야됨
# 나머지가 1인 것이 3개 있다면 ? 3combination2 
# 맨 처음이나 나중이면 달라지는게 있나? 맨 처음이면 각각이 m으로 나눠지는 것까지 들어가는거네
# 그냥 누적합도 고려해야되네
ans+=check[0]
for i in check:
    if i>1:
        ans+=int(i*(i-1)/2)
        
print(ans)

