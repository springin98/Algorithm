from sys import stdin

r, c = map(int, stdin.readline().split())
arr = [list(stdin.readline().rstrip()) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = 1
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for k in range(4):
                ny = i+dy[k]
                nx = j+dx[k]

                if ny<0 or nx<0 or ny>=r or nx>=c:
                    continue
                
                if arr[ny][nx] == 'D':
                    continue
                
                if arr[ny][nx] == 'S':
                    ans = 0
                    break
                
                if arr[ny][nx] == '.':
                    arr[ny][nx] = 'D'
                
        if ans == 0:
            break
        
print(ans)
if ans:
    for a in arr:
        print(''.join(a))