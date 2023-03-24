def solution(n):
    return ([i for i in range(1, n+1) if n%i == 0])
    # list.sort() 어차피 1부터 순서대로 넣어지기 때문에 굳이 sort할 필요가 없다.
