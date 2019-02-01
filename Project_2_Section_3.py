def section_3(n):
    global number
    if n == 1:
        number += 1
    else:
        section_3(n - 1)
        number += pow(n, 2)
    return number

while(1):
    number = 0
    x = int(input("Number: "))
    print(section_3(x))
