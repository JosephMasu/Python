# neested loo, the inner loop is insaide the outer loop

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbols = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbols, end=" ")
    print()

print('--------------------------')

for rows in range(rows):
    for columns in range(columns):
        print(symbols, end=" ")
    print()

print('--------------------------')

n = 5
for b in range(n):
    for c in range(b +1):
        print("*", end=" ")
    print()
