from sys import stdin
from itertools import combinations_with_replacement

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()
cands = list(combinations_with_replacement(arr, m))

for cand in cands:
    print(*cand)

