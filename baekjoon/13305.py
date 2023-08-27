n=int(input())
len_arr = list(map(int,input().split()))
price_arr = list(map(int,input().split()))


min_price=price_arr[0]
price=len_arr[0]*min_price
for i in range(1,len(len_arr)):  #price_arr가 인덱스는 하나 더 많지만 그건 필요없는 인덱스임으로
    if min_price>=price_arr[i]:
        min_price=price_arr[i]
    price+=min_price*len_arr[i]

print(price)