def solution(keyinput, board):
    dir = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    result = [0, 0]
    for i in keyinput :
            result[0] += dir[i][0]
            result[1] += dir[i][1]
            if board[0]//2 < abs(result[0]) :
                result[0] -= dir[i][0]
            if board[1]//2 < abs(result[1]) :
                result[1] -= dir[i][1]
            
    return result