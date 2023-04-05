def solution(n):
    primes = [0] * (n+1)
    primes[0] = 1
    primes[1] = 1
    
    for i in range(2, n+1):
        if(primes[i]): 
            continue
        
        for j in range(2*i, n+1, i):
            primes[j] = 1;
    
    return primes.count(0)
    