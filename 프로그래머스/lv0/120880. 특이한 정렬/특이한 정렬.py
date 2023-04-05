def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), -x))
    return answer

# lambda 라는 개념을 공부해볼 것
    

# 내가 생각했던 부분
# dict = {}
# for i in numlist :
#     dict[i] = abs(i-n)
# sorted_dict = sorted(dict.items(), key= lambda item:item[1])
# 으로 하면 딕셔너리의 value 값에 따른 내림차순이 완성됨.
# 근데 여기서부터 막힘.