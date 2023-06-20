def solution(sizes):
    maxSize = [max(map(max, sizes)), 0]
    for i in sizes:
        if min(maxSize) < min(i):
            maxSize[1] = min(i)
            
    return maxSize[0]*maxSize[1]