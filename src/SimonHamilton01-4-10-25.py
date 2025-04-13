import tkinter as tk # Imports the "tkinter" package which is a graphical programming toolkit for Python.
from tkinter import colorchooser # Imports the "colorchooser" module from tkinter which allows users to select colors.
import json # Imports the "json" module which allows for parsing and manipulating JSON data.
import os # Imports the "os" module which provides a way of using operating system dependent functionality like reading or writing to the file system.
from dataclasses import dataclass, asdict # Imports the "dataclass" decorator and the "asdict" function from the "dataclasses" module. The "dataclass" decorator is used to create classes that are primarily used to store data, and "asdict" converts a dataclass instance into a dictionary.
PATIENTS_FILE = "patients.json" # This creates a variable called "PATIENTS_FILE" and assigns it the string "patients.json". This is the name of a file that will be used to store patient data in JSON format.  
@dataclass # This is a decorator that automatically generates special methods for the class, such as __init__() and __repr__().
class Patients: # This creates a class called "Patients".
    first_name: str = "" # This creates a variable called "first_name" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    last_name: str = "" # This creates a variable called "last_name" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    dob: str = "" # This creates a variable called "dob" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    med_history: str = "" # This creates a variable called "med_history" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    allergies: str = "" # This creates a variable called "allergies" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    medications: str = "" # This creates a variable called "medications" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    emergency_contact_info: str = "" # This creates a variable called "emergency_contact_info" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    insurance_info: str = "" # This creates a variable called "insurance_info" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    primary_physician: str = "" # This creates a variable called "primary_physician" and assigns it an empty string. The type of this variable is specified as "str", meaning the input data is converted to string format.
    def get_patient_info(self): # A method is defined here by the name of "get_patient_info". This method is used to retrieve the patient information. "self" is the instance of the class.
        return asdict(self) # This returns the patient information as a dictionary using the "asdict" function. This function converts the dataclass instance into a dictionary, where the keys are the field names and the values are the corresponding values of the instance.
class BasePage(tk.Frame): # This creates a class called "BasePage" which inherits from "tk.Frame". This means that "BasePage" is a type of frame in tkinter.
    def __init__(self, parent, title="Base Page"): # This is the initial constructor method for the "BasePage" class. It initializes the frame with a parent widget and an optional title.
        super().__init__(parent) # This calls the constructor of the parent class "tk.Frame".
        self.title = title # This assigns the title to the instance variable "self.title".
        self.create_header() # This calls the "create_header" method to create the header of the page.
    def create_header(self): # A method is defined here by the name of "create_header". This method is used to create the header of the page.
        header = tk.Label(self, text=self.title, font=("Arial", 24)) # This creates a label widget with the title text and a font size of 24.
        header.pack(pady=20) # This packs the header widget into the frame with a vertical padding of 20 pixels.
        self.content = tk.Frame(self) # This creates a new frame widget called "content" which will hold the main content of the page.
        self.content.pack(fill="both", expand=True) # This packs the content frame into the base page, allowing it to fill both the horizontal and vertical space and expand as needed.
