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

# Default state
logged_in = False

profiles_and_ages = {}

# Login window
class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("[REDACTED] Login screen")
        self.geometry(f"450x340+500+200")
        self.resizable(False, False)
        self._login_ui_build()
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
                        global profiles_and_ages
                        self.logged_in = True 
                        profiles_and_ages[row[4]] = row[5]
                if self.logged_in != True:
                    self.check_label.configure(text = "Incorrect username or password") # Changes text when incorrect username or password is entered.
                else:
                    LoginWindow.destroy(self)
                    ProfileWindow().mainloop()
    
    def _login_ui_build(self):
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill = ctk.X, padx = (20,20), pady = (30, 0))
        self._login_inputs_build()

    # Builds login screen
    def _login_inputs_build(self):
        self.login_label = ctk.CTkLabel(self.frame_input, text = """Hello, welcome to [REDACTED]!
Please input your username
and password to log in.""").grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "n")
        self.username_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Username")
        self.username_input.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = "n")
        self.password_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Password")
        self.password_input.grid(row = 2, column = 1, padx = 20, pady = 5, sticky = "n")
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, text = "bite of 87", command=self.button_pressed)
        self.button.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = "n")
        self.check_label = ctk.CTkLabel(self.frame_input, text = "Input username and password", anchor = "w", justify = "left")
        self.check_label.grid(row = 3, column = 1, padx = 20, pady = 0, sticky = "n")
        
        self.login_image = ctk.CTkImage(light_image = Image.open("images/Markiplier.png"), dark_image = Image.open("images/Markiplier.png"), size = (150, 100))
        self.login_image_label = ctk.CTkLabel(self.frame_input, text = "", image = self.login_image)
        self.login_image_label.grid(row = 0, column = 0, rowspan = 5, padx = 20, pady = 20)
    

class ProfileWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("[REDACTED] Profile selection screen")
        self.geometry("500x360+500+200")
        self.resizable(False, False)
        self.background_build()
        self.main_screen_build()
    
    def background_build(self):
        self.background_image = ctk.CTkImage(light_image = Image.open("images/Background.png"), dark_image = Image.open("images/Background.png"), size = (500, 360))
        self.background_image_label = ctk.CTkLabel(self, text = "", image = self.background_image)
        self.background_image_label.place(x = 0, y = 0)
    
    def main_screen_build(self):
        self.frame_main = ctk.CTkFrame(self)
        self.frame_main.pack(fill=ctk.X, padx=(260,20), pady=(30, 0))
        self.main_screen()    
    
    def main_screen(self):
        self.name = ctk.CTkLabel(self.frame_main, padx = 20, pady = 20, text = f"Welcome back, {name}")
        self.name.pack()
        self.profile_checker = ctk.CTkComboBox(self.frame_main, values = list(profiles_and_ages.keys()), command = self.age_configure)
        self.profile_checker.pack()
        self.age = ctk.CTkLabel(self.frame_main, text = f"Age: {profiles_and_ages[self.profile_checker.get()]}")
        self.age.pack()
        self.profile_selector = ctk.CTkButton(self.frame_main, width = 100, height = 34, text = "Select profile", command = self.profile_button_pressed)
        self.profile_selector.pack(pady = 20)
        
    def age_configure(self, choice):
        print("Selected:", choice)
        self.age.configure(text=f"Age: {profiles_and_ages[choice]}")
        return choice
    
    def profile_button_pressed(self):
        print("profile button pressed")
    # should probably be used to like log into specific profiles

if __name__ == "__main__":
    markiplier = LoginWindow()
    markiplier.mainloop()
