# 곱할 떄의 시간 복잡도는 o(1) n번 곱함으로 그냥 곱하면 o(n) b는 매우 큰수가 될 수 있음으로 시간 초과
# 제곱을 이용한다면 시간이 줄어 들음
# 예를 들어 32번 곱해야 될 때 16번 곱한 것의 제곱하면 시간이 많이 줄어들음
a,b,c=map(int,input().split())

def mul(a,b,c):
    if b==1:
        return a%c
    else:
        if b%2==0:
            return (mul(a,b//2,c)**2)%c  #괄호 안해도 되지만 의미 때문에
        else:
            return (mul(a,b//2,c)**2*a)%c
        

ans=mul(a,b,c)

print(ans)

# 나머지만 필요 한 것이기 때문에 a*b%c = (a%c)*(b%c)