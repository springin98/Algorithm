def solution(balls, share):
    n = 1
    m = 1
    h = 1
    for i in range(1, balls+1) :
        n *= i
    for i in range(1, balls-share+1) :
        m *= i
    for i in range(1, share+1) :
        h *= i
    return (n/(m*h))