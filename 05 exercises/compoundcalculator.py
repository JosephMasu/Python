principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print('principle can not be less or equal to 0')
        
while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print('rate can not be less or equal to 0')

while time <= 0:
    time = int(input("Enter the time in years : "))
    if time <= 0:
        print('time can not be less or equal to 0')

total = principle * pow(1 + rate /100, time)
print(f'Balance after {time} years is {total:.2f}')

