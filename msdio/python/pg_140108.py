def solution(s):
    cur = ''
    cur_cnt = 0
    others = 0
    
    ans = 0
    for cand in s:
        if cur == '':
            cur = cand
            cur_cnt = 1
            continue
            
        if cur == cand:
            cur_cnt += 1
        else:
            others += 1
    
        if cur_cnt == others:
            ans += 1
            cur = ''
            cur_cnt = 0
            others = 0
            
    if cur:
        return ans+1
    else:
        return ans