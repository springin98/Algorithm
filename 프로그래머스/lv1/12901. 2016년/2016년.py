def solution(a, b):
    monthDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = b
    for i in range (0, a-1):
        day += monthDay[i]
        
    return week[day%7-1]