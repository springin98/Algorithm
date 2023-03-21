def solution(my_string):
    answer = ([int (list(my_string)[i]) for i in range(len(list(my_string))) if ord(list(my_string)[i])-47 < 11])
    return sum(answer)