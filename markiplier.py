# Imports
import customtkinter as ctk
import tkinter as tk
import time
import os
from tkinter import filedialog, messagebox
import csv
#import god as pleasesavethisproject

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

logged_in = False

import csv

class HelloEverybodyMyNameIsMarkiplier(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hello everybody my name is markiplier")
        self.geometry(f"500x600+700+50")
        self.resizable(False, False)
        self._login_build_ui()
        self.logged_in = logged_in
    
    def button_pressed(self):
        global name
        global password
        name = self.username_input.get()
        password = self.password_input.get()
        self.login_confirm()
    
    def login_confirm(self):
        with open("data.csv", "r") as csv_file:
                data = csv.reader(csv_file)
                for row in data:
                    if row[0] == name and row[2] == password:
                        self.logged_in = True
                        HelloEverybodyMyNameIsMarkiplier.destroy(self)
    
    def _login_build_ui(self):
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill=ctk.X, padx=20, pady=(20, 10))
        self._login_build_inputs()
    
    def _login_build_inputs(self):
        self.username_input = ctk.CTkEntry(self.frame_input, width=160, placeholder_text="Username")
        self.username_input.grid(row = 2, column = 2, padx = 20, pady = 20)
        self.password_input = ctk.CTkEntry(self.frame_input, width=160, placeholder_text="Password")
        self.password_input.grid(row = 3, column = 2, padx = 20, pady = 20)
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, text = "bite of 87", command=self.button_pressed)
        self.button.grid(row = 4, column = 2, padx = 20, pady = 20)
        
class AndWelcomBackToFiveNightsAtFreddys(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("butcheks")
        self.geometry("500x600+700+50")
        self.resizable(False, False)
    def main_screen(self):
        pass

if __name__ == "__main__":
    markiplier = HelloEverybodyMyNameIsMarkiplier()
    markiplier.mainloop()    
    if markiplier.logged_in == True:
        markiplier = AndWelcomBackToFiveNightsAtFreddys()
        markiplier.mainloop()