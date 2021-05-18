from math import sqrt

def is_prime(n):
    result = True
    if n%2 == 0:
        return(False)
    for i in range(3,int(sqrt(n)) + 1,2):
        if n%i == 0:
            result = False
            break
    return(result)

def f(n):
    binary_string_n = bin(n)[2:]
    binary_string_rev = binary_string_n[::-1]
    binary_rev_num = int(binary_string_rev,2)
    return(n - binary_rev_num)

no_of_terms = int(input('enter how many terms do you want\n'))

count,current = 1,3

primes,y_cor = [1],[1]

while (no_of_terms > count):
    if is_prime(current) == 1:
        primes.append(current)
        y_cor.append(f(current))
        count += 1
    current += 1

print('n\tprime\tf(prime)')

for i in range(no_of_terms):
    print('{}\t{}\t{}'.format(i+1,primes[i],y_cor[i]))
