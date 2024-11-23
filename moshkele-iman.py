lessons_num = input("enter the number of lessons: ")
L =[]
total =[]
x = 0
count = 0
for i in range(int(lessons_num)):
    user_input = input("enter the weight of lesson and the score(a,b,c,d,e,f) of it respectively and separate them with ',' :")
    m = user_input.split(",")
    L.extend(m)
for i in range(int(lessons_num)):
    L[x] = int(L[x])
    count = count + L[x]
    if L[x + 1] == "a":
        L[x+1] = 5
    elif L[x+1] == "b":
        L[x+1] = 4
    elif L[x+1] == "c":
        L[x+1] = 3
    elif L[x + 1] == "d":
        L[x + 1] = 2
    elif L[x + 1] == "e":
        L[x + 1] = 1
    else:
        L[x+1] = 0
    a = L[x]*L[x+1]
    total.append(a)
    x = x+2
sum = sum(total)
average = sum/count
if 4<=average<5 :
    print("Your average score is B")
elif 3<=average<4 :
    print("Your average score is C")

elif 2<=average<3 :
    print("Your average score is D")

elif 1<=average<2 :
    print("Your average score is E")

elif 0<=average<1 :
    print("Your average score is F")

else :
    print("Your average score is A")