from sys import stdin

book = {}

for _ in range(int(stdin.readline())) :
    dicKey = str(stdin.readline().strip())
    if dicKey in book :
        book[dicKey] += 1
    else :
        book[dicKey] = 1
        

print(max(book, key=book.get))

# 딕셔너리에서 value가 가장 큰 key 알아내는 방법
# https://bskyvision.com/entry/python-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%97%90%EC%84%9C-value%EA%B0%80-%EA%B0%80%EC%9E%A5-%ED%81%B0-key-%EC%95%8C%EC%95%84%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95