import tkinter as tk
from GameState import *

class GameWindow():
    def __init__ (self,width = 1080, height = 720, title = "Jeu des carrés",root = tk.Tk()):
        self.root = root
        self.width = width
        self.height = height
        self.title = title

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
        
        self.draw_grid()
        
    def draw_grid(self):
         
        
        canvas_height = int(0.8 * self.height)
        canvas_width = int(0.8 * self.height)
        
        square_height = canvas_height // self.grid_height
        square_width = canvas_width // self.grid_width
        
        self.board = tk.Canvas(self.root, width = canvas_width, height = canvas_height, bg = 'black')
        self.board.place(relx= 0.25, rely = 0.0)
        
        square_border_length = min(square_height,square_width)
        
        for x in range(0, self.grid_width+1):
            for y in range (0, self.grid_height+1):
                self.board.create_oval(x*square_border_length-5,y*square_border_length-5,x*square_border_length+5,y*square_border_length+5,fill = 'white')
        
    def destroy_after_dimensions(self):
        self.width_text.destroy()
        self.height_text.destroy()
        self.width_entry.destroy()
        self.height_entry.destroy()
        self.error_label.destroy()
        self.validation_button.destroy()
        self.selection_sentence.destroy()
        
    def init_board(self):
        pass
    
if __name__ == '__main__':
    GW = GameWindow()
