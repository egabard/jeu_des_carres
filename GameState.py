"""
Projet de programmation 2022 - 2023
Gabard Enzo
Jeu des carrés (ou pipopipette)
"""

"""Quelques caractères utiles"""
#Point centré ·
#Ligne horizontal non-tracée ┈
#Ligne horizontale tracée ─
#Ligne verticale non-tracée ┊
#Ligne verticale tracée |
#Grille 2x2 vide "·┈·┈·\n┊ ┊ ┊\n·┈·┈·\n┊ ┊ ┊\n·┈·┈·"


"""On définie les classe qui serviront au jeu"""
class line:
    """Cette classe contient toutes les informations sur une ligne
    Attributs:
    ----------
    
    
    """
    def __init__(self, starting_point : tuple, ending_point : tuple):
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.state = 0 #0 = pas encore tracé ; 1 = tracé
        self.related_squares_list = []

class square:
    """Cette classe contient toutes les informations sur un carré qui compose le plateau
    Attributs:
    ----------
    top_left_corner : tuple of (int, int)
        Le coin supérieur gauche du carré, qui permet également de moyen d'identification
        
    state : int
        L'état du carré (s'il à été complété ou non)
        
    borders : list of lines objects
        La liste des lignes qui sont les bordures de ce carré
    """
    def __init__(self, top_left_corner : tuple, borders : list):
        self.top_left_corner = top_left_corner
        self.state = 0 #0 = pas remporté ; 1 = remporté
        self.borders = borders
    
class board:
    """Cette classe contient toutes les informations sur l'état du plateau au cours de la partie,
    l'instance de cette classe sera un attribut de la class GameState.
    
    Attributs:
    ----------
    width : int
        La largeur du plateau qui sera choisie par l'utilisateur
    
    height : int
        La hauteur du plateau qui sera choisie par l'utilisateur
    
    points_list : list of tuple (int, int)
        La liste de tous les point qui composent le plateau
        
    lines_list : list of lines objects
        La liste de toutes les lignes qui composent le plateau
        
    squares_list : list of square objects
        La liste de tous les carrés qui composent le plateau
    
    Méthodes :
    ----------
    create_points_list()
        Créer la liste de tous les points du plateau en fonction de la largeur et la longueur du plateau
        
    create_lines_list()
        Créer la liste des lignes qui composent le plateau en fonction de la liste des points
    
    create_squares_list()
        Créer la liste des carrés qui composent le plateau en fonction de la liste des lignes
        
    create_borders(top_left_corner)
        Créer une liste des bordures qui composent le carré identifié par son coin supérieur gauche <top_left_corner>
    
    add_squares_at_lines_objects()
        Ajoute, à chaque instances de la class line (contenues dans la liste des lignes) dans son attributs related_squares, les carrés dont la ligne fait partie
    
    create_lists()
        Appelle toutes les fonctions de création de liste dans le but d'initialiser le plateau.
    
    """
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
                
        """for debugging
        print_all_points(self.points_list)"""
    
    def create_lines_list(self):
        for point in self.points_list:
            if point[0] < self.width:
            
                self.lines_list.append(line(point,(point[0]+1,point[1])))
            
                if point[1] < self.height:
                    self.lines_list.append(line(point,(point[0],point[1]+1)))
            else:
                if point[1] < self.height:
                    self.lines_list.append(line(point,(point[0],point[1]+1)))
        """for debugging
        print_all_lines(self.lines_list)"""
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
        
        """for debugging
        print_all_square_borders(self.squares_list)"""
        
    def add_squares_at_lines_objects(self):
        for square in self.squares_list:
            for line in square.borders:
                line.related_squares_list.append(square)
        """for debugging
        print_all_square_related_to_lines(self.lines_list)"""
        
    def create_lists(self):
        self.create_points_list()
        self.create_lines_list()
        self.create_squares_list()
        self.add_squares_at_lines_objects()
    
        
class game_state:
    """Cette classe contient toutes les informations sur l'état d'une partie.
    Attributs :
    ---------
    board : de longueur et de largeur choisie par l'utilisateur
        Le quadrillage sur lequel les lignes seront tracées ainsi que es carrés qu'elles composent.
        Chaque ligne peut avoir la valeur 0 dans le cas où elle n'as pas encore été tracée, ou 1 si elle l'a été.
        Chaque carré peut également avoir les même valeurs.
        
    hasWon :
        l'identifiant du joueur qui gagne la partie, s'il n'y a pas d'égalité.
       
    Méthodes :
    ----------
    play(line,player_id)
        Joue un coup pour le joueur avec l'identifiant <player_id> sur la ligne <line>
    
    canBePlayed(line)
        Renvoie True si la ligne <line> est déjà tracée ou non
        
    winner()
        Renvoie l'identifiant du gagnant s'il y en a un
    
    isTie()
        Renvoie True si la partie se termine sur une égalité
        
    textDisplay()
        Affiche l'état de la partie dans le terminal
    
    displayWinner()
        Affiche le gagnant de la partie
    """
    
    def __init__ (self, board_width : int, board_height : int):
        self.board = create_board(board_width, board_height)
    
"""Définition des fonctions de jeu"""
def play(line):
    


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
        
def print_all_square_related_to_lines(lines_list : list):
    for line in lines_list:
        string = f"line {line.starting_point} --> {line.ending_point}:\n"
        for square in line.related_squares_list:
            string += f"square starting at {square.top_left_corner}\n"
        print(string)
       
Board = board(2,2)
Board.create_lists()