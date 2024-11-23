n = int(input("enter the count of cities: "))
m = int(input("enter the count of airlines: "))
la = []
lc = []
ld = []
lpc = []
k = 1
o = 0
for v in range(n):
    cities = input(f"enter the city number {v + 1} : ")
    lc.append(cities)
for i in range(m):
    airlines = input(f"enter the first place number {i + 1} and destination number {i + 1} and separate them with',': ")
    e = airlines.split(",")
    la.extend(e)
for t in lc:
    print(t, ": ")
    for m in range(len(la)):
        if m % 2 == 0:
            if t == la[m]:
                o = o + 1
                ld.append(la[m + 1])
    print(o, "\n")
    for z in range(len(ld)):
        print(ld[z], '\n')
    ld.clear()
    o = 0
