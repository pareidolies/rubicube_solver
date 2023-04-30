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

def assign_column(arr1, arr2, col):
    for i in range(len(arr1)):
        arr1[i][col] = arr2[i][col]

def copy_2d_array(arr):
    """Create a copy of a 2D array."""
    return [row.copy() for row in arr]

class RubiksCube:

    def __init__(self):
        self.top = fill('w')
        self.left  = fill('o')
        self.front  = fill('g')
        self.right  = fill('r')
        self.back  = fill('b')
        self.bottom = fill('y')

    def print(self):
        print(" TOP")
        print(self.top)
        print(" LEFT")
        print(self.left)
        print(" FRONT")
        print(self.front)
        print(" RIGHT")
        print(self.right)
        print(" BACK")
        print(self.back)
        print(" BOTTOM")
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

    
    def horizontal_twist(self, row, direction):
    # row : integer representing which row you would like to twist
    # direction : boolean representing if you want to twist right or left [left = 0, right = 1]
        if direction == 1:
            tmp_right = self.right[row]
            self.right[row] = self.front[row]
            tmp_back = self.back[row]
            self.back[row] = tmp_right
            tmp_left = self.left[row]
            self.left[row] = tmp_back
            self.front[row] = tmp_left

        if direction == 0:
            tmp_right = self.right[row]
            self.right[row] = self.back[row]
            tmp_front = self.front[row]
            self.front[row] = tmp_right
            tmp_left = self.left[row]
            self.left[row] = tmp_front
            self.back[row] = tmp_left

    def vertical_twist(self, col, direction):
    # column : integer representing which column you would like to twist
    # direction : boolean representing if you want to twist up or down [down = 0, up = 1]
        if direction == 0:
            tmp_bottom = copy_2d_array(self.bottom)
            assign_column(self.bottom, self.front, col)
            tmp_back = copy_2d_array(self.back)
            assign_column(self.back, tmp_bottom, col)
            tmp_top = copy_2d_array(self.top)
            assign_column(self.top, tmp_back, col)
            assign_column(self.front, tmp_top, col)

        if direction == 1:
            tmp_top = copy_2d_array(self.top)
            assign_column(self.top, self.front, col)
            tmp_back = copy_2d_array(self.back)
            assign_column(self.back, tmp_top, col)
            tmp_bottom = copy_2d_array(self.bottom)
            assign_column(self.bottom, tmp_back, col)
            assign_column(self.front, tmp_bottom, col)

    #def side_twist(self, column, direction):
    # column : integer representing which column you would like to twist
    # direction : boolean representing if you want to twist up or down [down = 0, up = 1]

    #def shuffle():

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
