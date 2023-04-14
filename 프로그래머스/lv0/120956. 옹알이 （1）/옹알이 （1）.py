def solution(babbling):
    arrStr = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)) :
        for j in range(0, 4) :
            if arrStr[j] in babbling[i] :
                babbling[i] = babbling[i].replace(arrStr[j], ' ')
        
        babbling[i] = babbling[i].strip()
        
    return (babbling.count(''))