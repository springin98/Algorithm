def solution(my_string):
    my_string = list(my_string)
    answer = []
    for i in my_string:
        if i not in answer :
            answer.append(i)
            
    return (''.join(answer))