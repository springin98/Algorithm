def solution(my_string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    answer =  [int(i) for i in my_string if (i in numbers)]
    answer.sort()
    return (answer)