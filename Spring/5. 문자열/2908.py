import sys

A, B = sys.stdin.readline().strip().split()
NewA = int(A[2]+A[1]+A[0])
NewB = int(B[2]+B[1]+B[0])

print (NewA) if NewA > NewB else print(NewB)

# A[0], A[-1] = A[-1], A[0] 이게 안되는 이유는 문자열이기 때문이다.
# 문자열은 파이썬에서 상수이기 때문에 새로운 문자열을 반환시켜 줘야 한다.

# 31256KB
# 40ms