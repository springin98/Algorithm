def solution(array, commands):
    answer = []
    for i in commands:
        if i[0] == i[1] :
            answer.append(array[i[0]-1])
        else:
            arr_index = []
            for j in range(i[0]-1, i[1]):
                arr_index.append(array[j])
            arr_index.sort()
            answer.append(arr_index[i[2]-1])
    return answer
