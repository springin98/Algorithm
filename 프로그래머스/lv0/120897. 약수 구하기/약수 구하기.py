def solution(n):
    list = ([i for i in range(1, n+1) if n%i == 0])
    list.sort()
    return list