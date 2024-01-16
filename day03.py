#subjects ={'python':'kim', 'c++' : 'sung', 'data structure':'kim','databsase': 'kang'}
#print("{0[python]}{0[data structure]}".format(subjects))

#prime number
number = int(input("Input number : "))
is_prime = True #int -> bool
i = 2
while i < number:
    if (number % i) == 0:
        is_prime = False # remove +
        break
        #print(i, end=' ')
    i = i + 1

#if cnt == 0:
if is_prime:
            print(f'{number} is prime number')
else:
            print(f'{number} is not prime number')