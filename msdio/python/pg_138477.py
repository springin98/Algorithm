import heapq

def solution(k, score):
    hq = []
    ans = []

    for s in score:
        if(len(hq) < k):
            heapq.heappush(hq, s)
        else:
            cand = heapq.heappop(hq)

            if(cand < s):
                heapq.heappush(hq, s)
            else:
                heapq.heappush(hq, cand)
                
        temp = heapq.heappop(hq)
        ans.append(temp)
        heapq.heappush(hq, temp)

    return ans