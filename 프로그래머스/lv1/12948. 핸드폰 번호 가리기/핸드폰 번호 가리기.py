def solution(phone_number):
    answer = []
    
    for i in range (len(phone_number) - 4):
        answer.append("*")
        
    for i in range (len(phone_number)-4, len(phone_number)):
        answer.append(phone_number[i])
        
    return "".join(answer)