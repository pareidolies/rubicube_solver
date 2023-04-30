from solver import RubiksCube

ANSI_PURPLE = "\x1b[95m"
ANSI_BLUE = "\x1b[94m"
ANSI_YELLOW	= "\x1b[93m"
ANSI_RED = "\x1b[91m"
ANSI_GREEN = "\x1b[92m"
ANSI_CYAN = "\x1b[96m"
ANSI_RESET = "\x1b[0m"

cube = RubiksCube()

cube.print()
print(cube.is_solved())

print(ANSI_BLUE + "-HORIZONTAL TWIST!-" + ANSI_RESET)

cube.horizontal_twist(1, 1)

cube.print()
print(cube.is_solved())

cube.horizontal_twist(1, 0)

cube.print()
print(cube.is_solved())

print(ANSI_BLUE + "-VERTICAL TWIST!-" + ANSI_RESET)

cube.vertical_twist(1, 1)

cube.print()
print(cube.is_solved())

cube.vertical_twist(1, 0)

cube.print()
print(cube.is_solved())

print(ANSI_BLUE + "-SIDE TWIST!-" + ANSI_RESET)

cube.side_twist(1, 1)
cube.side_twist(1, 0)

cube.print()
print(cube.is_solved())

print(ANSI_BLUE + "-SHUFFLE-" + ANSI_RESET)

cube.shuffle()

cube.print()
print(cube.is_solved())
