# math → used for calculating distance between the mouse and a target
import math

# random → used to place targets at random positions
import random

# time → used to calculate how long the game has been running
import time

# pygame → library used to create the game window, draw objects, handle mouse/keyboard events, etc.
import pygame

# Start pygame
pygame.init()


# --------------------------------------------------
# GAME WINDOW
# --------------------------------------------------

# Width and height of our game window
WIDTH, HEIGHT = 800, 600

# Create the pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Aim Trainer")


# --------------------------------------------------
# GAME SETTINGS
# --------------------------------------------------

# A new target will appear every 400 milliseconds
TARGET_INCREMENT = 400

# Create a custom pygame event for creating targets
TARGET_EVENT = pygame.USEREVENT

# Minimum distance between a target and the edge of the screen
TARGET_PADDING = 30

# Background color: RGB
BG_COLOR = (0, 25, 40)

# Player starts with 3 lives
LIVES = 3

# Height of the top information bar
TOP_BAR_HEIGHT = 50

# Font used for labels such as Time, Hits, Lives, etc.
LABEL_FONT = pygame.font.SysFont("comicsans", 24)


# --------------------------------------------------
# TARGET CLASS
# --------------------------------------------------

# A class represents the blueprint for creating targets
class Target:

    # Maximum size a target can reach
    MAX_SIZE = 30

    # How quickly the target grows/shrinks
    GROWTH_RATE = 0.2

    # Main target color
    COLOR = "red"

    # Secondary target color
    SECOND_COLOR = "white"

    # This runs whenever we create a new Target
    def __init__(self, x, y):

        # Store the target's x position
        self.x = x

        # Store the target's y position
        self.y = y

        # Target starts with size 0
        self.size = 0

        # True means the target should grow
        self.grow = True

    # Update the target's size
    def update(self):

        # If the target is about to reach its maximum size,
        # stop growing
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        # If grow is True, increase the target size
        if self.grow:
            self.size += self.GROWTH_RATE

        # Otherwise, decrease the target size
        else:
            self.size -= self.GROWTH_RATE

    # Draw the target on the game window
    def draw(self, win):

        # Draw the outside red circle
        pygame.draw.circle(
            win,
            self.COLOR,
            (self.x, self.y),
            self.size
        )

        # Draw a smaller white circle
        pygame.draw.circle(
            win,
            self.SECOND_COLOR,
            (self.x, self.y),
            self.size * 0.8
        )

        # Draw another red circle
        pygame.draw.circle(
            win,
            self.COLOR,
            (self.x, self.y),
            self.size * 0.6
        )

        # Draw the center white circle
        pygame.draw.circle(
            win,
            self.SECOND_COLOR,
            (self.x, self.y),
            self.size * 0.4
        )

    # Check whether the mouse clicked inside this target
    def collide(self, x, y):

        # Calculate the distance between:
        # mouse position → (x, y)
        # target center → (self.x, self.y)
        dis = math.sqrt(
            (x - self.x) ** 2 +
            (y - self.y) ** 2
        )

        # If the distance is smaller than the target radius,
        # the mouse is inside the target
        return dis <= self.size


# --------------------------------------------------
# DRAW THE GAME
# --------------------------------------------------

def draw(win, targets):

    # Fill the entire window with the background color
    win.fill(BG_COLOR)

    # Go through every target in the targets list
    for target in targets:

        # Draw each target
        target.draw(win)


# --------------------------------------------------
# FORMAT THE GAME TIME
# --------------------------------------------------

def format_time(secs):

    # Get the first digit of the milliseconds
    milli = math.floor(
        int(secs * 1000 % 1000) / 100
    )

    # Get the seconds
    seconds = int(round(secs % 60, 1))

    # Get the minutes
    minutes = int(secs // 60)

    # Return time in this format:
    # 00:12.4
    return f"{minutes:02d}:{seconds:02d}.{milli}"


# --------------------------------------------------
# DRAW THE TOP INFORMATION BAR
# --------------------------------------------------

def draw_top_bar(win, elapsed_time, targets_pressed, misses):

    # Draw the grey top bar
    pygame.draw.rect(
        win,
        "grey",
        (0, 0, WIDTH, TOP_BAR_HEIGHT)
    )

    # Create the time text
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}",
        1,
        "black"
    )

    # Calculate targets hit per second
    speed = round(
        targets_pressed / elapsed_time,
        1
    )

    # Create the speed text
    speed_label = LABEL_FONT.render(
        f"Speed: {speed} t/s",
        1,
        "black"
    )

    # Create the hits text
    hits_label = LABEL_FONT.render(
        f"Hits: {targets_pressed}",
        1,
        "black"
    )

    # Calculate remaining lives
    lives_label = LABEL_FONT.render(
        f"Lives: {LIVES - misses}",
        1,
        "black"
    )

    # Put the time text on the window
    win.blit(time_label, (5, 5))

    # Put the speed text on the window
    win.blit(speed_label, (200, 5))

    # Put the hits text on the window
    win.blit(hits_label, (450, 5))

    # Put the lives text on the window
    win.blit(lives_label, (650, 5))


# --------------------------------------------------
# END GAME SCREEN
# --------------------------------------------------

