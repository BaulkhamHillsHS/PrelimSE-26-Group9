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

class VetApp(ctk.CTk):
    """
    Daily patient log.
    Demonstrates OOP design: encapsulation, composition, and message-passing.
    """

    def __init__(self):
        super().__init__()
        self.title("Clinic Name - Daily Patient Log")
        self.geometry("650x610")
        self.resizable(False, False)

        # Private attribute - only accessible through methods (encapsulation)
        self._notes_window = None       # None means "not open yet"
        self._record = PatientRecord()

        self._build_ui()

    # ---- UI Construction ----

    def _build_ui(self):
        """Builds the entire UI. One logical task: constructing the interface."""
        self._build_input_frame()
        self._build_log_frame()
        self._build_file_buttons()
        self.btn_notes = ctk.CTkButton(
            self, text="Open Treatment Notes", command=self._open_notes)
        self.btn_notes.pack(pady=40)

    def _build_input_frame(self):
        """Creates the patient intake form."""
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill=ctk.X, padx=20, pady=(20, 10))

        # Pet name
        ctk.CTkLabel(self.frame_input, text="Pet Name:").grid(
            row=0, column=0, padx=10, pady=10, sticky="e")
        self.ent_pet = ctk.CTkEntry(self.frame_input, width=160,
                                    placeholder_text="e.g. Biscuit")
        self.ent_pet.grid(row=0, column=1, padx=10, pady=10)

        # Species dropdown
        ctk.CTkLabel(self.frame_input, text="Species:").grid(
            row=0, column=2, padx=10, pady=10, sticky="e")
        self.cmb_species = ctk.CTkComboBox(
            self.frame_input,
            values=["Dog", "Cat", "Rabbit", "Bird", "Fish", "Reptile", "Hampterrrrr", "Other"],
            width=110
        )
        self.cmb_species.set("Other")
        self.cmb_species.grid(row=0, column=3, padx=10, pady=10)

        # Owner name
        ctk.CTkLabel(self.frame_input, text="Owner:").grid(
            row=1, column=0, padx=10, pady=10, sticky="e")
        self.ent_owner = ctk.CTkEntry(self.frame_input, width=160,
                                      placeholder_text="e.g. Sarah Chen")
        self.ent_owner.grid(row=1, column=1, padx=10, pady=10)

        # Weight
        ctk.CTkLabel(self.frame_input, text="Weight (kg):").grid(
            row=1, column=2, padx=10, pady=10, sticky="e")
        self.ent_weight = ctk.CTkEntry(self.frame_input, width=110,
                                       placeholder_text="e.g. 4.5")
        self.ent_weight.grid(row=1, column=3, padx=10, pady=10)

        # Add button
        self.btn_add = ctk.CTkButton(self.frame_input, text="Add Patient",
                                     command=self._add_patient, width=120)
        self.btn_add.grid(row=0, column=4, rowspan=2, padx=10, pady=10,
                          sticky="ns")

    def _build_log_frame(self):
        """Creates the patient log display area."""
        self.frame_log = ctk.CTkFrame(self)
        self.frame_log.pack(fill=ctk.BOTH, expand=True, padx=20, pady=(0, 20))

        self.textbox = ctk.CTkTextbox(self.frame_log, width=600, height=230,
                                       font=("Courier New", 12))
        self.textbox.pack(padx=10, pady=10)

        self.lbl_summary = ctk.CTkLabel(self.frame_log,
                                         text="No patients logged yet.",
                                         font=("Arial", 14, "bold"))
        self.lbl_summary.pack(pady=(0, 5))

        self.btn_clear = ctk.CTkButton(self.frame_log, text="Clear Log",
                                        command=self._clear_log,
                                        fg_color="#8B0000",
                                        hover_color="#5a0000")
        self.btn_clear.pack(pady=(0, 10))
        
    def _build_file_buttons(self):
        """Save and Load buttons — call this from _build_ui()."""
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=(0, 4))

        ctk.CTkButton(frame, text="Save to CSV",
                      command=self._save_records,
                      fg_color="#1A7A5E", hover_color="#125C46",
                      width=140).pack(side=ctk.LEFT, padx=(0, 8))

        ctk.CTkButton(frame, text="Load from CSV",
                      command=self._load_records,
                      width=140).pack(side=ctk.LEFT)

        self.lbl_file_status = ctk.CTkLabel(
            frame, text="No file loaded.", text_color="gray")
        self.lbl_file_status.pack(side=ctk.LEFT, padx=16)

    # ---- Handle Records ----
    def _save_records(self):
        """Opens a Save As dialog, then delegates the write to PatientRecord."""
        if self._record.get_patient_count() == 0:
            messagebox.showwarning("Nothing to Save",
                                   "Add at least one patient before saving.")
            return

        filepath = filedialog.asksaveasfilename(
            title="Save Patient Records",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="patients.csv"
        )
        if not filepath:        # user cancelled — do nothing
            return

        try:
            self._record.save_to_csv(filepath)      # delegate to data layer
            self.lbl_file_status.configure(
                text=f"Saved: {os.path.basename(filepath)}",
                text_color="green")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

    def _load_records(self):
        """Opens a file picker, then delegates the read to PatientRecord."""
        filepath = filedialog.askopenfilename(
            title="Open Patient Records",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not filepath:        # user cancelled — do nothing
            return

        try:
            self._record.load_from_csv(filepath)    # delegate to data layer
            self._refresh()
            count = self._record.get_patient_count()
            self.lbl_file_status.configure(
                text=f"Loaded: {os.path.basename(filepath)}  ({count} record(s))",
                text_color="green")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"Could not find:\n{filepath}")
        except (ValueError, KeyError) as e:
            messagebox.showerror("Load Error",
                                 f"File could not be read.\n"
                                 f"Make sure it was saved by this program.\n\n{e}")
        self._update_log()
    
    # ---- Display Handling ----
    
    def _refresh(self):
        count = self._record.get_patient_count()
        avg   = self._record.get_average_weight()
        self.lbl_summary.configure(
            text=f"{count} patient(s)  |  Avg weight: {avg:.1f} kg"
        )

    def _open_notes(self):
        """Opens the treatment notes window only if one is not already open."""
        if self._notes_window is None or not self._notes_window.winfo_exists():
            self._notes_window = TreatmentNotesWindow(self)
        else:
            self._notes_window.focus()  # bring existing window to the front
            
    # ---- Business Logic ----

    def _add_patient(self):
        """Validates the intake form and adds a patient to the log."""
        pet_name  = self.ent_pet.get().strip()
        owner     = self.ent_owner.get().strip()
        species   = self.cmb_species.get()
        weight_str = self.ent_weight.get().strip()

        # Input validation - SE-11-07: implement safe and secure programming solutions
        if not pet_name or not owner or not weight_str:
            self._show_error("All fields are required.")
            return

        try:
            weight = float(weight_str)
        except ValueError:
            self._show_error("Weight must be a number (e.g. 4.5).")
            return

        if weight <= 0 or weight > 200:
            self._show_error("Weight must be between 0 and 200 kg.")
            return

        self._record.add_patient(pet_name, species, owner, weight)

        self._update_log()
        self.ent_pet.delete(0, ctk.END)
        self.ent_owner.delete(0, ctk.END)
        self.ent_weight.delete(0, ctk.END)
        self.cmb_species.set("Other")

    def _update_log(self):
        """Refreshes the log display from the current patient list."""
        self.textbox.delete("1.0", ctk.END)
        header = f"{'#':<4} {'Pet':<18} {'Species':<10} {'Owner':<20} {'Weight':>8}\n"
        self.textbox.insert(ctk.END, header)
        self.textbox.insert(ctk.END, "-" * 62 + "\n")

        for i, p in enumerate(self._record.get_all(), 1):
            line = (f"{i:<4} {p['pet']:<18} {p['species']:<10} "
                    f"{p['owner']:<20} {p['weight']:>6.1f} kg\n")
            self.textbox.insert(ctk.END, line)

        count = self._record.get_patient_count()
        avg_weight = sum(p["weight"] for p in self._record.get_all()) / count
        self.lbl_summary.configure(
            text=f"{count} patient(s) today  |  Avg weight: {avg_weight:.1f} kg"
        )

    def _clear_log(self):
        """Clears the patient list and resets the display."""
        self._record.clear()
        self.textbox.delete("1.0", ctk.END)
        self.lbl_summary.configure(text="No patients logged yet.")

    def _show_error(self, message):
        """Displays an error message temporarily, then resets after 3 seconds."""
        self.lbl_summary.configure(text=f"Error: {message}",
                                    text_color="red")
        self.after(3000, lambda: self.lbl_summary.configure(
            text=f"{len(self._record.get_patient_count())} patient(s) today",
            text_color="white"))            

