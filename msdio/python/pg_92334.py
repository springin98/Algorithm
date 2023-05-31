def solution(id_list, report, k):
    dict = {}
    cnt = {}
    
    # create name-set dictionary
    for id in id_list:
        dict[id] = set()
        cnt[id] = set()
        
    # report
    for re in report:
        s1, s2 = re.split()
        if s1 != s2:
            dict[s2].add(s1)
    
    # count mails
    for key in dict.keys():
        if len(dict[key]) >= k:
            for val in dict[key]:
                cnt[val].add(key)
                
    # get answer
    ans = []
    for c in cnt.keys():
        ans.append(len(cnt[c]))
        
    return ans