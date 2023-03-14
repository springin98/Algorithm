import sys

#2557번
print("Hello World!")

#1000번
inputNum = sys.stdin.readline().strip().split(' ')
#strip() : 양 끝에 있는 줄바꿈과 공백 제거
print(int(inputNum[0])+int(inputNum[1]))
#형변환 필수
#성능 31256KB 44ms

#1000번 (대부분의 풀이)
num1, num2 = input().split(' ')
print(int(num1) + int(num2))
# 메모리는 이게 더 효율적이고, 시간은 동일하게 나옴
# 성능 31388KB 44ms

#1000번
num1, num2 = sys.stdin.readline().strip().split(' ')
print(int(num1) + int(num2))
#성능 31256KB 40ms