def solution(dots):
    width = [i[0] for i in dots]
    width = list(set(width))
    height = [i[1] for i in dots]
    height = list(set(height))
    
    return ((width[1]-width[0]) * (height[1]-height[0]))