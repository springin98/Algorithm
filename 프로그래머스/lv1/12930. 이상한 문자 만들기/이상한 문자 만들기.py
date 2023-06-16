def solution(s):
    s = s.split(' ');
    answer = ""
    
    for i in s:
        for j in range(0, len(i)):
            i = list(i)
            if j%2 == 0:
                # i[j] = i[j].upper()
                answer += i[j].upper()
            else:
                # i[j] = i[j].lower()
                answer += i[j].lower()
                
        answer += (' ')
        
    return answer[0:-1]