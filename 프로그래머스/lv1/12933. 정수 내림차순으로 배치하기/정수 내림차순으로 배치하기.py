def solution(n):
    n = sorted(list(map(int, list(str(n)))), reverse = True)
    n = int(''.join(map(str, n)))
    
    return n