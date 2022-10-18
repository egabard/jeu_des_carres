import tkinter as tk
from GameState import *

class GameWindow():
    def __init__ (self,width = 1080, height = 720, title = "Jeu des carrés",root = tk.Tk()):
        self.root = root
        self.width = width
        self.height = height
        self.title = title
        
        self.init_window()
        self.select_dimensions()
        
    def init_window(self):
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        
    def select_dimensions(self):
        width_text = tk.Label("Test")
        width_text.place(relwidth = 0.05,relheight = 0.05,relx = 1-0.25-0.05,rely = 0.425)
        width = tk.Entry()
        height = tk.Entry()
        height.place(relwidth = 0.05,relheight = 0.05,relx = 1-0.25-0.05,rely = 0.425)
        width.place(relwidth = 0.05,relheight = 0.05,relx = 0.25,rely = 0.425)
        self.root.update()
        
    def init_board(self):
        pass
GW = GameWindow()
