# weght convertor


weigth = float(input("Enter your weigth: "))
unit = input("(L)bs or (K)gs: ")

if unit == "K":
    weigth = weigth * 2.205
    unit = 'Lbs'
elif unit == "L":
    weigth = weigth / 2.205
    unit = 'Kgs'
else:
    print('invalid unit {unit}')

print(f"your weigth is {weigth: .1f} {unit}")