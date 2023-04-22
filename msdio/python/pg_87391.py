def solution(n, m, x, y, queries):
    queries.reverse()
    
    sy, ey = x, x
    sx, ex = y, y
    
    for [dir, dx] in queries:
        if dir == 0: # x+ 방향
            if ex+dx >= m:
                ex = m-1
            else:
                ex += dx
                
            if sx != 0:
                sx += dx
        elif dir == 1: # x- 방향
            if sx-dx < 0:
                sx = 0
            else:
                sx -= dx
                
            if ex != m-1:
                ex -= dx
        elif dir == 2: # y+ 방향
            if ey+dx >= n:
                ey = n-1
            else:
                ey += dx
                
            if sy != 0:
                sy += dx
        elif dir == 3: # y- 방향
            if sy - dx < 0:
                sy = 0
            else:
                sy -= dx
                
            if ey != n-1:
                ey -= dx
    
        if sy>=n or sx>=m or ey<0 or ex<0:
            return 0
        
    # print(sy, sx)
    # print(ey, ex)
    return (ey-sy+1) * (ex-sx+1)