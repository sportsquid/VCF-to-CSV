import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys

class Contact:
    first_name = ""
    last_name = ""
    display_name = ""
    nickname = ""
    email1 = ""
    email2 = ""
    email3 = ""
    home_phone= ""
    business_phone = ""
    home_fax = ""
    business_fax = ""
    pager = ""
    mobile_phone = ""
    home_street = ""
    home_address_2 = ""
    home_city = ""
    home_state = ""
    home_postal = ""
    home_country = ""
    business_address = ""
    business_address_2 = ""
    business_city = ""
    business_state = ""
    business_postal = ""
    business_country = ""
    country_code = ""
    related_name = ""
    job_title = ""
    department = ""
    organization = ""
    notes = ""
    birthday = ""
    anniversary = ""
    gender = ""
    web_page = ""
    web_page_2 = ""
    categories = ""

def select_import_file():
    file_path = filedialog.askopenfilename(
    title="Select a file",
    initialdir="C:\\",
    filetypes=(("VCard File", "*.vcf"), ("All files", "*.*"))
    )
    file_to_import.set(file_path)

def convert_contacts():
    pass
    

root = tk.Tk()
root.title("Altorfer iPhone Contact Converter")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=3, column=2)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
file_to_import = tk.StringVar()

#import file UI
ttk.Label(mainframe, text="Import Contacts:").grid(row=1, column=1)
import_entry = ttk.Entry(mainframe, width=75, textvariable=file_to_import)
import_entry.grid(column=1, row=2, sticky=tk.W)
ttk.Button(mainframe, text="Select File...", command=select_import_file).grid(row=2, column=2)
ttk.Button(mainframe, text="Convert", command=convert_contacts).grid(row=3, column=1)

root.mainloop()