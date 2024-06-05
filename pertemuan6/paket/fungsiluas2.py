def lbalok(x, y,z):
    luas= 2 * ((x* y) + (x * z) + (y * z))
    return luas

def lkubus(x):
    luas= 6 * (x ** 2)
    return luas

def llimassegiempat(x,y):
    luas=(x ** 2) + 4 * ((0.5 * x * y))
    return luas

def lbola(x):
    import math
    luas=4 * math.pi * (x ** 2)
    return luas
    