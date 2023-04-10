def solution(n, m, section):
    cur_end = 0
    
    cnt = 0
    for s in section:
        if s > cur_end:
            cnt += 1
            cur_end = s+m-1
            
    return cnt