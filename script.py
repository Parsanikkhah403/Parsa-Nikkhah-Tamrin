yo = float(input("enter the first y: "))
xo = float(input("enter the first x: "))
yt = float(input("enter the second y: "))
xt = float(input("enter the second x: "))


def slope(a, b, c, d):
    m = (d - b) / (c - a)
    return m


def arz(x, y):
    b = yo - (slope(xo, yo, xt, yt) * xo)
    return b


txt = f"y = {slope(xo, yo, xt, yt)} * x + {arz(xo, yo)} "
print(txt)
