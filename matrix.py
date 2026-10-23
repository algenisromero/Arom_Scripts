#!/usr/bin python3

import sys
import time
import os
import random
import shutil

# --- CONFIGURATION & CHARACTER POOL ---
# Define the characters used for the digital rain (letters, numbers, symbols)
CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+-<>/"


def get_random_char():
    """Returns a single random character from our character pool."""
    return random.choice(CHARACTERS)


def type_command(command, delay=0.08):
    """Phase 1: Simulates a user typing out the command line-by-line."""
    for char in command:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(0.5)  # Dramatic pause before clearing the screen
    print()          # Move down to a fresh line


def clean_screen():
    """Phase 2: Clears the terminal screen securely across Windows and Mac/Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def run_matrix_rain():
    """Phase 3: The core animation engine for the Matrix digital rain."""

    # Grab the current dimensions of the terminal window
    terminal_size = shutil.get_terminal_size()
    max_lines = terminal_size.lines
    max_columns = terminal_size.columns

    # Create a list tracking the Y (row) position for every single column.
    # We initialize them with random negative numbers so they stagger their entry.
    drops = [random.randint(-80, 0) for _ in range(max_columns)]

    try:
        # Set the text color to Matrix Green using ANSI escape codes (\033[32m)
        sys.stdout.write("\033[32m")

        while True:
            # Loop through every individual column across the screen width
            for col in range(len(drops)):
                row = drops[col]

                # 1. DRAW THE HEAD: If the drop is currently visible on screen
                # (keeping it 2 rows short of max_lines to prevent terminal auto-scrolling)
                if 0 <= row < max_lines - 2:
                    char = get_random_char()
                    # \033[{row};{col + 1}H moves the cursor to specific coordinates, then prints the green char
                    sys.stdout.write(f"\033[{row};{col + 1}H{char}")

                # 2. ERASE THE TAIL: Clear out characters a fixed distance behind the head
                # (e.g., 12 rows behind) so it looks like a falling streak instead of a solid line
                tail_row = row - 12
                if 0 <= tail_row < max_lines - 2:
                    sys.stdout.write(f"\033[{tail_row};{col + 1}H ")

                # 3. MOVE DROP DOWN: Advance the drop position downward for the next frame
                drops[col] += 1

                # 4. RESET DROP: If the entire drop (including its tail) falls past the screen,
                # send it back to a random position above the screen to fall again.
                if drops[col] - 12 > max_lines:
                    drops[col] = random.randint(-30, 0)

            # Flush the output buffer so all column updates render simultaneously
            sys.stdout.flush()

            # Control the animation frame rate (50 milliseconds per frame)
            time.sleep(0.05)

    except KeyboardInterrupt:
        # Safety catch when user presses Ctrl+C
        # Reset text color back to default white/system default (\033[0m) and show cursor
        sys.stdout.write("\033[0m\033[?25h")
        clean_screen()
        print("\nExiting Matrix...")


# --- SCRIPT EXECUTION ---
# Run Phase 1: Type out command
type_command('$ matrix -2020')

# Run Phase 2: Wipe screen clean
clean_screen()

# Run Phase 3: Launch the Matrix rain simulation
run_matrix_rain()