class TreatmentNotesWindow(ctk.CTkToplevel):
    """A secondary window for entering treatment notes."""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Treatment Notes")
        self.geometry("400x300")
        ctk.CTkLabel(self, text="Enter treatment notes below:").pack(pady=10)
        self.textbox = ctk.CTkTextbox(self, width=360, height=200)
        self.textbox.pack(padx=10, pady=5)

class ClinicScreen(ctk.CTk):
    """
    Base class for all clinic screens.
    Provides the standard header - subclasses add their own content below it.
    Never instantiate this class directly; inherit from it instead.
    """

    CLINIC_NAME = "Vet Clinic"

    def __init__(self, screen_title):
        super().__init__()
        self.geometry("480x380")
        self.title(f"{self.CLINIC_NAME} - {screen_title}")
        self._build_header(screen_title)
        self._build_content()           # calls the subclass version

    def _build_header(self, screen_title):
        """Shared header - runs automatically for every subclass."""
        frame_header = ctk.CTkFrame(self, corner_radius=0, fg_color="#0D3B2E")
        frame_header.pack(fill="x")
        ctk.CTkLabel(frame_header, text=self.CLINIC_NAME,
                     text_color="#A8D8C8").pack(side=ctk.LEFT, padx=14, pady=8)
        ctk.CTkLabel(frame_header, text=screen_title,
                     font=ctk.CTkFont(size=14, weight="bold"),
                     text_color="white").pack(side=ctk.RIGHT, padx=14, pady=8)

    def _build_content(self):
        """Override in subclasses to add screen-specific widgets."""
        pass

