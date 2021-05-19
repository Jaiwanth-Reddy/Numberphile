from math import sqrt

num = int(input('enter how many terms you want\n'.title()))

no_of_terms_found = 1

record = 1

current_no = 2

anti_primes = [1]
divisors_of_anti_primes = [[1]]

def get_divisors(n):
    divisors = []
    for i in range(1,int(sqrt(n)) + 1):
        if n%i == 0:
            if i*i == n:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n/i))
    return(divisors)

while (num > no_of_terms_found):
    current_divisors = get_divisors(current_no)
    
    if len(current_divisors) > record:
        record = len(current_divisors)
        anti_primes.append(current_no)
        divisors_of_anti_primes.append(sorted(current_divisors))
        no_of_terms_found += 1
    
    current_no += 2

for i in range(num):
    print(anti_primes[i],divisors_of_anti_primes[i])