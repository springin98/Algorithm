# def solution(a, b):
#     if b%a == 0 :
#         b = b//a
        
#     while b != 1 :
#         if b%2 == 0 :
#             b = b/2
#         elif b%5 == 0 :
#             b = b/5
#         else :
#             return 2
    
#     return 1

from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2