class HomePage(BasePage): # This creates a class called "HomePage" which inherits from "BasePage". This means that "HomePage" is a type of base page. This also exhibits heirarchical inheritance.
    def __init__(self, parent): # This is the initial constructor method for the "HomePage" class. It initializes the page with a parent widget.
        super().__init__(parent, title="Patient Data Entry") # This calls the constructor of the parent class "BasePage" with the title "Patient Data Entry".
        self.build_form() # This calls the "build_form" method to create the form for patient data entry.
    def build_form(self): # A method is defined here by the name of "build_form". This method is used to create the form for patient data entry.
        form_frame = tk.Frame(self.content) # This creates a new frame widget called "form_frame" which will hold the form fields.
        form_frame.pack(expand=True) # This packs the form frame into the content frame, allowing it to expand as needed.
        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the first name field and places it in the grid layout.
        self.first_name_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the first name field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Last Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the last name field and places it in the grid layout.
        self.last_name_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the last name field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Date of Birth:").grid(row=2, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the date of birth field and places it in the grid layout.
        self.dob_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the date of birth field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.dob_entry.grid(row=2, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Medical History:").grid(row=3, column=0, sticky="ne", padx=5, pady=5) # This creates a label widget for the medical history field and places it in the grid layout.
        self.med_history_entry = tk.Text(form_frame, width=30, height=4, bd=2, relief="solid") # This creates a text widget for the medical history field with a width of 30 characters, a height of 4 lines, a border width of 2, and a solid relief style.
        self.med_history_entry.grid(row=3, column=1, padx=5, pady=5) # This places the text widget in the grid layout.
        tk.Label(form_frame, text="Allergies:").grid(row=4, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the allergies field and places it in the grid layout.
        self.allergies_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the allergies field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.allergies_entry.grid(row=4, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Medications:").grid(row=5, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the medications field and places it in the grid layout.
        self.medications_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the medications field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.medications_entry.grid(row=5, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Emergency Contact Info:").grid(row=6, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the emergency contact info field and places it in the grid layout.
        self.emergency_contact_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the emergency contact info field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.emergency_contact_entry.grid(row=6, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Insurance Info:").grid(row=7, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the insurance info field and places it in the grid layout.
        self.insurance_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the insurance info field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.insurance_entry.grid(row=7, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        tk.Label(form_frame, text="Primary Physician:").grid(row=8, column=0, sticky="e", padx=5, pady=5) # This creates a label widget for the primary physician field and places it in the grid layout.
        self.physician_entry = tk.Entry(form_frame, width=40, bd=2, relief="solid") # This creates an entry widget for the primary physician field with a width of 40 characters, a border width of 2, and a solid relief style.
        self.physician_entry.grid(row=8, column=1, padx=5, pady=5) # This places the entry widget in the grid layout.
        submit_btn = tk.Button(form_frame, text="Submit", command=self.submit_patient, bd=2, relief="solid") # This creates a button widget for submitting the form with the text "Submit", a border width of 2, and a solid relief style.
        submit_btn.grid(row=9, column=0, columnspan=2, pady=20) # This places the button widget in the grid layout, spanning two columns and with a vertical padding of 20 pixels.
    def submit_patient(self): # A method is defined here by the name of "submit_patient". This method is used to submit the patient data.
        patient = Patients( # This creates an instance of the "Patients" class with the data entered in the form fields.
            first_name=self.first_name_entry.get(), # This retrieves the value from the first name entry field.
            last_name=self.last_name_entry.get(), # This retrieves the value from the last name entry field.
            dob=self.dob_entry.get(), # This retrieves the value from the date of birth entry field.
            med_history=self.med_history_entry.get("1.0", tk.END).strip(), # This retrieves the value from the medical history text field, starting from line 1 to the end of the text.
            allergies=self.allergies_entry.get(), # This retrieves the value from the allergies entry field.
            medications=self.medications_entry.get(), # This retrieves the value from the medications entry field.
            emergency_contact_info=self.emergency_contact_entry.get(), # This retrieves the value from the emergency contact info entry field.
            insurance_info=self.insurance_entry.get(), # This retrieves the value from the insurance info entry field.
            primary_physician=self.physician_entry.get() # This retrieves the value from the primary physician entry field.
        ) # This ends the creation of the "Patients" instance.
        patient_dict = patient.get_patient_info() # This retrieves the patient information as a dictionary using the "get_patient_info" method.
        data = [] # This initializes an empty list called "data" to store the patient data.
        if os.path.exists(PATIENTS_FILE): # This checks if the "patients.json" file exists.
            with open(PATIENTS_FILE, "r") as f: # This opens the "patients.json" file in read mode.
                try: # This tries to load the JSON data from the file.
                    data = json.load(f) # This loads the JSON data from the file into the "data" variable.
                except json.JSONDecodeError: # This handles the case where the JSON data is not valid.
                    data = [] # This initializes the "data" variable as an empty list.
        data.append(patient_dict) # This appends the patient data dictionary to the "data" list.
        with open(PATIENTS_FILE, "w") as f: # This opens the "patients.json" file in write mode.
            json.dump(data, f, indent=4) # This writes the "data" list to the file in JSON format with an indentation of 4 spaces.
        self.clear_form() # This calls the "clear_form" method to clear the form fields after submission.
    def clear_form(self): # A method is defined here by the name of "clear_form". This method is used to clear the form fields after submission.
        self.first_name_entry.delete(0, tk.END) # This clears the content of the first name entry field.
        self.last_name_entry.delete(0, tk.END) # This clears the content of the last name entry field.
        self.dob_entry.delete(0, tk.END) # This clears the content of the date of birth entry field.
        self.med_history_entry.delete("1.0", tk.END) # This clears the content of the medical history text field.
        self.allergies_entry.delete(0, tk.END) # This clears the content of the allergies entry field.
        self.medications_entry.delete(0, tk.END) # This clears the content of the medications entry field.
        self.emergency_contact_entry.delete(0, tk.END) # This clears the content of the emergency contact info entry field.
        self.insurance_entry.delete(0, tk.END) # This clears the content of the insurance info entry field.
        self.physician_entry.delete(0, tk.END) # This clears the content of the primary physician entry field.
class PatientDataPage(BasePage): # This creates a class called "PatientDataPage" which inherits from "BasePage". This means that "PatientDataPage" is a type of base page demonstrating heirarchical inheritance.
    def __init__(self, parent, show_page_callback): # This is the initial constructor method for the "PatientDataPage" class. It initializes the page with a parent widget and a callback function to show another page.
        super().__init__(parent, title="Patient Data") # This calls the constructor of the parent class "BasePage" with the title "Patient Data".
        self.show_page_callback = show_page_callback # This assigns the callback function to the instance variable "self.show_page_callback".
        self.build_search() # This calls the "build_search" method to create the search functionality for patient data.
    def build_search(self): # A method is defined here by the name of "build_search". This method is used to create the search functionality for patient data.
        search_frame = tk.Frame(self.content) # This creates a new frame widget called "search_frame" which will hold the search fields.
        search_frame.pack(pady=10) # This packs the search frame into the content frame with a vertical padding of 10 pixels.
        tk.Label(search_frame, text="Search by First or Last Name:").pack(side="left", padx=5) # This creates a label widget for the search field and places it in the grid layout.
        self.search_entry = tk.Entry(search_frame, width=30) # This creates an entry widget for the search field with a width of 30 characters.
        self.search_entry.pack(side="left", padx=5) # This places the entry widget in the grid layout.
        self.search_entry.bind("<Return>", lambda event: self.perform_search()) # This binds the "Return" key event to the "perform_search" method, allowing the user to press "Enter" to perform the search.
        search_btn = tk.Button(search_frame, text="Search", command=self.perform_search) # This creates a button widget for performing the search with the text "Search".
        search_btn.pack(side="left", padx=5) # This places the button widget in the grid layout.
        list_frame = tk.Frame(self.content) # This creates a new frame widget called "list_frame" which will hold the search results.
        list_frame.pack(fill="both", expand=True, pady=10) # This packs the list frame into the content frame, allowing it to fill both the horizontal and vertical space and expand as needed.
        self.results_listbox = tk.Listbox(list_frame, width=80, height=20) # This creates a listbox widget for displaying the search results with a width of 80 characters and a height of 20 lines.
        self.results_listbox.pack(side="left", fill="both", expand=True) # This packs the listbox widget into the list frame, allowing it to fill both the horizontal and vertical space and expand as needed.
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.results_listbox.yview) # This creates a scrollbar widget for the listbox with a vertical orientation.
        scrollbar.pack(side="right", fill="y") # This packs the scrollbar widget into the list frame, allowing it to fill the vertical space.
        self.results_listbox.config(yscrollcommand=scrollbar.set) # This configures the listbox to use the scrollbar for vertical scrolling.
        self.results_listbox.bind("<Double-Button-1>", self.open_patient_detail) # This binds the double-click event on the listbox to the "open_patient_detail" method, allowing the user to open patient details by double-clicking on a result.
        self.search_results = [] # This initializes an empty list called "search_results" to store the search results.
    def perform_search(self): # A method is defined here by the name of "perform_search". This method is used to perform the search for patient data.
        self.results_listbox.delete(0, tk.END) # This clears the content of the listbox before displaying new search results.
        query = self.search_entry.get().strip().lower() # This retrieves the value from the search entry field, strips any leading or trailing whitespace, and converts it to lowercase for case-insensitive searching.
        data = [] # This initializes an empty list called "data" to store the patient data.
        if os.path.exists(PATIENTS_FILE): # This checks if the "patients.json" file exists.
            with open(PATIENTS_FILE, "r") as f: # This opens the "patients.json" file in read mode.
                try: # This tries to load the JSON data from the file.
                    data = json.load(f) # This loads the JSON data from the file into the "data" variable.
                except json.JSONDecodeError: # This handles the case where the JSON data is not valid.
                    data = [] # This initializes the "data" variable as an empty list.
        if not query: # This checks if the search query is empty.
            sorted_data = sorted(data, key=lambda p: (p.get("last_name", "").lower(), p.get("first_name", "").lower())) # This sorts the patient data by last name and first name in ascending order.
        else: # This checks if the search query is not empty.
            sorted_data = [ # This creates a new list called "sorted_data" which contains the filtered patient data based on the search query.
                patient for patient in data # This iterates over each patient in the "data" list.
                if query in patient.get("first_name", "").lower() or query in patient.get("last_name", "").lower() # This checks if the search query is present in either the first name or last name of the patient.
            ] # This ends the creation of the "sorted_data" list.
            sorted_data = sorted(sorted_data, key=lambda p: (p.get("last_name", "").lower(), p.get("first_name", "").lower())) # This sorts the filtered patient data by last name and first name in ascending order.
        self.search_results = sorted_data # This assigns the sorted patient data to the instance variable "self.search_results".
        if sorted_data: # This checks if there are any matching patients in the sorted data.
            for patient in sorted_data: # This iterates over each patient in the sorted data.
                display_str = f"{patient.get('first_name', '')} {patient.get('last_name', '')} - DOB: {patient.get('dob', '')}" # This creates a display string for each patient with their first name, last name, and date of birth.
                self.results_listbox.insert(tk.END, display_str) # This inserts the display string into the listbox at the end of the list.
        else: # This checks if there are no matching patients in the sorted data.
            self.results_listbox.insert(tk.END, "No matching patients found.") # This inserts a message into the listbox indicating that no matching patients were found.
    def open_patient_detail(self, event): # A method is defined here by the name of "open_patient_detail". This method is used to open the details of a selected patient.
        selection = self.results_listbox.curselection() # This retrieves the current selection from the listbox.
        if not selection: # This checks if there is no selection in the listbox.
            return # This returns from the method if there is no selection.
        index = selection[0] # This retrieves the index of the selected item in the listbox.
        patient_data = self.search_results[index] # This retrieves the patient data from the "search_results" list based on the selected index.
        detail_page = PatientDetailPage(self.master, patient_data, go_back=lambda: self.show_page_callback("PatientDataPage")) # This creates an instance of the "PatientDetailPage" class with the patient data and a callback function to go back to the patient data page.
        detail_page.place(relx=0, rely=0, relwidth=1, relheight=1) # This places the detail page in the same position as the patient data page.
        detail_page.tkraise() # This raises the detail page to the top of the stacking order, making it visible.
class PatientDetailPage(BasePage): # This creates a class called "PatientDetailPage" which inherits from "BasePage". This means that "PatientDetailPage" is a type of base page demonstrating heirarchical inheritance.
    def __init__(self, parent, patient_data, go_back): # This is the initial constructor method for the "PatientDetailPage" class. It initializes the page with a parent widget, patient data, and a callback function to go back.
        super().__init__(parent, title="Patient Details") # This calls the constructor of the parent class "BasePage" with the title "Patient Details".
        self.bind("<Escape>", lambda event: self.go_back(go_back)) # This binds the "Escape" key event to the "go_back" method, allowing the user to go back to the previous page by pressing "Escape".
        self.build_details(patient_data, go_back) # This calls the "build_details" method to create the details view for the selected patient.
        self.focus_set() # This sets the focus to the current widget, allowing it to receive keyboard events.
    def build_details(self, patient_data, go_back): # A method is defined here by the name of "build_details". This method is used to create the details view for the selected patient.
        details_frame = tk.Frame(self.content) # This creates a new frame widget called "details_frame" which will hold the patient details.
        details_frame.pack(fill="both", expand=True, padx=10, pady=10) # This packs the details frame into the content frame, allowing it to fill both the horizontal and vertical space and expand as needed.
        for idx, (key, value) in enumerate(patient_data.items()): # This iterates over each key-value pair in the patient data dictionary.
            field_name = key.replace("_", " ").title() + ":" # This formats the field name by replacing underscores with spaces and capitalizing the first letter of each word.
            tk.Label(details_frame, text=field_name, anchor="w", width=20).grid(row=idx, column=0, sticky="w", padx=5, pady=2) # This creates a label widget for the field name and places it in the grid layout.
            tk.Label(details_frame, text=value, anchor="w").grid(row=idx, column=1, sticky="w", padx=5, pady=2) # This creates a label widget for the field value and places it in the grid layout.
        back_btn = tk.Button(self.content, text="Back", command=lambda: self.go_back(go_back)) # This creates a button widget for going back with the text "Back".
        back_btn.pack(side="right", anchor="ne", padx=10, pady=10) # This places the button widget in the content frame, aligning it to the right and with a padding of 10 pixels.
    def go_back(self, go_back_cb): # A method is defined here by the name of "go_back". This method is used to go back to the previous page.
        go_back_cb() # This calls the callback function to go back to the previous page.
        self.destroy() # This destroys the current widget, removing it from the display.
def recursive_set_bg(widget, color): # A function is defined here by the name of "recursive_set_bg". This function is used to recursively set the background color of a widget and its children.
    try: # This tries to set the background color of the widget.
        widget.configure(bg=color) # This configures the widget to use the specified background color.
    except Exception: # This handles any exceptions that may occur while setting the background color.
        pass # This passes the exception without doing anything.
    for child in widget.winfo_children(): # This iterates over each child widget of the current widget.
        recursive_set_bg(child, color) # This recursively calls the "recursive_set_bg" function for each child widget, setting its background color.
class SettingsPage(BasePage): # This creates a class called "SettingsPage" which inherits from "BasePage". This means that "SettingsPage" is a type of base page demonstrating heirarchical inheritance.
    def __init__(self, parent): # This is the initial constructor method for the "SettingsPage" class. It initializes the page with a parent widget.
        super().__init__(parent, title="Settings Page") # This calls the constructor of the parent class "BasePage" with the title "Settings Page".
        self.create_widgets() # This calls the "create_widgets" method to create the settings widgets.
    def create_widgets(self): # A method is defined here by the name of "create_widgets". This method is used to create the settings widgets.
        description = tk.Label(self.content, text="Configure your settings here.") # This creates a label widget with a description text.
        description.pack(pady=10) # This packs the description label into the content frame with a vertical padding of 10 pixels.
        change_bg_btn = tk.Button(self.content, text="Change Background Color", command=self.change_bg) # This creates a button widget for changing the background color with the text "Change Background Color".
        change_bg_btn.pack(pady=10) # This packs the button widget into the content frame with a vertical padding of 10 pixels.
    def change_bg(self): # A method is defined here by the name of "change_bg". This method is used to change the background color of the application.
        color = colorchooser.askcolor(title="Choose Background Color")[1] # This opens a color chooser dialog and retrieves the selected color.
        if color: # This checks if a color was selected.
            top = self.winfo_toplevel() # This retrieves the top-level widget (the main window) of the current widget.
            recursive_set_bg(top, color) # This calls the "recursive_set_bg" function to set the background color of the top-level widget and its children.
def create_window(): # A function is defined here by the name of "create_window". This function is used to create the main application window.
    window = tk.Tk() # This creates a new instance of the Tk class, which represents the main application window.
    window.title("Simon Hamilton") # This sets the title of the main window to "Simon Hamilton".
    window.geometry("900x800") # This sets the size of the main window to 900 pixels wide and 800 pixels tall.
    window.resizable(False, False) # This makes the main window non-resizable in both horizontal and vertical directions.
    menu_width = 200 # This creates a variable called "menu_width" and assigns it the value 200. This is the width of the side menu.
    step = 20 # This creates a variable called "step" and assigns it the value 20. This is the step size for the menu animation.
    delay = 10 # This creates a variable called "delay" and assigns it the value 10. This is the delay time in milliseconds for the menu animation.
    menu_frame = tk.Frame(window, width=menu_width, height=800, bg="lightgray") # This creates a new frame widget called "menu_frame" which will hold the side menu. The width is set to "menu_width", the height is set to 800 pixels, and the background color is set to light gray.
    menu_frame.place(x=-menu_width, y=0) # This places the menu frame at the left side of the window, outside of the visible area.
    menu_visible = [False] # This creates a list called "menu_visible" with a single element set to False. This is used to track whether the menu is currently visible or not.
    current_x = [-menu_width] # This creates a list called "current_x" with a single element set to -menu_width. This is used to track the current x-coordinate of the menu frame.
    def animate_menu_in(): # A function is defined here by the name of "animate_menu_in". This function is used to animate the menu sliding in from the left.
        x = current_x[0] # This retrieves the current x-coordinate of the menu frame.
        if x < 0: # This checks if the menu frame is not fully visible.
            x += step # This increments the x-coordinate by the step size.
            if x > 0: # This checks if the x-coordinate exceeds 0.
                x = 0 # This sets the x-coordinate to 0 to ensure the menu frame is fully visible.
            current_x[0] = x # This updates the current x-coordinate of the menu frame.
            menu_frame.place(x=x, y=0) # This places the menu frame at the updated x-coordinate.
            window.after(delay, animate_menu_in) # This schedules the next animation step after the specified delay.
        else: # This checks if the menu frame is fully visible.
            menu_visible[0] = True # This sets the menu_visible flag to True, indicating that the menu is now visible.
            menu_frame.lift() # This brings the menu frame to the top of the stacking order, making it visible above other widgets.
    def animate_menu_out(): # A function is defined here by the name of "animate_menu_out". This function is used to animate the menu sliding out to the left.
        x = current_x[0] # This retrieves the current x-coordinate of the menu frame.
        if x > -menu_width: # This checks if the menu frame is not fully hidden.
            x -= step # This decrements the x-coordinate by the step size.
            if x < -menu_width: # This checks if the x-coordinate exceeds -menu_width.
                x = -menu_width # This sets the x-coordinate to -menu_width to ensure the menu frame is fully hidden.
            current_x[0] = x # This updates the current x-coordinate of the menu frame.
            menu_frame.place(x=x, y=0) # This places the menu frame at the updated x-coordinate.
            window.after(delay, animate_menu_out) # This schedules the next animation step after the specified delay.
        else: # This checks if the menu frame is fully hidden.
            menu_visible[0] = False # This sets the menu_visible flag to False, indicating that the menu is now hidden.
            hamburger_btn.lift() # This brings the hamburger button to the top of the stacking order, making it visible above other widgets.
    def toggle_menu(): # A function is defined here by the name of "toggle_menu". This function is used to toggle the visibility of the menu.
        if not menu_visible[0]: # This checks if the menu is currently hidden.
            animate_menu_in() # This calls the "animate_menu_in" function to slide the menu in from the left.
        else: # This checks if the menu is currently visible.
            animate_menu_out() # This calls the "animate_menu_out" function to slide the menu out to the left.
    def is_descendant(child, parent): # A function is defined here by the name of "is_descendant". This function is used to check if a widget is a descendant of another widget.
        while child: # This loops while the child widget is not None.
            if child == parent: # This checks if the child widget is the same as the parent widget.
                return True # This returns True if the child widget is a descendant of the parent widget.
            child = child.master # This sets the child widget to its parent widget, moving up the widget hierarchy.
        return False # This returns False if the child widget is not a descendant of the parent widget.
    def close_menu_if_click_outside(event): # A function is defined here by the name of "close_menu_if_click_outside". This function is used to close the menu if a click occurs outside of it.
        if menu_visible[0]: # This checks if the menu is currently visible.
            if is_descendant(event.widget, menu_frame) or is_descendant(event.widget, hamburger_btn): # This checks if the clicked widget is a descendant of the menu frame or the hamburger button.
                return # This returns from the function if the clicked widget is a descendant of the menu frame or the hamburger button.
            toggle_menu() # This calls the "toggle_menu" function to slide the menu out to the left if the clicked widget is not a descendant of the menu frame or the hamburger button.
    container = tk.Frame(window) # This creates a new frame widget called "container" which will hold the main content of the application.
    container.place(x=0, y=50, relwidth=1, relheight=0.95) # This places the container frame at the top of the window, below the menu frame, and allows it to fill the remaining space.
    pages = {} # This initializes an empty dictionary called "pages" to store the different pages of the application.
    for PageClass in (HomePage, SettingsPage): # This iterates over each page class in the tuple (HomePage, SettingsPage).
        page_name = PageClass.__name__ # This retrieves the name of the page class.
        frame = PageClass(container) # This creates an instance of the page class with the container frame as the parent.
        pages[page_name] = frame # This adds the page instance to the "pages" dictionary with the page name as the key.
        frame.place(relx=0, rely=0, relwidth=1, relheight=1) # This places the page frame in the same position as the container frame, allowing it to fill the entire space.
    pd_page = PatientDataPage(container, show_page_callback=lambda name: show_page(name)) # This creates an instance of the "PatientDataPage" class with the container frame as the parent and a callback function to show another page.
    pages["PatientDataPage"] = pd_page # This adds the patient data page instance to the "pages" dictionary with the page name as the key.
    pd_page.place(relx=0, rely=0, relwidth=1, relheight=1) # This places the patient data page frame in the same position as the container frame, allowing it to fill the entire space.
    def show_page(page_name): # A function is defined here by the name of "show_page". This function is used to show a specific page in the application.
        pages[page_name].tkraise() # This raises the specified page to the top of the stacking order, making it visible.
    def go_home(): # A function is defined here by the name of "go_home". This function is used to navigate to the home page.
        show_page("HomePage") # This calls the "show_page" function to show the home page.
        if menu_visible[0]: # This checks if the menu is currently visible.
            toggle_menu() # This calls the "toggle_menu" function to slide the menu out to the left.
    def open_patient_data(): # A function is defined here by the name of "open_patient_data". This function is used to navigate to the patient data page.
        show_page("PatientDataPage") # This calls the "show_page" function to show the patient data page.
        if menu_visible[0]: # This checks if the menu is currently visible.
            toggle_menu() # This calls the "toggle_menu" function to slide the menu out to the left.
    def open_settings(): # A function is defined here by the name of "open_settings". This function is used to navigate to the settings page.
        show_page("SettingsPage") # This calls the "show_page" function to show the settings page.
        if menu_visible[0]: # This checks if the menu is currently visible.
            toggle_menu() # This calls the "toggle_menu" function to slide the menu out to the left.
    def logout(): # A function is defined here by the name of "logout". This function is used to log out of the application.
        window.quit() # This calls the "quit" method of the main window to close the application.
    btn_home = tk.Button(menu_frame, text="Home", command=go_home, bg="white", bd=2, relief="solid") # This creates a button widget for navigating to the home page with the text "Home", a background color of white, a border width of 2, and a solid relief style.
    btn_home.pack(pady=10, fill="x", padx=10) # This packs the button widget into the menu frame with a vertical padding of 10 pixels and fills the horizontal space.
    btn_patient_data = tk.Button(menu_frame, text="Patient Data", command=open_patient_data, bg="white", bd=2, relief="solid") # This creates a button widget for navigating to the patient data page with the text "Patient Data", a background color of white, a border width of 2, and a solid relief style.
    btn_patient_data.pack(pady=10, fill="x", padx=10) # This packs the button widget into the menu frame with a vertical padding of 10 pixels and fills the horizontal space.
    btn_settings = tk.Button(menu_frame, text="Settings", command=open_settings, bg="white", bd=2, relief="solid") # This creates a button widget for navigating to the settings page with the text "Settings", a background color of white, a border width of 2, and a solid relief style.
    btn_settings.pack(pady=10, fill="x", padx=10) # This packs the button widget into the menu frame with a vertical padding of 10 pixels and fills the horizontal space.
    btn_logout = tk.Button(menu_frame, text="Logout", command=logout, bg="white", bd=2, relief="solid") # This creates a button widget for logging out with the text "Logout", a background color of white, a border width of 2, and a solid relief style.
    btn_logout.pack(pady=10, fill="x", padx=10) # This packs the button widget into the menu frame with a vertical padding of 10 pixels and fills the horizontal space.
    hamburger_btn = tk.Button(window, text="☰", font=("Arial", 16), command=toggle_menu) # This creates a button widget for the hamburger menu with the text "☰", a font size of 16, and a command to toggle the menu visibility.
    hamburger_btn.place(x=10, y=10) # This places the hamburger button at the top left corner of the window with a padding of 10 pixels from the left and top edges.
    window.bind("<Button-1>", close_menu_if_click_outside) # This binds the left mouse button click event to the "close_menu_if_click_outside" function, allowing the menu to close if a click occurs outside of it.
    show_page("HomePage") # This calls the "show_page" function to show the home page.
    window.mainloop() # This starts the main event loop of the Tkinter application, allowing it to run and respond to user events.
if __name__ == "__main__": # This checks if the script is being run as the main program.
    create_window() # This calls the "create_window" function to create and run the main application window.