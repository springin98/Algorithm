from sys import stdin

s = stdin.readline().rstrip()

def is_alpha(c): # 1: 소문자, 2: 대문자, 3: 알파벳 아님
    if c>='a' and c<='z':
        return 1
    if c>='A' and c<='Z':
        return 2
    
    return 0

def snake_to_camel(arr: list[str]):
    ret = ''

    for a in arr:
        if ret == '':
            ret += a
            continue
        
        ret += a[0].upper() + a[1:]

    return ret

def camel_to_snake(s: str):
    ret = ''

    for i in range(len(s)):
        if is_alpha(s[i]) == 2:
            ret += '_'
            ret += s[i].lower()
            continue
        
        ret += s[i]

    return ret
            

# main
flag = True
if not is_alpha(s[0]) or not is_alpha(s[-1]):
    flag = False
    print('Error!')
elif is_alpha(s[0]) == 2:
    flag = False
    print('Error!')

is_snake = False
is_camel = False
if flag:
    for i in range(len(s)):
        if s[i] == '_':
            if not is_snake and not is_camel:
                is_snake = True
            elif is_camel:
                print('Error!')
                flag = False
                break
        elif is_alpha(s[i]) == 2:
            if not is_snake and not is_camel:
                is_camel = True
            elif is_snake:
                print('Error!')
                flag = False
                break
        
if flag:
    for i in range(1, len(s)-1):
        if s[i] == '_':
            if not is_alpha(s[i-1]) or not is_alpha(s[i+1]):
                flag = False
                print('Error!')
                break

if flag:
    arr = s.split('_')

    if len(arr) == 1:
        print(camel_to_snake(arr[0]))
    else:
        print(snake_to_camel(arr))