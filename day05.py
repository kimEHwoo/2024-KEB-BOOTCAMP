# prime number

def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    # Assignment (add prime series program)
    while True:
        menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

        if menu == '1':
            fahrenheit = float(input('Input Fahrenheit : '))
            print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
        elif menu == '2':
            celsius = float(input('Input Celsius : '))
            print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')
        elif menu == '3':
            number = int(input("Input number : "))
            is_prime = True

            if number < 2:
                print(f'{number} is NOT prime number!')
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break

                if is_prime:
                    print(f'{number} is prime number')
                else:
                    print(f'{number} is NOT prime number!')
        elif menu == '4':
            for number in range(n1, n2 + 1):
                if isprime(number):
                print(number, end=' ')
            print()
        elif menu == '5':
            print('Terminate Program.')
            break
        else:
            print('Invalid Menu!')