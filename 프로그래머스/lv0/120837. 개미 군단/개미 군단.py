def solution(hp):
    ant5 = int(hp/5)
    ant3 = int((hp%5)/3)
    return ant5+ant3+hp-ant5*5-ant3*3