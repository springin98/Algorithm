import sys

# 자료구조 : 배열과 연결 리스트
# 요세푸스 문제

# 문제 이해
# 원을 이루고 있음 & K번째를 제거해야 함 -> 연결 리스트
# N명의 사람, K번째 사람 제거
# N: 7, K: 3일 때
# 1-2-3-4-5-6-7 -> 1-2-4-5-6-7 (4가 1번째가 됨) -> 1-2-4-5-7 (7이 1번째가 됨)
#               3 제거                         6 제거
# 3-6-2-7-5-1-4 순으로 제거됨

# 근데 접근, 즉 K번째 사람한테 접근해야 하니까 연결 리스트는 O(K), 배열은 O(N)
# 자세한 건 27페이지 참조
# 아무튼 연결 리스트이든, 배열이든 시간 복잡도는 똑같다.

N, K = map(int, sys.stdin.readline().strip().split())

# 배열을 만들 때는 이렇게 사용한다.
peo = [i for i in range(1, N+1)]

pt = 0
ans = []
for _ in range(N) :
    pt += K - 1 # 3번째 [2]
    pt %= len(peo) # 2%7 = 2
    ans.append(peo.pop(pt)) # peo (1~7)에서 2를 빼고, 그 값을 ans 에 저장한다.
    print(peo)
    # print(ans)

print(f"<{', '.join(map(str, ans))}>")
# f-string : 한 번에 문자열로 처리한다.
# join 함수
# https://velog.io/@qhsh866/Python-split-join-map-%EB%AC%B8%EC%9E%90%EC%97%B4-%EA%B4%80%EB%A0%A8-%ED%95%A8%EC%88%98-%EC%A0%95%EB%A6%AC
# a = ['A', 'B', 'C', 'D']
# s1 = ','.join(a)
# s1 : A,B,C,D