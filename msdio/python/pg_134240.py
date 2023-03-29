def solution(food):
    ans = '0'
    
    for i in range(len(food)-1, 0, -1):
        food[i] = food[i] // 2
        
        adj = str(i) * food[i]
        
        ans = adj + ans + adj
        
    return ans
    
    