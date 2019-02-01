def section_4(n):
    global number
    if n == 1:
        number = 1
        print(int(number))
    else:
        section_4(n - 1)
        number = n * ((n + 1) / 2)
        print(int(number))

while(1):
    number = 0
    x = int(input("Number: "))
    section_4(x)
