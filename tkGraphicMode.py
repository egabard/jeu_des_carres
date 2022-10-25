import tkinter as tk
from GameState import *
import time

class GameWindow():
    def __init__ (self,width = 1080, height = 720, title = "Jeu des carrés",root = tk.Tk()):
        self.root = root
        self.width = width
        self.height = height
        self.title = title
        
        self.point_positions_list = []
        self.line_list = []
        
        self.init_window()
        self.start()
        
    def init_window(self):
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        
    def start(self):
        self.width_text = tk.Label(self.root, text = "Largeur")
        self.width_text.place(relwidth = 0.05,relheight = 0.05,relx = 0.3,rely = 0.35)
        self.width_entry = tk.Entry()
        self.width_entry.place(relwidth = 0.05,relheight = 0.05,relx = 0.3,rely = 0.425)
        
        
        self.height_entry = tk.Entry()
        self.height_entry.place(relwidth = 0.05,relheight = 0.05,relx = 0.65,rely = 0.425)
        self.height_text = tk.Label(self.root, text = "Hauteur")
        self.height_text.place(relwidth = 0.05,relheight = 0.05,relx = 0.65,rely = 0.35)
        
        self.validation_button = tk.Button(self.root, text = "Valider", command = lambda : self.dimensions_validations())
        self.validation_button.place(relwidth = 0.05, relheight = 0.05, relx = 0.475, rely = 0.7)        
         
        self.selection_sentence = tk.Label(self.root, text = "Veuillez choisir une largeur et une hauteur de plateau (elles doivent être comprises entre 1 et 25 inclus)")
        self.selection_sentence.place(relwidth = 1,relheight = 0.1, relx = 0,rely = 0)
    
    def dimensions_validations(self):
        width = self.width_entry.get()
        height = self.height_entry.get()
        
        if width.isdigit() and height.isdigit():
            if int(height) > 0 and int(width) > 0 and int(height) < 26 and int(width) < 26:
                self.error_label = tk.Label(self.root, text = "Il faut que les valeurs soient des entiers compris entre 1 et 25 inclus")
                self.grid_height = int(height)
                self.grid_width = int(width)
                self.start_game()
            else:
                self.selection_sentence.place_forget()
                self.error_label = tk.Label(self.root, text = "Il faut que les valeurs soient des entiers compris entre 1 et 25 inclus")
                self.error_label.place(relx = 0,relwidth = 1,rely = 0.2)
        else:
            self.error_label = tk.Label(self.root, text = "Il faut que les valeurs soient des entiers compris entre 1 et 25 inclus")
            self.selection_sentence.place_forget()
            self.error_label.place(relx = 0,relwidth = 1,rely = 0.2)
            
    def start_game(self):
        self.destroy_after_dimensions()
        
        self.init_board()
    
    def draw_grid_lines(self):
        for y in range(self.grid_height+1):
            for x in range(self.grid_width+1):
                point_position = self.find_point_position(x,y)
                if point_position != False:
                    if point_position[0] + self.square_border_length - 2 <= self.x_decalage + self.square_border_length * self.grid_width:
                        self.line_list.append(self.board.create_line(point_position[0]+6,point_position[1]+2,point_position[0]+self.square_border_length-2,point_position[1]+2,width = 5))
                    if point_position[3] + self.square_border_length - 2 <= self.y_decalage + self.square_border_length * self.grid_height:
                        self.line_list.append(self.board.create_line(point_position[0]+2,point_position[1]+6,point_position[0]+2,point_position[1]+self.square_border_length - 2,width = 5))
    def find_point_position(self,x,y):
        for point in self.point_positions_list:
            if (x,y)==point[0]:
                return point[1]
        return False
    
    def draw_grid_points(self):
         
        
        self.canvas_height = int(0.8 * self.height)
        self.canvas_width = int(0.8 * self.height)
        
        square_height = self.canvas_height // self.grid_height
        square_width = self.canvas_width // self.grid_width
        
        self.board = tk.Canvas(self.root, width = self.canvas_width, height = self.canvas_height, bg = 'white')
        self.board.place(relx= 0.25, rely = 0.0)
        
        self.square_border_length = min(square_height,square_width)
        self.x_decalage = (self.canvas_width-self.grid_width*self.square_border_length)/2
        self.y_decalage = (self.canvas_height-self.grid_height*self.square_border_length)/2
        
        for x in range(0, self.grid_width+1):
            for y in range (0, self.grid_height+1):
                x0 = self.x_decalage+(x*self.square_border_length)-2
                x1 = self.x_decalage+(x*self.square_border_length)+2
                y0 = self.y_decalage+(y*self.square_border_length)-2
                y1 = self.y_decalage+(y*self.square_border_length)+2
                
                self.board.create_oval(x0,y0,x1,y1,fill = 'green')
                
                point = (x,y)
                point_position = (x0,y0,x1,y1)
                self.point_positions_list.append((point,point_position))
                self.board.update()

    def destroy_after_dimensions(self):
        self.width_text.destroy()
        self.height_text.destroy()
        self.width_entry.destroy()
        self.height_entry.destroy()
        self.error_label.destroy()
        self.validation_button.destroy()
        self.selection_sentence.destroy()
        
    def init_board(self):
        self.draw_grid_points()
        self.draw_grid_lines()
    
    

if __name__ == '__main__':
    GW = GameWindow()