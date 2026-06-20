# Imports
import customtkinter as ctk
import tkinter as tk
import time
import os
from tkinter import filedialog, messagebox
import csv
from PIL import Image
#import god as pleasesavethisproject

# Themes
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Screen information
winfo = tk.Tk()
winfo.withdraw()
print(winfo.winfo_screenwidth())

# Default state
logged_in = False

# Login window
class HelloEverybodyMyNameIsMarkiplier(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hello everybody my name is markiplier")
        self.geometry(f"500x360+" + str((winfo.winfo_screenwidth() - 600)) + "+" + str((winfo.winfo_screenheight() / 2 - 250)))
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
                        AndWelcomBackToFiveNightsAtFreddys().mainloop()
                if self.logged_in != True:
                    self.check_label.configure(text = "Incorrect username or password") # Changes text when incorrect username or password is entered.
                
    
    def _login_build_ui(self):
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill=ctk.X, padx=(260,20), pady=(30, 0))
        self._login_build_inputs()
    
    def _login_build_inputs(self):
        self.login_label = ctk.CTkLabel(self.frame_input, text = """Hello everybody my name
is Markiplier and
welcome back to Five
Nights At Freddy's""").grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "n")
        self.username_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Username")
        self.username_input.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = "n")
        self.password_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Password")
        self.password_input.grid(row = 2, column = 0, padx = 20, pady = 5, sticky = "n")
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, text = "bite of 87", command=self.button_pressed)
        self.button.grid(row = 4, column = 0, padx = 20, pady = 20, sticky = "n")
        self.check_label = ctk.CTkLabel(self.frame_input, text = "Input username and password", anchor = "w", justify = "left")
        self.check_label.grid(row = 3, column = 0, padx = 20, pady = 0, sticky = "n")
        
class AndWelcomBackToFiveNightsAtFreddys(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("butcheks")
        self.geometry("500x600+700+50")
        self.resizable(False, False)
        self.main_screen_build()
    def main_screen(self):
        profiles = ['1', '2', '3']
        profile_checker = ctk.CTkComboBox(self.frame_main, values = profiles)
        profile_checker.pack()
    def main_screen_build(self):
        self.frame_main = ctk.CTkFrame(self)
        self.frame_main.pack(fill=ctk.X, padx=(260,20), pady=(30, 0))
        self.main_screen()

if __name__ == "__main__":
    markiplier = HelloEverybodyMyNameIsMarkiplier()
    markiplier.mainloop()
