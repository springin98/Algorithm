def solution(left, right):
#     answer = 0;
    
#     for i in range(left, right+1) :
#         if left == 1 :
#             answer -= 2
#         answer += i
#         for j in range (2, i//2) :
#             if j*j == i :
#                 answer -= i*2
        
#     return answer
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer