from math import sqrt

num = int(input('enter how many terms you want\n'.title()))

no_of_terms_found = 1

record = 1

current_no = 2

anti_primes = [1]

def get_divisors(n):
    count = 0
    for i in range(1,int(sqrt(n)) + 1):
        if n%i == 0:
            if i*i == n:
                count += 1
            else:
                count += 2
    return(count)

while (num > no_of_terms_found):
    no_of_divisors = get_divisors(current_no)
    
    if no_of_divisors > record:
        record = no_of_divisors
        anti_primes.append(current_no)
        no_of_terms_found += 1
    
    current_no += 2

for i in range(num):
    print(i+1,anti_primes[i])