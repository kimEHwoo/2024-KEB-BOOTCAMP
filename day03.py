#prime number
numbers = (input("Input first second number : ")).split() #int형 하면 만약 21 10 넣었을 때 이게 정수형이 아니어서 안된다.
n1 = int(numbers[0])
n2 = int(numbers[1])

for number in range(n1, n2+1):
    is_prime = True

    if number < 2 :
        pass
    else :
        for i in range(2, number) :
            if (number % i) == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')