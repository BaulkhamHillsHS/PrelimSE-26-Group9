# Imports
import customtkinter as ctk
from CTkListbox import *
import csv
from PIL import Image
import ast

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
anime = {
    "Naruto": "child",
    "Pokémon": "child",
    "Doraemon": "child",
    "Yo-kai Watch": "child",
    "Beyblade": "child",
    "Digimon Adventure": "child",
    "Cardcaptor Sakura": "child",
    "Hamtaro": "child",
    "Chi's Sweet Home": "child",
    "Anpanman": "child",
    "Pretty Cure": "child",
    "Inazuma Eleven": "child",

    "Attack on Titan": "adult",
    "Death Note": "adult",
    "Tokyo Ghoul": "adult",
    "Monster": "adult",
    "Psycho-Pass": "adult",
    "Parasyte": "adult",
    "Black Lagoon": "adult",
    "Hellsing Ultimate": "adult",
    "Berserk": "adult",
    "Vinland Saga": "adult",
    "Chainsaw Man": "adult",
    "Devilman Crybaby": "adult",
    "Perfect Blue": "adult"
}
movies = movies | anime
# Themes
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Default state
logged_in = False

# Global variable setup
profiles_and_ages = {}
watching = ""
age = ""
profile = ""
email = ""

# Login window
class LoginWindow(ctk.CTk):
    def __init__(self): ##initialises the window
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

    def login_confirm(self): ##matches the data entered with csv to check if user exists
        with open("data.csv", "r") as csv_file:
                data = csv.reader(csv_file)
                next(data)
                for row in data:
                    if row[1] == email and row[2] == password:
                        global profiles_and_ages
                        global name
                        self.logged_in = True 
                        profiles_and_ages[row[4]] = row[5]
                        name = row[0] ##Saving these variable for later (they are needed)

                if self.logged_in != True:
                    # Changes text when incorrect email or password is entered.
                    self.check_label.configure(text_color = "red", text = "Incorrect email or password")
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
Please input your email
and password to log in.""").grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "n")
        self.username_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Email")
        self.username_input.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = "n")
        self.password_input = ctk.CTkEntry(self.frame_input, width = 160, placeholder_text="Password", show = "*") ##asterisks out the password
        self.password_input.grid(row = 2, column = 1, padx = 20, pady = 5, sticky = "n")
        self.button = ctk.CTkButton(self.frame_input, width = 160, height = 28, border_width = 2, fg_color = "#fb86a9", hover_color = "#a7516b", border_color = "#ce0606", text = "Log in", command=self.button_pressed)
        self.button.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = "n")
        self.check_label = ctk.CTkLabel(self.frame_input, text = "Input email and password", anchor = "w", justify = "left")
        self.check_label.grid(row = 3, column = 1, padx = 20, pady = 0, sticky = "n")
        
        # Image
        self.login_image = ctk.CTkImage(light_image = Image.open("images/ui/Markiplier.png"), dark_image = Image.open("images/ui/Markiplier.png"), size = (150, 150))
        self.login_image_label = ctk.CTkLabel(self.frame_input, text = "", image = self.login_image)
        self.login_image_label.grid(row = 0, column = 0, rowspan = 5, padx = 20, pady = 20)
    
    def button_pressed(self):
        global email
        global password
        email = self.username_input.get()
        password = self.password_input.get()
        self.login_confirm()    ##Links the button to the command given

##Main movie/show viewing window
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
    
    def main_screen_build(self): ##Separating background and main screan for cleanliness
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
        self.profile_checker.set(list(profiles_and_ages.keys())[0])
        global profile, age
        profile = self.profile_checker.get()
        age = profiles_and_ages[profile]
        self.age = ctk.CTkLabel(self.frame_main, text=f"Age: {age}")
        self.age.pack()
        self.profile_selector = ctk.CTkButton(self.frame_main, width = 100, height = 34, border_width = 2, fg_color = "#fb86a9", hover_color = "#a7516b", border_color = "#ce0606", text = "Exit", command = self.exit_button_pressed)
        self.profile_selector.pack(pady = 20)
    
    def search_screen(self): ##Uses the community addon for ctk Listbox, emulating the tkinter listbox
        self.entry_box = ctk.CTkEntry(self.frame_search, width = 220, placeholder_text = "Shrek...")
        self.entry_box.pack(padx = 20, pady = 20)
        self.search_button = ctk.CTkButton(self.frame_search, border_width = 2, fg_color = "#fb86a9", hover_color = "#a7516b", border_color = "#ce0606", text="search", command=self.search, width = 220)
        self.search_button.pack()
        self.movies_box = CTkListbox(self.frame_search, height = 220, command=self.show_value)
        self.movies_box.pack(fill="both", expand=True, padx=10, pady=10)
        for item in movies.keys():
            self.movies_box.insert("end", item)
            
    def search(self): ##Refreshing the search box
        query = self.entry_box.get().lower()
        self.movies_box.delete(0, "end")
        for item in movies.keys():
            if query in item.lower():
                self.movies_box.insert("end", item)
                
    def age_configure(self, choice):
        global age
        global profile
        age = profiles_and_ages[choice]
        profile = choice
        self.age.configure(text=f"Age: {profiles_and_ages[choice]}")
        return choice
    
    def show_value(self, selected_option):
        global watching
        watching = selected_option
        self.destroy()
        media = MediaWindow()
        media.mainloop()
    
    def exit_button_pressed(self):
        self.destroy()
    # Exits application

class MediaWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Media Player")
        self.geometry("600x400+500+150")
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 0)
        self.resizable(False, False)
        self.background_build()
    
    def background_build(self):
        self.background_image = ctk.CTkImage(light_image = Image.open("images/ui/ProfileBackground.png"), dark_image = Image.open("images/ui/ProfileBackground.png"), size = (600, 400))
        self.background_image_label = ctk.CTkLabel(self, text = "", image = self.background_image)
        self.background_image_label.place(x = 0, y = 0)
        self.watching = ctk.CTkLabel(self, text = watching)
        self.watching.pack()
        try: ##Just in case there is no image
            self.media_image = ctk.CTkImage(light_image = Image.open(f"images/posters/{watching}.webp"), dark_image = Image.open(f"images/posters/{watching}.webp"), size = (500, 300))
            self.media_image_label = ctk.CTkLabel(self, text = "", image = self.media_image)
            self.media_image_label.pack()
        except FileNotFoundError: ##make sure a missing or broken image doesnt break program
            pass
        self.watch_button = ctk.CTkButton(self, width = 240, border_width = 2, fg_color = "#fb86a9", hover_color = "#a7516b", border_color = "#ce0606", text = "Watch" if watching not in anime else "Watch Next Episode", command = self.watch_check)
        self.watch_button.pack()
        self.return_button = ctk.CTkButton(self, width = 100, border_width = 2, fg_color = "#fb86a9", hover_color = "#a7516b", border_color = "#ce0606", text = "Return to main menu", command = self.go_back)
        self.return_button.pack()

    def watch_check(self):
        if age.lower() == "child" and movies[watching] == "adult": ##content filtering
            self.watch_button.configure(text = "ERROR age does not meet requirement", state = "disabled")
        else: ##opens corresponding text file thank goodness for fstrings
            with open(f"profiles/{profile}.txt", "r", encoding="utf-8") as file:
                content = file.read()
            watchhistory = ast.literal_eval(content or "[]")
            if watching not in anime:
                if watching not in watchhistory:
                    watchhistory.append(watching)
                with open(f"profiles/{profile}.txt", "w", encoding="utf-8") as file:
                    file.write(str(watchhistory))
            else: ##Appends episodes as tvshow1, tvshow2 etc
                episode = 1
                while f"{watching}{str(episode)}" in watchhistory:
                    episode += 1
                if f"{watching}{str(episode)}" not in watchhistory:
                    watchhistory.append(f"{watching}{str(episode)}")
                    with open(f"profiles/{profile}.txt", "w", encoding="utf-8") as file:
                        file.write(str(watchhistory))
                
        
    def go_back(self):
        self.destroy()        
        main = MainWindow()
        main.mainloop()

if __name__ == "__main__":
    markiplier = LoginWindow()
    markiplier.mainloop()
