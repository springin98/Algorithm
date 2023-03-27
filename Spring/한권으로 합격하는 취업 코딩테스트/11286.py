from sys import stdin
import heapq

h =[]

for _ in range(int(stdin.readline())) :
    input = int(stdin.readline())
    if input == 0 :
        print(heapq.heappop(h)[1] if len(h) else 0)
        # 배열이 비어있는 경우 0 출력
    else :
        heapq.heappush(h, (abs(input), input))