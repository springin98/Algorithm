from collections import deque

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = deque([])
        for j in range(n):
            if arr1[i]%2 == 0 and arr2[i]%2 == 0:
                result.appendleft(" ")
            else:
                result.appendleft("#")
            arr1[i] = arr1[i]//2
            arr2[i] = arr2[i]//2
        answer.append("".join(list(result)))
    return answer