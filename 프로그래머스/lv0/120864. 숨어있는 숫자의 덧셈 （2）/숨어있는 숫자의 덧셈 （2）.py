def solution(my_string):
    my_string = "".join([i if i.isnumeric() else ' ' for i in list(my_string)])
    return sum(list(map(int, my_string.split())))