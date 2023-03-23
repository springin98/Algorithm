def solution(age):
    answer = []
    return (''.join([chr(97+int(i)) for i in str(age)]))