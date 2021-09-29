#WRITE YOUR CODE IN THIS FILE
def close10(x,y):
    diffx= abs(x-10)
    diffy=abs(y-10)
    if diffx > diffy:
        return y
    elif diffx < diffy:
        return x
    else:
        return 0
print(close10(50,2000))