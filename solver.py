# state="rrrwrwrgryrywwwwrwbrbggggggwowyyyyyygygbbbbbbooobooooo"

# colours = ['w', 'o', 'g', 'r', 'b', 'y'],

def fill(color):
        face = [[None for j in range(3)] for i in range(3)]
        for i in range (3):
            for j in range(3):
                face[i][j] = color
        return face

def check_face(face):
        first_element = face[0][0]
        for row in face:
            for element in row:
                if element != first_element:
                    return False
        return True

class RubiksCube:

    def __init__(self):
        self.top = fill('w')
        self.left  = fill('o')
        self.front  = fill('g')
        self.right  = fill('r')
        self.back  = fill('b')
        self.bottom = fill('y')

    def print(self):
        print(self.top)
        print(self.left)
        print(self.front)
        print(self.right)
        print(self.back)
        print(self.bottom)

    def check_face(self, face):
        first_element = face[0][0]
        for row in face:
            for element in row:
                if element != first_element:
                    return False
        return True

    def is_solved(self):
        if (check_face(self.top) & check_face(self.left) & check_face(self.front)
            & check_face(self.right) & check_face(self.back) & check_face(self.bottom)):
            return True
        return False

    #def shuffle() :

    #def horizontal_twist(my_cube, row, direction) :
    # row : integer representing which row you would like to twist
    # direction : boolean representing if you want to twist right or left [left = 0, right = 1]

    #def vertical_twist(my_cube, column, direction) :
    # column : integer representing which column you would like to twist
    # direction : boolean representing if you want to twist up or down [down = 0, up = 1]

    #def side_twist(my_cube, column, direction) :
    # column : integer representing which column you would like to twist
    # direction : boolean representing if you want to twist up or down [down = 0, up = 1]

    # step 1
    # check


    # step 2
    # check

    # step 3
    # check

    # step 4
    # check

    # step 5
    # check

    # step 6
    # check

    # step 7
    # check
