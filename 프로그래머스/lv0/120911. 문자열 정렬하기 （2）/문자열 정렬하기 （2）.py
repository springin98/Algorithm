def solution(my_string):
    my_string = [chr(ord(i)+32) if ord(i)<97 else i for i in my_string ]
    my_string.sort()
    return (''.join(my_string))
