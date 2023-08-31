n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

count1,count0,count_1=0,0,0 
def solution(x,y,n):
    global count1 , count0 , count_1
    check=arr[x][y]
    check1=True
    
    for i in range(x,x+n):
        for k in range(y,y+n):
            
            if check!=arr[i][k]:
               
                n=n//3
                solution(x,y,n)
                solution(x+n,y,n)
                solution(x+2*n,y,n)
                solution(x,y+n,n)
                solution(x+n,y+n,n)
                solution(x+2*n,y+n,n)
                solution(x,y+2*n,n)
                solution(x+n,y+2*n,n)
                solution(x+2*n,y+2*n,n)
                
                check1=False
                break
    if check1:
        if check==0:
            count0+=1
        elif check==1:
            count1+=1
        else:
            count_1+=1
            
    return

solution(0,0,n)
print(count_1)
print(count0)
print(count1)
        
    
    