letter = input('Input a letter : ')

#vowels = {'a', 'e', 'i', 'o', 'u'} #set
vowels = "aeiou" #str

print(type(vowels))
if letter in vowels:
    print(f'{letter} is a vowel~')
else:
    print(f'{letter} is a consonant!')