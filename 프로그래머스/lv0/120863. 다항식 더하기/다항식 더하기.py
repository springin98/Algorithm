def solution(polynomial):
    polynomial = list(polynomial.split(' + '))
    x = 0
    n = 0
    
    for i in polynomial :
        if 'x' in i :
            list_x = list(map(int, [1 if j=='' else j for j in i.split('x')]))
            x += list_x[0]
        else :
            n += int(i)
            
    if n == 0 and x == 1:
        return 'x'
    elif n == 0:
        return str(x)+'x'
    elif x == 0 :
        return str(n)
    elif x == 1 :
        return 'x + '+str(n)
    else :
        return str(x)+'x + '+str(n)