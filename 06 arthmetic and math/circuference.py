import math

raduis = float(input('Enter the raduis of a circle: '))
circuference = 2 * math.pi * raduis
area = math.pi * raduis * raduis


print(f'the circuference is {circuference: .2f} and the area is {round(area, 3)}')