class PatientIntakeScreen(ClinicScreen):
    """Intake form - inherits the header, adds its own form."""

    def __init__(self):
        super().__init__("Patient Intake")  # passes the title up to ClinicScreen

    def _build_content(self):
        # Intake-specific widgets go here
        ctk.CTkButton(self, text="Check In Patient").pack(pady=40)

class TreatmentScreen(ClinicScreen):
    """Treatment notes - same header, completely different content."""

    def __init__(self):
        super().__init__("Treatment Notes")

    def _build_content(self):
        self.textbox = ctk.CTkTextbox(self, width=430, height=220)
        self.textbox.pack(padx=20, pady=20)

class PatientRecord:
    FIELDS = ["pet", "species", "owner", "weight"]  # column names used in CSV

    """
    Stores and manages vet clinic patient data.
    No GUI dependencies - this class can be tested without a window.
    """

    def __init__(self):
        self._patients = []             # private - encapsulation

    def add_patient(self, pet_name, species, owner, weight):
        self._patients.append({
            "pet": pet_name,
            "species": species,
            "owner": owner,
            "weight": weight,
        })

    def get_patient_count(self):
        return len(self._patients)

    def get_average_weight(self):
        if not self._patients:
            return 0.0
        return sum(p["weight"] for p in self._patients) / len(self._patients)

    def get_all(self):
        return list(self._patients)     # returns a copy, not original list

    def clear(self):
        self._patients.clear()
    
    def save_to_csv(self, filepath):
        """
        Writes all current patient records to a CSV file.

        The file will look like this:
            pet,species,owner,weight
            Biscuit,Dog,Sarah Chen,12.4
            Mochi,Cat,James Park,4.1
        """
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDS)
            writer.writeheader()        # writes the column name row
            writer.writerows(self._patients)
    
    def load_from_csv(self, filepath):
        """
        Reads patient records from a CSV file, replacing current records.

        weight is stored as a string in the file — float() converts it back.
        """
        self._patients.clear()
        with open(filepath, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._patients.append({
                    "pet":     row["pet"],
                    "species": row["species"],
                    "owner":   row["owner"],
                    "weight":  float(row["weight"]),   # string → float
                })


if __name__ == "__main__":
    app = VetApp()
    app.mainloop()