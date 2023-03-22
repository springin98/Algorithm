def solution(cipher, code):
    listCipher = list(cipher)
    answer = []
    for i in range(len(listCipher)) :
        if (i+1)%code == 0 :
            answer.append(listCipher[i])
    return (''.join(answer))