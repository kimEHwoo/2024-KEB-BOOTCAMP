# 연습문제 chapter 3
# 초, 분, 시간, 일

print("What do you want to change?\n1. seconds  2.minutes   3.hours   4.days")
From = input("Enter the menu: ")

if From == '1':
    print("What do you want to change this to?\n1. seconds  2.minutes   3.hours   4.days")
    menu2 = input("Enter the menu: ")
    if menu2 == '1':
        seconds_per_seconds = input("seconds: ")
        print("seconds -> seconds = ", seconds_per_seconds)
    elif menu2 == '2':
        seconds_per_minutes = int(input("seconds: "))
        seconds_per_minutes = 60 * seconds_per_minutes
        print("seconds -> minutes = ", seconds_per_minutes)
    elif menu2 == '3':
        seconds_per_hours = int(input("seconds: "))
        seconds_per_hours = 60 * 60 *  seconds_per_hours
        print("seconds -> hours = ", seconds_per_hours)
    elif menu2 == '4':
        seconds_per_days = int(input("seconds: "))
        seconds_per_days = 60 * 60 * 24 * seconds_per_days
        print("seconds -> days = ", seconds_per_days)
    else:
        print("Invalid menu")
elif From == '2':
    print("What do you want to change this to?\n1. seconds  2.minutes   3.hours   4.days")
    menu2 = input("Enter the menu: ")
    if menu2 == '1':
        minutes_per_seconds = int(input("minutes: "))
        minutes_per_seconds = minutes_per_seconds * 60
        print("minutes -> seconds = ", minutes_per_seconds)
    elif menu2 == '2':
        minutes_per_minutes = int(input("minutes: "))
        print("minutes -> minutes = ", minutes_per_minutes)
    elif menu2 == '3':
        minutes_per_hours = int(input("minutes: "))
        minutes_per_hours = minutes_per_hours / 60
        print("minutes -> hours = ", minutes_per_hours)
    elif menu2 == '4':
        minutes_per_days = int(input("minutes: "))
        minutes_per_days = minutes_per_days / 60 /24
        print("minutes -> days = ", minutes_per_days)
    else:
        print("Invalid menu")
elif From == '3':
    print("What do you want to change this to?\n1. seconds  2.minutes   3.hours   4.days")
    menu2 = input("Enter the menu: ")
    if menu2 == '1':
        hours_per_seconds = int(input("hours: "))
        hours_per_seconds = hours_per_seconds * 60 * 24
        print("hours -> seconds = ")
    elif menu2 == '2':
        print("hours -> minutes = ")
    elif menu2 == '3':
        print("hours -> hours = ")
    elif menu2 == '4':
        print("hours -> days = ")
    else:
        print("Invalid menu")

elif From == '4':
    print("What do you want to change this to?\n1. seconds  2.minutes   3.hours   4.days")
    menu2 = input("Enter the menu: ")
    if menu2 == '1':
        print("days -> seconds = ")
    elif menu2 == '2':
        print("days -> minutes = ")
    elif menu2 == '3':
        print("days -> hours = ")
    elif menu2 == '4':
        print("days -> days =")
    else:
        print("Invalid menu")

else:
    print("Invalid menu")

# hours = int(input("Enter the hour: ", ))
#
# seconds_per_hour = 60 * 60 * hours
# print(seconds_per_hour)