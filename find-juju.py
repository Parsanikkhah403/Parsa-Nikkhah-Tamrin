n = int(input("enter the count of check points: "))
l = []
x = (n-3)/2
if n%4==0 :
    print("*")
    for k in range (n-1):
        print(" _")
    print(" *")
    for i in range(n-1) :
        if i%2==0 :
            print("    ")
            for p in range(x):
                l.append("_")
                l.append(" ")
            l[i] = "*"
            l[] = "*"
elif n%4==3 :
    print("mamad")
elif n%4==2 :
    print("mamad")
else :
    print("salam")