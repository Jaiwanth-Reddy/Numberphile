no_of_digits = int(input("Enter 3 for checking for 3 digit numbers, or 4 for 4 digits\n"))

if (no_of_digits == 3):
    kaprekar = 495
    k = 1
elif (no_of_digits == 4):
    kaprekar = 6174
    k = 10
else:
    print("Incorrect Input")

def give_next_no(dg):
    temp = len(dg)
    big,small = 0,0
    revdg = sorted(dg,reverse = True)
    for i in range(0,temp):
        big += dg[i] * pow(10,i)
        small += revdg[i] * pow(10,i)
    final = big - small
    #print("(" + str(small) + "," + str(big) + ") -> " +str(final))
    return(final)

def give_digits(n):
    dig = []
    while (n >= 1):
        dig.append(n%10)
        n = int(n/10)
    dig = sorted(dig)
    return(dig)

def count_iterations(num):
    count = 0
    while (num != kaprekar) :
        num = give_next_no(give_digits(num))
        count += 1
        if (num == 0):
            count = -1
            break
    return(count)

ex = []
#495 takes 0 steps
data = {i:0 for i in range(1,9)}

for i in range(100*k,1000*k):
    temp = count_iterations(i)
    if (temp != -1 and temp != 0): 
        print(str(i) + " takes "+ str(temp) + " steps")
        data[temp + 1] += 1
    else:
        print(str(i) + " does not follow the rule")
        ex.append(i)

del data[1]
if no_of_digits == 3:
    del data[7]
    del data[8]
print("The set of " + str(len(ex)) + " numbers which do not follow the rule are:".title() + str(ex))

print("\nDistribution of steps taken\n" + str(data))
