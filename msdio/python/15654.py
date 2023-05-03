from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

cands = list(permutations(arr, m))

for cand in cands:
    print(*cand)
