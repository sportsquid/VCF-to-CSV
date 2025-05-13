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

#function to handle import file dialogue 
def select_import_file():
    file_path = filedialog.askopenfilename(
    title="Select a file",
    initialdir="C:\\",
    filetypes=(("VCard File", "*.vcf"), ("All files", "*.*"))
    )
    file_to_import.set(file_path)

def write_contact(contact, filepath):
    with open(filepath, 'w') as file:
        file.write(f"{contact.first_name}, {contact.last_name}, {contact.display_name}, {contact.nickname}, {contact.email1}, {contact.email2}, " \
                    f"{contact.email3}, {contact.home_phone}, {contact.business_phone}, {contact.home_fax}, {contact.business_fax}, {contact.pager}," \
                    f"{contact.mobile_phone}, {contact.home_street}, {contact.home_address2}, {contact.home_city}, {contact.home_state}, {contact.home_postal}," \
                    f"{contact.home_country}, {contact.business_address}, {contact.business_address_2}, {contact.business_city}, {contact.business_state}, {contact.business_postal}, {contact.business_country}, {contact.country_code}, {contact.related_name}," \
                    f"{contact.job_title}, {contact.department}, {contact.organization}, {contact.notes}, {contact.birthday}, {contact.anniversary}," \
                    f"{contact.gender}, {contact.web_page}, {contact.web_page2}, {contact.categories}")
        return 

#function to convert the CSV 
def convert_contacts():
    file_path = filedialog.asksaveasfilename(
    title="Save contacts as...",
    defaultextension=".csv",
    filetypes=[("CSV", "*.csv")],
    initialdir="C:\\",
    )
    if(file_path == ""):
        convert_contacts()
        return
    #write first line in CSV
    with open(file_path, 'w') as file:
        file.write("First Name,Last Name,Display Name,Nickname,E-mail Address,E-mail 2 Address,E-mail 3 Address,Home Phone,Business Phone,Home" \
                   "Fax,Business Fax,Pager,Mobile Phone,Home Street,Home Address 2,Home City,Home State,Home Postal Code,Home Country,Business Address," \
                   "Business Address 2,Business City,Business State,Business Postal Code,Business Country,Country Code,Related name,Job Title,Department,Organization," \
                   "Notes,Birthday,Anniversary,Gender,Web Page,Web Page 2,Categories")

    #load entire file into list
    lines = []
    with open(file_to_import, 'r') as file:
       current_contact = Contact()
       for line in file:
           if(line.strip() == "END:VCARD"):
               write_contact(current_contact, file_path)
               current_contact = Contact()
           elif (line.strip().startswith("N:") != -1):
               pass
                
    
    


#Create Window
root = tk.Tk()
root.title("Altorfer iPhone Contact Converter")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=3, column=2)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
file_to_import = tk.StringVar()

#Basic UI layout
ttk.Label(mainframe, text="Import Contacts:").grid(row=1, column=1)
import_entry = ttk.Entry(mainframe, width=75, textvariable=file_to_import).grid(column=1, row=2, sticky=tk.W)
ttk.Button(mainframe, text="Select File...", command=select_import_file).grid(row=2, column=2)
ttk.Button(mainframe, text="Convert", command=convert_contacts).grid(row=3, column=1)

root.mainloop()