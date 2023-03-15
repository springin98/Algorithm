import sys

while True:
    try:
      A, B = map(int, sys.stdin.readline().strip().split())
      print(A+B)
    except:
        break

# 31256KB
# 44ms