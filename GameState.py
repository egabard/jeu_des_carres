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
    starting point : tuple of int(int : int)
        Le point de départ de la ligne
        
    ending point : tuple of int (int, int)
        Le point d'arrivé de la ligne
        
    state : int
        L'état de la ligne (1 = tracée, 0 = pas encore tracée)
        
    related_squares_list : list of square objects
        La liste des carrées dont la ligne fait partie
    """
    def __init__(self, starting_point : tuple, ending_point : tuple):
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.state = 0
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
        self.state = 0 #0 = pas remporté ; 1 = remporté par joueur 1 ; 2 = remporté par joueur 2
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
    def __init__ (self, width : int, height : int, debug = False):
        self.debug = debug
        self.width = width
        self.height = height
        
        self.points_list = []
        self.lines_list = []
        self.squares_list = []
        
        self.create_lists()
        
    def create_points_list(self):
        for width_index in range (self.width + 1):
            for height_index in range(self.height + 1):
                self.points_list.append((width_index,height_index))
                
        if self.debug:
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
        if self.debug:
            print_all_lines(self.lines_list)
            
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
        
        if self.debug:
            print_all_square_borders(self.squares_list)
        
    def add_squares_at_lines_objects(self):
        for square in self.squares_list:
            for line in square.borders:
                line.related_squares_list.append(square)
        
        if self.debug:
            print_all_square_related_to_lines(self.lines_list)
        
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
    play(self,starting_point,ending_point,current_player_id)
        Joue un coup pour le joueur avec l'identifiant <current_player_id> sur la ligne qui part du point <starting_point> et qui arrive au point <ending_point> et renvoie True si le joueur doit rejouer, renvoie False sinon

    canBePlayed(self,line)
        Renvoie True si la ligne <line> est déjà tracée ou non
        
    winner(self)
        Renvoie l'identifiant du gagnant s'il y en a un et renvoie 0 sinon
    
    textDisplay(self)
        Affiche l\'état de la partie dans le terminal
    
    displayWinner(self)
        Affiche le gagnant de la partie
        
    isEnd(self)
        renvoie True si la partie est finie, renvoie False sinon
    
    isComplete(self,square,player_id)
        renvoie True et modifie l'état d'un carré (en lui changeant sa composante <state> avec le <player_id> du joueur qui vient de le compléter)s'il est complété, renvoie False et ne modifie pas son état sinon
    """
    
    
    def __init__ (self, board_width : int, board_height : int):
        self.board = create_board(board_width, board_height)
    
    """Définition des méthodes de jeu"""
    def play(self,starting_point,ending_point,current_played_id):
        line = find_line(starting_point,ending_point)
        if line != 1:
            if canBePlayed(line):
                line.state = 1
                for square in line.related_squares_list:
                    if isComplete_square:
                        return True
        return False
    
    def isEnd(self):
        for square in self.squares_list:
            if square.state != 0:
                return False
        return True

    def canBePlayed(self,line):
        if line.state == 0:
            return True
        return False

    def winner(self):
        player_1_points = 0
        player_2_points = 0
        for square in self.squares_list:
            if square.state == 1:
                player_1_points += 1
            else:
                player_2_points +=1
                
        if player_1_points > player_2_points:
            return 1
        if player_1_points < player_2_points:
            return 2
        
        return 0

    def textDisplay(self):
        pass
    
    def displayWinner(self):
        pass
    
    """Définitions des méthodes annexes"""
    def find_line(self,starting_point,ending_point):
        for line in self.lines_list:
            if line.starting_point == starting_point and line.ending_point == ending_point:
                return line
            
            else:
                return 1
    def isComplete(self,square,played_id):
        for line in square.borders:
            if line.state == 1:
                return False
            
        square.state = player_id
        return True

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


"""Quelques tests"""
#vérification que les carrés sont les memes instances
def verif_instances(Board):
    for line in Board.lines_list:
        number_of_squares = len(line.related_squares_list)
        for related_square in line.related_squares_list:
            for square in Board.squares_list:
                if square is related_square == False:
                    print("All squares are not the same")
                    return
    print("All squares are the same")
                
#verif_instances(Board)
                
    
