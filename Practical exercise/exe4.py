#One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. Each day thereafter, you go out double the number of bills. How long does it take for the stack of bills to exceed the height of the tower?

bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
number_of_bills = 1
days = 1

while number_of_bills * bill_thickness < sears_height:
    days += 1
    number_of_bills *= 2
    print(f"Day {days}: {number_of_bills} bills, height: {number_of_bills * bill_thickness:.3f} meters")


print("Number of days it takes for the stack of bills to exceed the height of the Sears tower:", days)
print(f"Final number of bills  {number_of_bills}")
print(f"Final height of the stack of bills: {number_of_bills * bill_thickness:.3f} meters")
