# 최소 공배수 구하기
def solution(n):
    for i in range(1, n*6) :
        if (i*6)%n == 0 :
            return i