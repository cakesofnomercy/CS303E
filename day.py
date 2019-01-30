#  File: Day.py

#  Description: This program will prompt the user to enter the day, month,
#  and year and enter the day of the week for that day.

#  Student Name: Fernando Ocon

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number:

#  Date Created: 1/25/19

#  Date Last Modified:


def main():
    # year input
    user_year = int(input("Enter year: "))
    while user_year < 1900 or user_year > 2100:
        print("Invalid year\n")
        user_year = int(input("Enter year: "))

    # Enter month, a
    a = int(input("Enter month: "))
    while a < 1 or a > 12:
        print("Invalid month\n")
        user_year = int(input("Enter month: "))

    # weird calendar adjustment
    if a > 2:
        a = a - 2
    else:
        a = a + 10

    # Day input, b
    b = int(input("Enter day: "))
    while b < 1 or b > 31:
        print("Invalid day\n")
        b = int(input("Enter day: "))

    # check for February day
    while a == 2 and b > 29:
        print("Invalid day for Feb\n")
        b = int(input("Enter day"))

    # assign c,d
    if user_year >= 1900 and user_year < 2000:
        c = user_year - 1900
    else:
        c = user_year - 2000

    d = user_year // 100

    ###########################

    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
               "Friday", "Saturday"]

    print(weekday[r] + '\n')
    print(a, b, c, d, w, x, y, z, r)


main()
