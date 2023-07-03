def solution(s):
    s = list(s)
    answer = []
    for i in range(0, len(s)):
        result = -1
        for j in range(0, i):
            if (s[j] == s[i] and j != i):
                result = i-j
        answer.append(result)
        
    return answer