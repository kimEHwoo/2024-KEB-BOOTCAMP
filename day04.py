sugang = dict(python="kim", cpp = "sung", db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim'
# print(sugang)
# sugang['datastructure'] = 'park'
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource'))
# print(sugang.get('opensource', 'not exist'))
for subject, professor in sugang.items():
    print(f'{subject} 과목 담당교수는 {professor}입니다.')

#for k in sugang.keys(): 아래와 같은 코드 keys()는 default값이다.
for k in sugang:
    print(k)

for v in sugang.values():
    print(v)

for s in sugang.items():
    print(s)