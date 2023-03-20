def solution(my_string, letter):
    answer = [my_string[i] for i in range(len(my_string))]
    for _ in range(answer.count(letter)) :
            answer.remove(letter)
    return (''.join(answer))