n , k = map(int,input().split())
arr = [i for i in range(1,n+1)]
check=0
ans=[]
while arr:
    check+=k-1
    if check>len(arr)-1:
        check=check%len(arr)
        
    ans.append(arr.pop(check))
    
    

print("<",end="")
print(*ans,sep=",",end="")
print(">")
    