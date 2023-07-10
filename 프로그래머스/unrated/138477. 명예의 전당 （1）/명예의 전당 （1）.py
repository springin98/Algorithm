def solution(k, score):
    answer = [];
    scoreArr = [];
    for i in range(0, len(score)):
        scoreArr.append(score[i]);
        scoreArr.sort()
        if len(scoreArr) > k:
            scoreArr.pop(0)
        answer.append(min(scoreArr))
        
    return answer