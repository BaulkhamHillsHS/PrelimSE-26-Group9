# Imports
import customtkinter as ctk
import tkinter as tk
from CTkListbox import *
import time
import os
from tkinter import filedialog, messagebox
import csv
from PIL import Image
#import god as pleasesavethisproject

## Movies and TV Shows
movies = {
    "The Lion King": "child",
    "Toy Story": "child",
    "Frozen": "child",
    "Moana": "child",
    "Shrek": "child",
    "Finding Nemo": "child",
    "Inside Out": "child",
    "Aladdin": "child",
    "Up": "child",
    "Kung Fu Panda": "child",
    "Harry Potter and the Sorcerer's Stone": "child",
    "The Incredibles": "child",
    "Monsters, Inc.": "child",
    "Zootopia": "child",
    "Paddington": "child",

    "The Matrix": "adult",
    "Fight Club": "adult",
    "Joker": "adult",
    "Inception": "adult",
    "Titanic": "adult",
    "Pulp Fiction": "adult",
    "The Godfather": "adult",
    "Parasite": "adult",
    "Drive": "adult",
    "Mad Max: Fury Road": "adult"
}


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
        self.title("Markiflixer Login screen")
        self.geometry(f"450x310+500+200")
        self.resizable(False, False)
        self.background_build()
        self._login_ui_build()
        self.logged_in = logged_in
    
    def background_build(self):
        self.background_image = ctk.CTkImage(light_image = Image.open("images/ui/LoginBackground.png"), dark_image = Image.open("images/ui/LoginBackground.png"), size = (450, 310))
        self.background_image_label = ctk.CTkLabel(self, text = "", image = self.background_image)
        self.background_image_label.place(x = 0, y = 0)

    def login_confirm(self):
        with open("data.csv", "r") as csv_file:
                data = csv.reader(csv_file)
                for row in data:
                    if row[0] == name and row[2] == password:
                        global profiles_and_ages
                        self.logged_in = True 
                        profiles_and_ages[row[4]] = row[5]
                if self.logged_in != True:
                    # Changes text when incorrect username or password is entered.
                    self.check_label.configure(text_color = "red", text = "Incorrect username or password")
                else:
                    LoginWindow.destroy(self)
                    MainWindow().mainloop()
    
    def _login_ui_build(self):
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill = ctk.X, padx = (20,20), pady = (20, 0))
        self._login_inputs_build()

    # Builds login screen
    def _login_inputs_build(self):
        self.login_label = ctk.CTkLabel(self.frame_input, text = """Hello, welcome to Markiflixer!
Please input your username
and password to log in.""").grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "n")
        self.username_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Username")
        self.username_input.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = "n")
        self.password_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Password")
        self.password_input.grid(row = 2, column = 1, padx = 20, pady = 5, sticky = "n")
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, text = "Log in", command=self.button_pressed)
        self.button.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = "n")
        self.check_label = ctk.CTkLabel(self.frame_input, text = "Input username and password", anchor = "w", justify = "left")
        self.check_label.grid(row = 3, column = 1, padx = 20, pady = 0, sticky = "n")
        
        # Image
        self.login_image = ctk.CTkImage(light_image = Image.open("images/ui/Markiplier.png"), dark_image = Image.open("images/ui/Markiplier.png"), size = (150, 150))
        self.login_image_label = ctk.CTkLabel(self.frame_input, text = "", image = self.login_image)
        self.login_image_label.grid(row = 0, column = 0, rowspan = 5, padx = 20, pady = 20)
    
    def button_pressed(self):
        global name
        global password
        name = self.username_input.get()
        password = self.password_input.get()
        self.login_confirm()    

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Markiflixer Profile selection screen")
        self.geometry("600x400+500+150")
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 0)
        self.resizable(False, False)
        self.background_build()
        self.main_screen_build()
    
    def background_build(self):
        self.background_image = ctk.CTkImage(light_image = Image.open("images/ui/ProfileBackground.png"), dark_image = Image.open("images/ui/ProfileBackground.png"), size = (600, 400))
        self.background_image_label = ctk.CTkLabel(self, text = "", image = self.background_image)
        self.background_image_label.place(x = 0, y = 0)
    
    def main_screen_build(self):
        self.frame_main = ctk.CTkFrame(self)
        self.frame_main.grid(column = 1, row = 0, padx = 30, pady = 25)
        self.frame_search = ctk.CTkFrame(self)
        self.frame_search.grid(column = 0, row = 0, rowspan = 2, padx = (50,20), pady = 10)
        self.main_screen_image = ctk.CTkImage(light_image = Image.open("images/ui/Markiplier.png"), dark_image = Image.open("images/ui/Markiplier.png"), size = (100, 100))
        self.main_screen_image_label = ctk.CTkLabel(self, text = "", image = self.main_screen_image)
        self.main_screen_image_label.grid(row = 1, column = 1, padx = 20, pady = (10,20))
        self.main_screen()
        self.search_screen()    
    
    def main_screen(self):
        self.name = ctk.CTkLabel(self.frame_main, padx = 20, pady = 20, text = f"Welcome back, {name}!\nChoose your profile below.")
        self.name.pack()
        self.profile_checker = ctk.CTkComboBox(self.frame_main, values = list(profiles_and_ages.keys()), command = self.age_configure)
        self.profile_checker.pack()
        self.age = ctk.CTkLabel(self.frame_main, text = f"Age: {profiles_and_ages[self.profile_checker.get()]}")
        self.age.pack()
        self.profile_selector = ctk.CTkButton(self.frame_main, width = 100, height = 34, text = "Select profile", command = self.profile_button_pressed)
        self.profile_selector.pack(pady = 20)
    
    def search_screen(self):
        self.entry_box = ctk.CTkEntry(self.frame_search, width = 220, placeholder_text = "Shrek...")
        self.entry_box.pack(padx = 20, pady = 20)
        self.search_button = ctk.CTkButton(self.frame_search, text="search", command=self.search, width = 220)
        self.search_button.pack()
        self.movies_box = CTkListbox(self.frame_search, height = 220, command=self.show_value)
        self.movies_box.pack(fill="both", expand=True, padx=10, pady=10)
        for item in movies.keys():
            self.movies_box.insert("end", item)
            
    def search(self):
        query = self.entry_box.get().lower()
        self.movies_box.delete(0, "end")
        for item in movies.keys():
            if query in item.lower():
                self.movies_box.insert("end", item)
                
    def age_configure(self, choice):
        print("Selected:", choice)
        self.age.configure(text=f"Age: {profiles_and_ages[choice]}")
        return choice
    
    def show_value(self, selected_option):
        print(movies[selected_option])
    
    def profile_button_pressed(self):
        print("profile button pressed")
    # should probably be used to like log into specific profiles

if __name__ == "__main__":
    markiplier = LoginWindow()
    markiplier.mainloop()
