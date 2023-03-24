def solution(order):
    cnt = 0
    order = str(order)
    for i in order :
        if int(i) != 0 and int(i)%3==0 :
            cnt += 1
    return cnt