def solution(id_pw, db):
    if dict(db).get(id_pw[0]) :
        db_pw = dict(db).get(id_pw[0])
        return "login" if db_pw == id_pw[1] else "wrong pw"
    
    return "fail"