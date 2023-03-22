from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1) if direction=='right' else numbers.rotate(-1)
    return list(numbers)