import sys
s=sys.stdin.readline().rstrip()
arr=[[0 for _ in range(26) ] for _ in range(len(s))]
arr[0][ord(s[0])-97]+=1 
for i in range(1,len(s)):
    num=ord(s[i])-97   # 문자
    arr[i]=arr[i-1][:]  # 리스트를 그냥 arr[i]=arr[i-1]로 하면 모든 것들이 똑같아짐 
    arr[i][num]+=1 # 누적합을 만들었음 . 
    
t=int(sys.stdin.readline())

for _ in range(t):
    alp , l ,r = sys.stdin.readline().split() # 문자열로 인식해서 int 처리 해줘야 함
    l,r=int(l),int(r)
    point=ord(alp)-97
    if l>0: 
        ans=arr[r][point]-arr[l-1][point]
    else:
        ans=arr[r][point] 
    print(ans)

