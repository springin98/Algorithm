def solution(sides):
    cnt = 0
    for i in range(max(sides)-min(sides)+1, max(sides)+1) :
        cnt +=1
    for i in range(max(sides)+1, sides[0]+sides[1]) :
        cnt += 1
    return cnt