def solution(my_string, n):
    answer = [my_string[i]*n for i in range(len(my_string))]
    return (''.join(answer))