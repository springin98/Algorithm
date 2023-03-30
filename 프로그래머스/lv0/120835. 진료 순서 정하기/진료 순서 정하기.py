def solution(emergency):
    sortE = sorted(emergency, reverse=True)
    
    return [sortE.index(i)+1 for i in emergency]