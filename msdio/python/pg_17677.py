def formatting(arr):
    ret = []
    
    for s in arr:
        s = s.lower()
        ret.append(s)
            
    return ret


def split_2(str):
    ret = []
    
    for i in range(len(str)-1):
        if((('a' <= str[i+1] and str[i+1] <= 'z') or ('A' <= str[i+1] and str[i+1] <= 'Z')) and (('a' <= str[i] and str[i] <= 'z') or ('A' <= str[i] and str[i] <= 'Z'))):
            ret.append(str[i] + str[i+1])
        
    return ret


def get_intersection(arr1, arr2):
    temp1 = arr1.copy()
    temp2 = arr2.copy()
    
    if(len(temp1) > len(temp2)):
        temp = temp1
        temp1 = temp2
        temp2 = temp
    
    ret = 0
    
    for a in temp1:
        if(a in temp2):
            ret += 1
            temp2.remove(a)
            
    return ret
    

def solution(str1, str2):
    arr1 = split_2(str1)
    arr2 = split_2(str2)
    
    if(len(arr1)==0 and len(arr2)==0):
        return 65536
    
    cand1 = formatting(arr1)
    cand2 = formatting(arr2)
    
    intersection = get_intersection(cand1, cand2)
    union = len(cand1) + len(cand2) - intersection
    
    similarity = (intersection / union) * 65536
    
    return int(similarity)
    
    