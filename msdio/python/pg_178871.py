def solution(players, callings):
    name_rank = {}
    rank_name = {}
    
    for i in range(len(players)):
        name_rank[players[i]] = i+1
        rank_name[i+1] = players[i]
    
    for c in callings:
        # 나보다 하나 앞에있는 애 정보
        idx = name_rank[c] - 1
        name = rank_name[idx]
        
        # 앞에있는 애는 뒤로 보내기
        name_rank[name] += 1
        rank_name[idx+1] = name
        
        # 불린 애는 앞으로 보내기
        name_rank[c] -= 1
        rank_name[idx] = c
        
    ans = []
    for i in range(1, len(players) + 1):
        ans.append(rank_name[i])
        
    return ans
