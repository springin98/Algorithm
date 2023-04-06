def solution(n, m, a):
    left_dp = [[0]*(m+2) for _ in range(n+2)]
    right_dp = [[0]*m for _ in range(n+2)]
    dp = [[0]*(m+2) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(m):
            if (j <= 0): # 왼쪽 벽이 막힌 경우
                    left_dp[i][j] = a[i-1][j] + max(left_dp[i-1][j], left_dp[i][j+1])
            elif (j+1 >= m): # 오른쪽 벽이 막힌 경우
                left_dp[i][j] = a[i-1][j] + max(left_dp[i-1][j], left_dp[i][j-1])
            else:
                left_dp[i][j] = a[i-1][j] + max(left_dp[i-1][j], left_dp[i][j-1], left_dp[i][j+1])

        for j in range(m-1, -1, -1):
            if (j <= 0): # 왼쪽 벽이 막힌 경우
                right_dp[i][j] = a[i-1][j] + max(right_dp[i-1][j], right_dp[i][j+1])
            elif (j+1 >= m): # 오른쪽 벽이 막힌 경우
                right_dp[i][j] = a[i-1][j] + max(right_dp[i-1][j], right_dp[i][j-1])
            else:
                right_dp[i][j] = a[i-1][j] + max(right_dp[i-1][j], right_dp[i][j-1], right_dp[i][j+1])

        for j in range(1, m+1):
            dp[i][j] = a[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i][j+1])

            if (j > 1):
                dp[i][j] = max(dp[i][j], dp[i+1][j-1] + a[i-1][j-2])
            if (j < m+1):
                dp[i][j] = max(dp[i][j], dp[i+1][j+1] + a[i-1][j])


    cand1 = max(left_dp[n])
    cand2 = max(right_dp[n])
    cand3 = max(dp[n])

    print(dp)

    return max(cand1, cand2, cand3)

print(solution(3, 3, [[1,4,5], [3,8,2], [10, 0, 6]])) # 30
print(solution(2, 2, [[10,10],[10,10]])) # 30
print(solution(1, 2, [[0,0]])) # 0
print(solution(3, 4, [[1,4,5,1],[3,8,2,1],[0,10,6,1]])) # 33
print(solution(3, 4, [[1,1,1,1],[1,1,1,1],[1,1,1,1]])) # 9
print(solution(4,4,[[1, 4, 5,1], [1000,1, 8, 1], [10, 1,9, 6],[1, 1,1, 1]])) # 1031