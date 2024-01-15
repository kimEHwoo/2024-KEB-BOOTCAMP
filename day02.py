dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec,octal,hexadecimal,binary)
print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
#chr은 ASCII코드로 보여주는 함수이다. 결과는 A
print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
print(ord('B'), ord('Z'),ord('a'), ord('2')) #66,90,97,50