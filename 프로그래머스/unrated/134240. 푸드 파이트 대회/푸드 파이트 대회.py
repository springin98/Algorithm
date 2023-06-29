def solution(food):
    answer =["0"]
    
    for i in range(len(food)-1, 0, -1) :
        if food[i]//2 >= 1:
            for j in range(0, food[i]//2):
                answer.append(str(i))
                answer.insert(0, str(i))

    answer = "".join(answer)
    return answer