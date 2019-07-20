
currentNumber = 1
stop = 2
rows = int(input("Enter the number of row: "))
for i in range(rows):
    for column in range(1, stop):
        print(currentNumber, end=' ')
        currentNumber += 1
    print("")
    stop += 1
