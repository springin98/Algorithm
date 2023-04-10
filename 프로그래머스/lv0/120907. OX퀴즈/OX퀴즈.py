def solution(quiz):
    answer = []
    
    for i in quiz :
        quiz_list = i.split()
        
        if quiz_list[1] == '-' :
            quiz_list[2] = -int(quiz_list[2])
            
        if int(quiz_list[0])+int(quiz_list[2]) == int(quiz_list[4]) :
            answer.append("O")
        else :
            answer.append("X")
        
    return answer