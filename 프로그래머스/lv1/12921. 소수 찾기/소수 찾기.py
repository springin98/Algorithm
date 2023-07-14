def solution(n):
    # 에라토스테네스의 체
    isDeciaml = [False, False] + [True]*(n-1)
    primes = []
    
    for i in range (2, n+1):
        if isDeciaml[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            isDeciaml[j] = False
        
    return len(primes)