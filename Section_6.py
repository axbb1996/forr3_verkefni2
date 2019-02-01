def section_6(n):
    global number
    if((x % n == 0) and (y % n == 0)):
        number = n
    else:
        section_6(n - 1)

while(1):
    number = 0
    x = int(input("First number: "))
    y = int(input("Second number: "))

    if x > y:
        n = y
    else:
        n = x

    section_6(n)
    print(number)
