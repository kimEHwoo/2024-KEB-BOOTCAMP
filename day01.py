base_number=int(input('Input base number : '))
exponent_number = int(input('Input exponnent : '))
print(type(base_number), type(exponent_number))
#f-string
#print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {base_number**exponent_number}')
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number ** exponent_number}')

#format function
print('밑은 {0}, 지수는 {1}, 결과 값은 {2}')
