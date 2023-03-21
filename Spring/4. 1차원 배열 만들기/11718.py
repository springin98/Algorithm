import sys

while True :
    try :
        print(sys.stdin.readline().strip())
    except EOFError:
        break
    
# 이렇게 sys를 사용하면 출력 초과가 뜬다.
# https://phin09.tistory.com/18
# readline()이 EOF 에서 return 하는 건 에러가 아니라 빈 문자열이라 except로 빠지지 않는다.

# sys를 사용하고 싶으면
while True:
    line = sys.stdin.readline().rstrip()
    if line != "":
        print(line)
    else:
        break
# 방법이 있긴 하지만 우측 공백이 포함되어 있거나 빈 문자열이 있으면 안되기 때문에 여기서는 그냥 input()을 사용해라.
# 반드시 sys를 고집할 필요는 없다. 실제로 차이가 많이는 안나더라.

# 못 품
# 이유 : while 문, try&except 생각을 못함. EOFEError 도 처음 봄
# EOFError : 입력이 끝남