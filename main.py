from solver import RubiksCube

cube = RubiksCube()

cube.print()
print(cube.is_solved())

cube.horizontal_twist(1, 1)

cube.print()
print(cube.is_solved())

cube.horizontal_twist(1, 0)

cube.print()
print(cube.is_solved())