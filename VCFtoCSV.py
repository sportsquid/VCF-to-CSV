import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

class Contact:
    first_name = "" #supported
    last_name = "" #supported
    display_name = ""
    nickname = ""
    email1 = "" #supported (Home)
    email2 = "" #supported (Work)
    email3 = ""
    home_phone= "" #supported
    business_phone = "" #supported
    home_fax = "" #supported
    business_fax = "" #supported
    pager = "" #supported
    mobile_phone = "" #supported
    home_street = "" #supported
    home_address_2 = ""
    home_city = "" #supported
    home_state = "" #supported
    home_postal = "" #supported
    home_country = "" #supported
    business_address = "" #supported
    business_address_2 = ""
    business_city = "" #supported
    business_state = "" #supported
    business_postal = "" #supported
    business_country = "" #supported
    country_code = ""
    related_name = ""
    job_title = "" #supported
    department = "" #supported
    organization = "" #supported
    notes = "" #supported
    birthday = "" #supported
    anniversary = ""
    gender = ""
    web_page = "" #supported
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
    with open(filepath, 'a', encoding="utf-8") as file:
        file.write(f"{contact.first_name},{contact.last_name},{contact.display_name},{contact.nickname},{contact.email1},{contact.email2}," \
                    f"{contact.email3},{contact.home_phone},{contact.business_phone},{contact.home_fax},{contact.business_fax},{contact.pager}," \
                    f"{contact.mobile_phone},{contact.home_street},{contact.home_address_2},{contact.home_city},{contact.home_state},{contact.home_postal}," \
                    f"{contact.home_country},{contact.business_address},{contact.business_address_2},{contact.business_city},{contact.business_state},{contact.business_postal},{contact.business_country},{contact.country_code},{contact.related_name}," \
                    f"{contact.job_title},{contact.department},{contact.organization},{contact.notes},{contact.birthday},{contact.anniversary}," \
                    f"{contact.gender},{contact.web_page},{contact.web_page_2},{contact.categories}\n")
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
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write("First Name,Last Name,Display Name,Nickname,E-mail Address,E-mail 2 Address,E-mail 3 Address,Home Phone,Business Phone,Home" \
                   "Fax,Business Fax,Pager,Mobile Phone,Home Street,Home Address 2,Home City,Home State,Home Postal Code,Home Country,Business Address," \
                   "Business Address 2,Business City,Business State,Business Postal Code,Business Country,Country Code,Related name,Job Title,Department,Organization," \
                   "Notes,Birthday,Anniversary,Gender,Web Page,Web Page 2,Categories\n")

    #load entire file into list
    lines = []
    with open(file_to_import.get(), 'r', encoding="utf-8") as file:
        current_contact = Contact()
        try:
            for line in file:
                if(line.strip() == "END:VCARD"):
                    write_contact(current_contact, file_path)
                    current_contact = Contact()
                #first and last name
                elif (line.strip().startswith("N:")):
                    current_contact.first_name = line.strip().split(";")[1]
                    current_contact.last_name = line.strip().split(";")[0].split(":")[1]
                #home email
                elif(line.strip().startswith("EMAIL;type=INTERNET;type=HOME")):
                    current_contact.email1 = line.strip().split(":")[1]
                #work email
                elif(line.strip().startswith("EMAIL;type=INTERNET;type=WORK")):
                    current_contact.email1 = line.strip().split(":")[1]
                #home phone
                elif(line.strip().startswith("TEL;type=HOME") and ("type=FAX" not in line.strip())):
                    current_contact.home_phone = line.strip().split(":")[1]
                #work phone
                elif(line.strip().startswith("TEL;type=WORK") and ("type=FAX" not in line.strip())):
                    current_contact.work_phone = line.strip().split(":")[1]
                #cell phone
                elif(line.strip().startswith("TEL;type=CELL")):
                    current_contact.mobile_phone = line.strip().split(":")[1]
                elif(line.strip().startswith("TEL;type=pref")):
                    current_contact.mobile_phone = line.strip().split(":")[1]
                #pager
                elif(line.strip().startswith("TEL;type=PAGER;")):
                    current_contact.pager = line.strip().split(":")[1]
                #home fax
                elif(line.strip().startswith("TEL;type=HOME;type=FAX")):
                    current_contact.home_fax = line.strip().split(":")[1]
                #work fax
                elif(line.strip().startswith("TEL;type=WORK;type=FAX")):
                    current_contact.business_fax = line.strip().split(":")[1]
                #home address
                elif("ADR;type=HOME" in line.strip()):
                    current_contact.home_street = line.strip().split(":")[1].split(";")[2].replace("\\n", " ")
                    current_contact.home_city = line.strip().split(":")[1].split(";")[3]
                    current_contact.home_state = line.strip().split(":")[1].split(";")[4]
                    current_contact.home_postal = line.strip().split(":")[1].split(";")[5]
                    current_contact.home_country = line.strip().split(":")[1].split(";")[6]
                #business address
                elif("ADR;type=WORK" in line.strip()): 
                    current_contact.business_city = line.strip().split(":")[1].split(";")[3]
                    current_contact.business_state = line.strip().split(":")[1].split(";")[4]
                    current_contact.business_postal = line.strip().split(":")[1].split(";")[5]
                    current_contact.business_country = line.strip().split(":")[1].split(";")[6]
                    current_contact.business_address = f"\"{line.strip().split(":")[1].split(";")[2].replace("\\n", " ")}, {current_contact.business_city}, " \
                        f"{current_contact.business_state}, {current_contact.business_postal}, {current_contact.business_country}\""
                #organization
                elif(line.strip().startswith("ORG")):
                    current_contact.organization = line.strip().split(":")[1].split(";")[0].strip()
                    current_contact.department = line.strip().split(":")[1].split(";")[1].strip()
                #job title
                elif(line.strip().startswith("TITLE:")):
                    current_contact.job_title = line.strip().split(":")[1]
                elif(line.strip().startswith("NOTE:")):
                    current_contact.notes = f"\"{line.strip()[5:]}\""
                #birthday
                elif(line.strip().startswith("BDAY:")):
                    current_contact.birthday = line.strip().split(":")[1]
                #website
                elif("URL;" in line.strip()):
                    current_contact.web_page = line.strip().split(":")[1]
        except Exception as err:
            messagebox.showinfo("Status", "An error has occured processing this file. Please contact IT")
        else:
            file_to_import.set("")
            messagebox.showinfo("Status", "Contacts Successfully Converted")
    
    
    


#Create Window
root = tk.Tk()
root.title("Altorfer iPhone Contact Converter")
root.iconbitmap("./Contact Converter.ico")
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