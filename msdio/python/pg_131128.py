# 시간 초과

def solution(X, Y):    
    lenX = len(X)
    lenY = len(Y)
    
    arrX = [0 for _ in range(10)]
    arrY = [0 for _ in range(10)]
    
    for i in range(lenX):
        idx = int(X[i])
        arrX[idx] += 1
    for i in range(lenY):
        idx = int(Y[i])
        arrY[idx] += 1
    
    ans_arr = []
    for i in range(10):
        ans_arr.append(min(arrX[i], arrY[i]))
    
    ans = ''
    for i in range(9, -1, -1):
        ans += (str(i) * ans_arr[i])
        
    if ans == '':
        return "-1"
    
    ans_int = int(ans)
    if ans_int == 0:
        return "0"
    else:
        return ans
    
# ------------------------------------------------------- #
def solution(X, Y):    
    lenX = len(X)
    lenY = len(Y)
    
    arrX = [0 for _ in range(10)]
    arrY = [0 for _ in range(10)]
    
    for i in range(lenX):
        idx = int(X[i])
        arrX[idx] += 1
    for i in range(lenY):
        idx = int(Y[i])
        arrY[idx] += 1
    
    ans_arr = []
    for i in range(10):
        ans_arr.append(min(arrX[i], arrY[i]))
    
    ans = ''
    for i in range(9, -1, -1):
        ans += (str(i) * ans_arr[i])
        
    if ans == '':
        return "-1"
    
    if ans[0] == "0":
        return "0"
    else:
        return ans
    
    
    