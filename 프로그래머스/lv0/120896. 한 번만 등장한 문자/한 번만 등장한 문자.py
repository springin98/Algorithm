def solution(s):
    s = sorted(list(s))
    return (''.join([i for i in s if s.count(i) == 1]))