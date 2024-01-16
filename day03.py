course = "2024 KEB Bootcamp"
print(course)
print(course.replace('KEB', 'Inha'))
print(course)
course = course.replace('KEB', 'Inha')
print(course)

course = "KEB 2024 KEB Bootcamp"
print(course)
course = course.replace('KEB', 'Inha', 1)
print(course)

course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.strip())
print(course.strip("!#.*"))
print(course.find('KEB')) #2
print(course.rfind('KEB')) #26
print(course.index('KEB')) #2
print(course.rindex('KEB')) #26
print(course.find('Inha')) #-1
print(course.index('Inha'))