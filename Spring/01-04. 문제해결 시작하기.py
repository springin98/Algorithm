1. 입출력

input() : 한 줄씩 입력받는다.
형변환 : int(input())

split() : 쪼갤 때 사용한다.
문자열.split(',', 3) : [a, b, c, d, e, f] -> ['a', 'b', 'c', 'd, e, f']

빠른 입출력 : input() 대신 sys.stdin.readline() 을 사용한다.
수십 만 개의 데이터를 입력받아야 하는 문제라도 그 데이터가 전부 한 줄에 주어지면 input()을 한 번만 호출하므로 굳이 빠른 입출력이 필요없다.

한 줄에 한 번에 받을 때
map(int, sys.stdin.readline().strip().split())

2. 자료형
Python은 변수에 담을 수 있는 범위를 초과하면 오버플로우를 발생시키지 않고 내부적으로 알아서 더 큰 자료형으로 변환시켜 줍니다.
즉, 오버플로우를 신경쓰지 않아도 됩니다.

3. 변수명
i : left / 범위에서 왼쪽
m : mid / 범위에서 중간
r : right / 범위에서 오른쪽
l : low / 범위에서 낮은 쪽
hi : high / 범위에서 높은 쪽
combi : combination / 조합들 중 하나
gr : graph / 그래프
adj : adjacent / 인접행렬 또는 인접 리스트. 그래프를 담는 변수명으로 주로 사용
d/dist : distance / 거리 또는 그래프 탐색 과정에서 시작점에서 몇 단계를 거쳐 왔는지 나타냄
tot : total / 총합 (sum : sum()이 존재하기 때문에 지양)
cnt : count / 카운트, 횟수를 세서 저장하는 변수로 사용
a/arr : array / 배열
narr : next array / 다음 배열 (변수 앞에 n이 붙으면 next 의미로 사용)
acc : accumulate / 누적합을 담는 배열
now : now / 현재 값, 그래프 탐색 과정에서 현재 방문한 노드를 나타낼 때 주로 사용
nxt : next / 다음 값, 그래프 탐색 과정에서 다음 방문할 노드를 나타낼 때 주로 사용
val : value / 값
stk : stack / 스택
ch : character / 한 글자
chk : check / 체크 배열, 주로 그래프 탐색할 때 방문 체크를 위한 배열 이름으로 사용
dq : deque / 덱
q : queue / 큐
ret : return / 함수에서 반환할 값을 담는 변수로 주로 사용
ans : answer / 문제에서 구하는 답을 담는 변수로 주로 사용
mv : move / 이동
candi : candidate / 후보, 여러 가지 후보들 중 하나를 골라야 할 경우 그 후보들을 담을 배열 이름으로 사용
recur : recursive / 재귀, 재귀 함수
sz : size / 크기

4. 리스트 컴프리헨션 : 리스트를 생성하는 방법
사용 이유
- 속도가 빠르다. (속도가 더 빠른 이유 : https://whatisand.github.io/why-fast-list-comprehension-python/)
- 코드가 간략해져 가독성이 좋다.

https://wikidocs.net/22805
[ 2*x for x in range(1, 10) ]
출력 결과
[2, 4, 6, 8, 10, 12, 14, 16, 18]

[ x for x in range(10) if x < 5 if x % 2 == 0 ]
출력 결과
[0, 2, 4]

[ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
출력 결과
[('쌈밥', '사과'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'),
 ('치킨', '사과'),
 ('치킨', '아이스크림'),
 ('치킨', '커피'),
 ('피자', '사과'),
 ('피자', '아이스크림'),
 ('피자', '커피')]

5. 삼항 연산자
- 코드가 간략해진다.
print("짝수" if num % 2 == 0 else "홀수")

print ('<') if A < B else print('>') if A > B else print('==')

6. \ ` 출력
print("\\") => \
print("\"") => "