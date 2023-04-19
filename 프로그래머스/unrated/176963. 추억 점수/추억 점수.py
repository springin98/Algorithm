def solution(name, yearning, photo):
    
    answer = []
    name_dic = {}
    
    for i in range(0, len(name)) :
        name_dic[name[i]] = yearning[i]
        
    for i in photo:
        sum = 0
        for j in i :
            if name_dic.get(j) != None :
                sum += name_dic.get(j)    
        answer.append(sum)
        
    return answer