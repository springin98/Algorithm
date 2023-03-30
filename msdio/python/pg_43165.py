from collections import deque

ans = 0
def bfs(arr, target, size):
    global ans
    
    dq = deque()
    dq.append((arr[0], 1))
    dq.append((-arr[0], 1))
    
    while dq:
        psum, depth = dq.popleft()
        
        if(depth == size and psum == target):
            ans += 1
        elif(depth < size):
            dq.append((psum + arr[depth], depth + 1))
            dq.append((psum - arr[depth], depth + 1))
        

def solution(numbers, target):
    bfs(numbers, target, len(numbers))
    
    return ans
    