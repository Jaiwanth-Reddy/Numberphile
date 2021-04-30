def leap_year(y):
    check = False
    if (y%4 == 0) and (y%100 != 0):
        check = True
    if (y%100 == 0) and (y%400 == 0):
        check = False
    return(check)

days_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
names = ('January','February','March','April','May','June','July','August','September','October','November','December')

def get_s(year):
    count = year - 1583
    for i in range(1583,year):
        if leap_year(i) == True:
            count += 1
    count = count % 7 
    return(count) 

def print_month(s,days):                            # works perfectly!
    print('\nMon\tTue\tWed\tThur\tFri\tSat\tSun\t')
    for i in range(s):
        print('\t',end = '')
    for i in range(1,days+1):
        print(i,end='\t')
        s += 1
        if s == 7:
            print('')
            s = 0
    return(s)


def print_year(year):
    s = get_s(year)
    global days_of_month
    global names
    months = list(days_of_month)
    if leap_year(year) == True:
        months[1] = 29
    print(year)
    for i in range(12):
        print('\n\n' + str(names[i]) + ' ' + str(year))
        s = print_month(s, months[i])

inp = int(input('enter the year of you want the calender of\n'.title()))

if inp > 1852:
    print_year(inp)
else:
  print('Invalid Input')
