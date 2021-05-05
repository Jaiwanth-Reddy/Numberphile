final = [1,2,2]

def golumb(n):
    t = final[n - 1]
    for i in range(0,t):
        final.append(n)

def loop(l):
    temp = len(l)
    for i in range(temp):
        print(i+1,l[i])

option = int(input("Enter 1 if you want first n numbers of the series\nEnter 2 if you want all numbers less than a given number\nEnter 3 if you want the nth term of the series\n".title()))

if option == 1:
    lmt = int(input("how many numbers of the sequence do you want\n".title()))
    i = 3

    while (len(final) < lmt):
        golumb(i)
        i += 1

    loop(final[:lmt])
elif option == 2:
    lmt = int(input("till what number do you want the sequence\n".title()))
    
    for i in range(3,lmt+1):
        golumb(i)
    
    loop(final)
elif option == 3:
    lmt = int(input("enter which term you want\n".title()))
    i = 3

    while (len(final) < lmt):
        golumb(i)
        i += 1

    print(final[lmt])
elif option == 4:
    print("Invalid Input")
