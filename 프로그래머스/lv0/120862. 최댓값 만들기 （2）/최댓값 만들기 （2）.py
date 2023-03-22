def solution(numbers):
    numbers.sort()
    multi = numbers[-1]*numbers[-2]
    if numbers[0]*numbers[1] > multi :
        multi = numbers[0]*numbers[1]
    return multi