n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
blue=0
white=0
def solution(x,y,n):
    global blue,white
    check = arr[x][y]
    for i in range(x,x+n):
        for k in range(y,y+n):
            if check!=arr[i][k]:
                solution(x,y,n//2)
                solution(x+n//2,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
                
    if check==1:
        blue+=1
    else:
        white+=1
solution(0,0,n) 
print(white)
print(blue)