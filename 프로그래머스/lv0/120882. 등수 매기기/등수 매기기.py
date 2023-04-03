def solution(score):
    grade = sorted([(i[0]+i[1])/2 for i in score], reverse = True)
    score = [(i[0]+i[1])/2 for i in score]

    return [grade.index(i)+1 for i in score]