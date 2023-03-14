import sys

A, B = map(int, sys.stdin.readline().strip().split())

print('>') if A > B else print('<') if A < B else print('==')

#31256KB
#44ms