from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
visited = []

def dfs(sy, sx, row, col, maps):
    visited[sy][sx] = 1    
    dq = deque()
    dq.append((sy, sx))
    
    cnt = int(maps[sy][sx])
    
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if ny<0 or nx<0 or ny>=row or nx>=col:
                continue
                
            if maps[ny][nx] == 'X' or visited[ny][nx]:
                continue
            
            visited[ny][nx] = 1
            cnt += int(maps[ny][nx])
            dq.append((ny, nx))
            
    return cnt


def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    global visited
    visited = [[0]*col for _ in range(row)]
    
    ans = []
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and not visited[i][j]:
                ret = dfs(i, j, row, col, maps)
                ans.append(ret)
    
    if not ans:
        return [-1]
    else:
        ans.sort()
        return ans