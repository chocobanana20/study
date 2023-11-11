n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
blue=0
white=0
def solution(x,y,n):
    global blue,white
    check = arr[x][y]
    for i in range(x,x+n):
        for k in range(y,y+n):  # y,x+n으로 잘못써서 한참 찾았네 정신차려
            if check!=arr[i][k]:
                solution(x,y,n//2)
                solution(x+n//2,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y+n//2,n//2)
                return # 함수를 나가게 해줌
                
    if check==1:
        blue+=1
    else:
        white+=1
solution(0,0,n) 
print(white)
print(blue)

# 분할정복 재귀를 이용해서 절반으로 나눠서 확인하기