def fogJump(X,Y,D):
    distance = Y - X
    if distance % D == 0:
        num = distance // D
    else:
        num = (distance // D) + 1
    return num


X = 10
Y = 85
D = 30
print(fogJump(X,Y,D))
