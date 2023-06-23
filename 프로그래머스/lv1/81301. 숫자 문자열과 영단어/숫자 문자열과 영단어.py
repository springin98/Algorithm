def solution(s):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]
    # num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(0, len(eng)):
        s = s.replace(eng[i], num[i])
        
    return int(s)