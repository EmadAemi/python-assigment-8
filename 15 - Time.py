def menu():
    global choice
    print("1. Time Summation")
    print("2. Time Subtraction")
    print("3. Time to Seconds")
    print("4. Seconds to Time")
    print("0. Exit")
    choice = int(input())


def sum(a, b):
    hour = a['hour'] + b['hour']
    minute = a['minute'] + b['minute']
    if minute > 59:
        minute -= 60
        hour += 1
    second = a['second'] + b['second']
    if second > 59:
        second -= 60
        minute += 1
    print(hour, ":", minute, ":", second)


def sub(a, b):
    hour = a['hour'] - b['hour']
    if hour < 0:
        print("Time 2 cant be greater than Time 1")
    else:
        minute = a['minute'] - b['minute']
        if minute < 0:
            minute = 60 + minute
            hour -= 1
        second = a['second'] - b['second']
        if second < 0:
            second = 60 + second
            minute -= 1
        print(hour, ":", minute, ":", second)


def time2sec(a):
    print(a['hour'] * 3600 + a['minute'] * 60 + a['second'])


def sec2time(a):
    hour = int(a / 3600)
    minute = int((a - hour * 3600) / 60)
    second = a - hour * 3600 - minute * 60
    print(hour, ":", minute, ":", second)


while True:
    menu()
    if choice in [1, 2]:
        a = {'hour': int(input("Time 1 - hour: ")), 'minute': int(input("Time 1 - minute: ")),
             'second': int(input("Time 1 - second: "))}
        b = {'hour': int(input("Time 2 - hour: ")), 'minute': int(input("Time 2 - minute: ")),
             'second': int(input("Time 2 - second: "))}
        if choice == 1:
            sum(a, b)
        elif choice == 2:
            sub(a, b)
    elif choice == 3:
        time2sec({'hour': int(input("hour: ")), 'minute': int(input("minute: ")),
                  'second': int(input("second: "))})
    elif choice == 4:
        sec2time(int(input("Seconds: ")))
    elif choice == 0:
        exit()
    else:
        print("Wrong Choice")
