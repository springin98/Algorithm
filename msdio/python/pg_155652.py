def solution(s, skip, index):
    alp = [chr(97+i) for i in range(26)]
    length = len(s)
    
    ans = ''
    for ch in s:
        start = (ord(ch) - ord('a') + 1) % 26

        idx = start
        added = 0
        while added < index:
            if(alp[idx] in skip):
                idx = (idx+1) % 26
                continue
                
            added += 1
            idx = (idx+1) % 26
            
        ans += alp[idx-1]
    
    return ans
    