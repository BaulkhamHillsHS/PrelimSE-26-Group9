# Imports
import customtkinter as ctk
import tkinter as tk
import time
import os
from tkinter import filedialog, messagebox
#import god as pleasesavethisproject

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

import csv

class HelloEverybodyMyNameIsMarkiplier(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hello everybody my name is markiplier")
        self.geometry("500x600+700+50")
        self.resizable(False, False)
        self._login_build_ui()
    
    def button_pressed(self):
        name = self.username_input.get()
        print(name)
    
    def _login_build_ui(self):
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill=ctk.X, padx=20, pady=(20, 10))
        self._login_build_inputs()
    
    def _login_build_inputs(self):
        self.username_input = ctk.CTkEntry(self.frame_input, width=160, placeholder_text="Username")
        self.username_input.grid(row = 2, column = 2, padx = 20, pady = 20)
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, text = "bite of 87", command=self.button_pressed)
        self.button.grid(row = 3, column = 2, padx = 20, pady = 20)

if __name__ == "__main__":
    markiplier = HelloEverybodyMyNameIsMarkiplier()
    markiplier.mainloop()    