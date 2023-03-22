def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans_one = 0
    ans_two = 0
    ans_three = 0
    
    for i in range(len(answers)):
        if(one[i%5] == answers[i]):
            ans_one += 1
            
        if(two[i%8] == answers[i]):
            ans_two += 1
            
        if(three[i%10] == answers[i]):
            ans_three += 1
    
    cand = [ans_one, ans_two, ans_three]
    cand_max = max(cand)
    
    ans = []
    for i in range(3):
        if(cand[i] == cand_max):
            ans.append(i+1)
            
    return ans
            