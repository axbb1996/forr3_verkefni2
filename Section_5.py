def section_5(n):
    global number
    global sequence
    if n == 1:
        sequence += int(number[n - 1])
    else:
        section_5(n - 1)
        sequence += int(number[n - 1])

while(1):
    x = int(input("Number: "))
    number = str(x)
    sequence = 0
    section_5(len(number))
    print(sequence)
