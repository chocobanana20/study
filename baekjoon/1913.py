N = int(input())
time = []


for i in range(N):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key = lambda a : (a[1], a[0]))  # 그리디 알고리즘 - 현상황에서 제일 좋은 것 (먼저 끝날 수록 좋음) (1,2 2,2 이렇게 끝나는 시간이 같다면 먼저 시작할때가 좋음)  

last_end = 0
cnt = 0

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)