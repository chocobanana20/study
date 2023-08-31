n=int(input())
arr = [list(map(int,input())) for _ in range(n)] 

    
def solution(x,y,n):
    check=arr[x][y]
    check_num=0
    for i in range(x,x+n):
        for k in range(y,y+n):
            if check!=arr[i][k]:  # 전부다 같은 것이 아니면
                
                check_num=1
                break
                
                
    if check_num==1:
        print("(",end='')
        solution(x,y,n//2)
        solution(x,y+n//2,n//2)
        solution(x+n//2,y,n//2)
        solution(x+n//2,y+n//2,n//2)  # 이차원 배열 인덱스 확인 
        print(")",end='')          
    else:
        print(check,end='')            
    
print("(",end='')
solution(0,0,n)
print(")",end='')