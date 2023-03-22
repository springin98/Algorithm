def solution(my_string):
    answer = list(my_string)
    for i in range(len(answer)) :
        if answer[i] > 'Z' :
            answer[i] = chr(ord(answer[i])-32)
        else :
            answer[i] = chr(ord(answer[i])+32)
    return (''.join(answer))