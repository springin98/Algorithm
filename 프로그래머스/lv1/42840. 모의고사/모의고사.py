def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    total = [0, 0, 0]
    answer= []
    
    for i in range (0, len(answers)):
        if answers[i] == first[i%len(first)]:
            total[0] += 1
        if answers[i] == second[i%len(second)]:
            total[1] += 1
        if answers[i] == third[i%len(third)]:
            total[2] += 1
    
    for i in range (0, len(total)):
        if total[i] == max(total):
            answer.append(i + 1)
    
    return answer
    
    # answer = sorted(list((filter(lambda i:answer[i] == max(answer), range(len(answer))))))