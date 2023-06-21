def solution(t, p):
    answer = []
    t = list(t)
    for i in range(len(t)-len(p)+1):
        string = ""
        for j in range(len(p)):
            string += t[i+j]
        if (int(string) <= int(p)):
            answer.append(int(string))
        
    return len(answer)