def end_screen(win, elapsed_time, targets_pressed, clicks):

    # Clear the screen
    win.fill(BG_COLOR)

    # Show final time
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}",
        1,
        "white"
    )

    # Calculate final speed
    speed = round(
        targets_pressed / elapsed_time,
        1
    )

    # Show final speed
    speed_label = LABEL_FONT.render(
        f"Speed: {speed} t/s",
        1,
        "white"
    )

    # Show total targets hit
    hits_label = LABEL_FONT.render(
        f"Hits: {targets_pressed}",
        1,
        "white"
    )

    # Calculate accuracy
    #
    # Example:
    # 8 hits / 10 clicks × 100 = 80%
    accuracy = round(
        targets_pressed / clicks * 100,
        1
    )

    # Show accuracy
    accuracy_label = LABEL_FONT.render(
        f"Accuracy: {accuracy}%",
        1,
        "white"
    )

    # Put the time in the center
    win.blit(
        time_label,
        (get_middle(time_label), 100)
    )

    # Put speed in the center
    win.blit(
        speed_label,
        (get_middle(speed_label), 200)
    )

    # Put hits in the center
    win.blit(
        hits_label,
        (get_middle(hits_label), 300)
    )

    # Put accuracy in the center
    win.blit(
        accuracy_label,
        (get_middle(accuracy_label), 400)
    )

    # Update the display
    pygame.display.update()

    # Keep the end screen open
    run = True

    while run:

        # Check for events
        for event in pygame.event.get():

            # If the player closes the window
            # or presses any key
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:

                # Exit the program
                quit()


# --------------------------------------------------
# FIND THE CENTER OF THE SCREEN
# --------------------------------------------------

def get_middle(surface):

    # Calculate where the text should start
    # so that it appears in the center
    return WIDTH / 2 - surface.get_width() / 2


# --------------------------------------------------
# MAIN GAME
# --------------------------------------------------

def main():

    # Controls whether the game is running
    run = True

    # List containing all active targets
    targets = []

    # Clock controls the game's FPS
    clock = pygame.time.Clock()

    # Number of targets successfully clicked
    targets_pressed = 0

    # Total number of mouse clicks
    clicks = 0

    # Number of targets missed
    misses = 0

    # Store the time when the game starts
    start_time = time.time()

    # Tell pygame to create TARGET_EVENT
    # every 400 milliseconds
    pygame.time.set_timer(
        TARGET_EVENT,
        TARGET_INCREMENT
    )

    # --------------------------------------------------
    # GAME LOOP
    # --------------------------------------------------

    while run:

        # Limit the game to 60 frames per second
        clock.tick(60)

        # Keeps track of whether the current click hit a target
        click = False

        # Get the current mouse position
        # Example: (400, 250)
        mouse_pos = pygame.mouse.get_pos()

        # Calculate how long the game has been running
        elapsed_time = time.time() - start_time

        # --------------------------------------------------
        # HANDLE EVENTS
        # --------------------------------------------------

        # Get all events that happened
        for event in pygame.event.get():

            # Player closes the window
            if event.type == pygame.QUIT:

                # Stop the game
                run = False
                break

            # A TARGET_EVENT happens every 400ms
            if event.type == TARGET_EVENT:

                # Generate a random X position
                x = random.randint(
                    TARGET_PADDING,
                    WIDTH - TARGET_PADDING
                )

                # Generate a random Y position
                #
                # We add TOP_BAR_HEIGHT so that
                # targets don't appear inside the top bar.
                y = random.randint(
                    TARGET_PADDING + TOP_BAR_HEIGHT,
                    HEIGHT - TARGET_PADDING
                )

                # Create a new target
                target = Target(x, y)

                # Add the target to our list
                targets.append(target)

            # The player clicked the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Remember that a click happened
                click = True

                # Increase total clicks
                clicks += 1

        # --------------------------------------------------
        # UPDATE TARGETS
        # --------------------------------------------------

        # Go through every target
        for target in targets:

            # Make the target grow or shrink
            target.update()

            # If the target has completely disappeared
            if target.size <= 0:

                # Remove it from the list
                targets.remove(target)

                # Count it as a miss
                misses += 1

            # If the player clicked
            # AND the click was inside this target
            if click and target.collide(*mouse_pos):

                # Remove the target
                targets.remove(target)

                # Increase successful hits
                targets_pressed += 1

        # --------------------------------------------------
        # CHECK FOR GAME OVER
        # --------------------------------------------------

        # If the player has missed 3 targets
        if misses >= LIVES:

            # Show the end screen
            end_screen(
                WIN,
                elapsed_time,
                targets_pressed,
                clicks
            )

        # --------------------------------------------------
        # DRAW EVERYTHING
        # --------------------------------------------------

        # Draw background and targets
        draw(WIN, targets)

        # Draw the top information bar
        draw_top_bar(
            WIN,
            elapsed_time,
            targets_pressed,
            misses
        )

        # Show everything we just drew
        pygame.display.update()

    # Close pygame
    pygame.quit()


# --------------------------------------------------
# START THE PROGRAM
# --------------------------------------------------

# This makes sure main() only runs
# when this file is executed directly.
if __name__ == "__main__":
    main()