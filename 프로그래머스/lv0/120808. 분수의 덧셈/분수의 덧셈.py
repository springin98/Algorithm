def solution(numer1, denom1, numer2, denom2):
    numer = 0
    denom = 0
    
    for i in range(max(denom1, denom2), denom1*denom2+1) :
        if i%denom1==0 and i%denom2==0 :
            denom = i
            break
            
            
    numer = numer1*(denom//denom1) + numer2*(denom//denom2)
    
    for i in range(min(numer, denom), 0, -1) :
        if numer%i == 0 and denom%i == 0 :
            numer = numer//i
            denom = denom//i
            break
            
    return [numer, denom]