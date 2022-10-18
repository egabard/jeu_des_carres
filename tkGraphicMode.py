import tkinter as tk
from GameState import *

class GameWindow(tk.Tk):
    def __init__ (self,width = 1080, height = 720, title = "Jeu des carrés"):
        tk.Tk().__init__(self)
        self.width = width
        self.height = height
        self.title = title
        
        self.init()
    
    def init(self):
        self.title(self.title)
        self.dimension(f"{self.width}x{self.height}")
        self.flip()
        
GW = GameWindow()
