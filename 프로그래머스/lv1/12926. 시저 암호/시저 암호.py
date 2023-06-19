def solution(s, n):
    answer = ""
    print('a: ', ord('a'))
    print('z: ', ord('z'))
    print('A: ', ord('A'))
    print('Z: ', ord('Z'))
    for i in s :
        if i == " ":
            answer += " "
        else:
            if ord(i) <= 90 and ord(i)+n > 90:
                answer += chr(ord(i)+n-26)
            elif ord(i) <= 122 and ord(i)+n > 122:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        
    return answer