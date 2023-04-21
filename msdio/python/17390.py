from sys import stdin

n, q = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

psum = [0] * (n+1)
psum[1] = arr[0]
for i in range(2, n+1):
    psum[i] = psum[i-1]+arr[i-1]

for _ in range(q):
    l, r = map(int, stdin.readline().split())

    print(psum[r] - psum[l-1])
