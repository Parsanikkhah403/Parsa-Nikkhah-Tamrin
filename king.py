from typing import List, Any

x = int(input("enter the count of repetition: "))


def check(p, b, s, m):
    w = 0
    while p >= len(b):
        p = p - len(b)
        while s < len(b):
            if s in m:
                w = w + 1
                s = s + 1
            else:
                s = s + 1
        s = 0
        while s < p - 1:
            if s in m:
                w = w + 1
                s = s + 1
            else:
                s = s + 1
        p = p + w
        m.append(p - 1)
        w = 0


def jay(z, y):
    l = []
    j = []
    h = y
    u = 0

    for i in range(1, z + 1):
        l.append(i)
    while len(j) < (len(l) - 1):
        check(h, l, u, j)
    g = len(l) - 1
    for c in range(g, -1, -1):
        if l[c] in j:
            l.pop(c)
    print(l)
    print(j)


for q in range(x):
    n = int(input("enter the number of rubbers: "))
    k = int(input("enter the step number: "))
    jay(n, k)
