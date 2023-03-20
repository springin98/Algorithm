def solution(array, height):
    cnt = 0
    for i in range(0, len(array)) :
        if array[i] > height :
            cnt += 1
    return cnt