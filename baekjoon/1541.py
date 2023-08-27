a=input().split("-")
ans=sum(list(map(int,a[0].split("+"))))

for i in range(1,len(a)):
    check=sum(list(map(int,a[i].split("+"))))
    ans-=check
    
print(ans)
    