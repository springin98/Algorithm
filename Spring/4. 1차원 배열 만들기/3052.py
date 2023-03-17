import sys

remain = []

for _ in range(10) :
    n = int(sys.stdin.readline().strip())%42
    if (n in remain) == False :
        remain.append(n)

print(len(remain))

# 31256 KB
# 40ms