# 이분 탐색

# 재귀 함수 이용

# def binary_search(arr,target,start,end):
    
#     mid = (start+end)//2
#     if start>end: # 재귀함수도 끝날 때가 있어야지 못찾을 경우도 넣어 놨어야됨 .
#         return 0
#     if arr[mid]==target:
#         return 1
#     elif arr[mid]>target:
#         return binary_search(arr,target,start,mid-1)
#     else:
#         return binary_search(arr,target,mid+1,end)
        
        
        
def binary_search(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]>target:
            end=mid-1 
        else:
            start=mid+1
       
    return 0       

 
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
ans = map(int,input().split())
arr=sorted(arr)

for i in ans:
    print(binary_search(arr,i,0,len(arr)-1))
