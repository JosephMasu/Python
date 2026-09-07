#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

rubber_ball_height = 100  # Initial height in meters
bounce_factor = 3/5  # Bounce factor
first_bounces = 10  # Number of bounces to display

for bounce in range(1, first_bounces + 1):
    rubber_ball_height *= bounce_factor  # Calculate the height after the bounce
    print(f"{bounce}\t{rubber_ball_height:.4f}")  # Print the bounce number and height

print("The height of the ball after 10 bounces is: {:.4f} meters".format(rubber_ball_height))