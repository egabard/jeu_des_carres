"""
Projet de programmation 2022 - 2023
Gabard Enzo
Jeu des carrés (ou pipopipette)
"""

"""On définie les classe qui serviront au jeu"""
class line:
    def __init__(self, starting_point : tuple, ending_point : tuple):
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.state = 0 #0 = pas encore tracé ; 1 = tracé

class square:
    def __init__(self, top_left_corner : tuple, borders : list):
        self.top_left_corner = top_left_corner
        self.state = 0 #0 = pas remporté ; 1 = remporté
        self.borders = borders
    
class board:
    def __init__ (self, width : int, height : int):
        self.width = width
        self.height = height
        
        self.points_list = []
        self.lines_list = []
        self.squares_list = []
        
    def create_points_list(self):
        for width_index in range (self.width + 1):
            for height_index in range(self.height + 1):
                self.points_list.append((width_index,height_index))
        """for debugging"""
        print_all_points(self.points_list)
    
    def create_lines_list(self):
        for point in self.points_list:
            if point[0] < self.width:
            
                self.lines_list.append(line(point,(point[0]+1,point[1])))
            
                if point[1] < self.height:
                    self.lines_list.append(line(point,(point[0],point[1]+1)))
            else:
                if point[1] < self.height:
                    self.lines_list.append(line(point,(point[0],point[1]+1)))
        """for debugging"""
        print_lines_list(self.lines_list)
    def create_borders(self, top_left_corner_point : tuple):
        square_borders = []
        for line in self.lines_list:
            if line.starting_point == top_left_corner_point:
                if line not in square_borders:
                    square_borders.append(line)
                for other_line in self.lines_list:
                    if ((other_line.starting_point == line.ending_point) and ((other_line.ending_point[0] == top_left_corner_point[0]+1) and (other_line.ending_point[1] == top_left_corner_point[1]+1))):
                        if other_line not in square_borders:
                            square_borders.append(other_line)
        return square_borders
    
    def create_squares_list(self):
        for point in self.points_list:
            if point[0] < self.width:
                if point[1] < self.height:
                    for line in self.lines_list:
                        if line.starting_point == point:
                            square_borders = self.create_borders(point) 
                    self.squares_list.append(square(point, square_borders))
        
        """for debugging"""
        print_all_square_borders(self.squares_list)
    def create_lists(self):
        self.create_points_list()
        self.create_lines_list()
        self.create_squares_list()
        
class game_state:
    def __init__ (self, board_width : int, board_height : int):
        self.board = create_board(board_width, board_height)
    
"""Définition des fonction de debugging"""
def print_all_points(points_list):
    for element in points_list:
        print(element)
        
def print_all_lines(lines_list):
    for line in lines_list:
        starting_point = line.starting_point
        ending_point = line.ending_point
        
        print(f"{starting_point} --> {ending_point}")
        
def print_all_square_borders(square_list):
    for square in square_list:
        string = f"square at {square.top_left_corner}:\n"
        for line in square.borders:
            starting_point = line.starting_point
            ending_point = line.ending_point
            string+=(f"{starting_point} --> {ending_point}\n")
        print(string)
        
Board = board(2,2)
Board.create_lists()