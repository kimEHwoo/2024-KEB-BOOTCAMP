#subjects ={'python':'kim', 'c++' : 'sung', 'data structure':'kim','databsase': 'kang'}
#print("{0[python]}{0[data structure]}".format(subjects))

#prime number
number = int(input("Input number : "))
cnt =0
i=2
while i<number:
    if (number % i) == 0:
        cnt = cnt + 1
     i = i + 1
if cnt == 2:
            print(f'{number} is prime number')
else:
            print(f'{number} is not prime number')