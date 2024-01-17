#Assignment (add prime series program)

while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3)prime1	4)prime2	5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
	elif menu == '3':
		pass
	elif menu == '4':
		pass

    elif menu == '5':
        print('Terminate Program.')
        break
	else:
		print('Invalid Menu')