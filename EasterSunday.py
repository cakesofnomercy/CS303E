#  File: EasterSunday.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


def main():
    user_year = input("Enter year: ")

    y = int(user_year)
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    # day p in month n

    month = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]

    print("In %d Easter Sunday was on %d %s" % (y, p, month[n-1]))


main()
