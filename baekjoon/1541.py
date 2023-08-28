# 00009 같은 문자열에 int를 처리하면 9가 됨
# 결국 더하기가 나온 부분을 먼저 처리한 후 -를 연산하면 최소가 나옴
# 그래서 -를 기준으로 split 한 후 + 연산을 진행 한 후 빼주는 방식으로 진행 하였음


a=input().split("-")
ans=sum(list(map(int,a[0].split("+"))))

for i in range(1,len(a)):
    check=sum(list(map(int,a[i].split("+"))))
    ans-=check
    
print(ans)
    