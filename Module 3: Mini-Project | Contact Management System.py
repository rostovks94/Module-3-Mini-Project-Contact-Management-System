# Module 3: Mini-Project | Contact Management System
# Introduction
# Welcome to the Contact Management System project! In this project, you will apply your Python programming skills to create a functional command-line-based application that simplifies the management of your contacts. The Contact Management System will empower you to add, edit, delete, and search for contacts with ease, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.
# Project Requirements
# Your task is to develop a Contact Management System with the following features:
# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:
# Welcome to the Contact Management System! 
# Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file
# Quit 
# > 
# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name -required
# Phone number -required
# Email address -required
# Additional information (e.g., address, notes). -optional
# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact with all relevant details.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact by searching for their email.
# Searching for a contact by their unique email and displaying their details.
# Displaying a list of all contacts.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system.
# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include clear instructions on how to run the application and explanations of its features.
# Provide examples and screenshots, if possible, to enhance user understanding.
# Include a link to your GitHub repository in your project documentation.
# Optional Bonus Points
# Contact Categories : Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories, and add an action to your menu to "Show Categories" where they choose a category and all those contacts are shown.
# Automating Contact Import and Export : Intuitively importing the file data at the beginning of your app and automatically store after addition and editing your contactsa

# regular expression:

import re

# initializing an empty dictionary named @contacts" which will be used to store contact information:

contacts = {}

# This regex pattern ensures that the phone number consists of exactly 10 digits (\d{10}):
# ^: Asserts the start of the string;
# \d{10}: Matches exactly 10 digits:
# \d: Matches any single digit character from 0 to 9;
# $: Asserts the end of the string.

phone_regex = re.compile(r'^\d{10}$')

# This regex pattern validates the format of email addresses:
# ^: Asserts the start of the string.
# \S+: Matches one or more non-whitespace characters (the username part).
# @: Matches the "@" symbol.
# \S+: Matches one or more non-whitespace characters (the domain part).
# \.: Matches a literal dot "." character.
# \S+: Matches one or more non-whitespace characters (the top-level domain part).
# $: Asserts the end of the string.

email_regex = re.compile(r'^\S+@\S+\.\S+$')

#Defining aa funnction named "display_menu()":

def display_menu():

# Printing a welcome message and display a menu of options for the user to interact with the system:

    print ("\nWelcome to contact Managment System!")
    print ("Menu:")
    print ("1. Add a new contact.")
    print ("2. Edit an existing contact.")
    print ("3. Delete an existing contact.")
    print ("4. Search for a contact")
    print ("5. Display all contacts")
    print ("6. Export contacts to a text file.")
    print ("7. Import contacts from a text file." )
    print ("8. Quit")

# Defining a function named "add_contact()":

def add_contact():
    print ("\nAdding a new contact: ")
    name = input ("Enter name: ")
    phone = input("Enter phone number: ")

    # Validating the entered phone number using the "phone_regex" regular expression pattern.
    # If the pattern doesn't match the patttern, the user is prompted to enter it again until a valid number is provided.

    while not phone_regex.match(phone):
        print ("Invalid phone number format. Please, enter 10 digits.")
        phone = input("Enter phone number: ")
    email = input ("Enter email address: ")

    # the same as with the phone number, the user will be prompted to enter email again until a valid email address is provided.
    
    while not email_regex.match(email):
        print ("Invalid email address format.")
        email = input ("Enter email address: ") 
    additional_info = input ("Enter contact information (optional): ")

    # Adding the new contact to the contacts dictionary with the phone number as the key and a dictionary containing the contact details as the value:

    contacts[phone] = {"Name": name, "Phone": phone, "Email": email, "Contact Info": additional_info}
    
    # Confirmation number:
    
    print ("Contact added successfully!")


def edit_contact():
    print("\nEditing an existing contact:") 
    phone = input ("Enter phone number of the contact you would like to edit: ")

    # Checking if the entered email exists in the contacts dictionary.
    if phone in contacts:
        print ("Contatc found. Enter new details: ")

        #  Prompts the user to enter a new name for the contact. 
        # If the user enters nothing (presses Enter), it defaults to the existing name of the contact. 

        name = input (f"Enter new name ({contacts[phone]['Name']})): ") or contacts[phone]['Name']  

        # ({contacts[phone]['Name']}): This part of the string displays the current name associated with the contact's phone number (phone). 
        # It retrieves the name from the contacts dictionary using the phone variable as the key. This allows the user to see the current name while being prompted to enter a new one.) followed by : ": These characters close the parentheses and start the string again.
        # or contacts[phone]['Name']:  A logical OR operator (or) is checking if the input provided by the user is a falsy value (such as an empty string). If the user enters nothing or just presses Enter, the input() function will return an empty string, which is considered falsy. 
        # In this case, the expression on the right side of the or operator (contacts[phone]['Name']) will be evaluated. This retrieves the current name associated with the contact's phone number from the contacts dictionary. 
        # The same as the name.

        new_phone = input (f"Enter new phone number ({contacts[phone]['Phone']}): ") or contacts[phone]['Phone']
        while not phone_regex.match(new_phone):
            print("Invalid phone number format. Please enter 10 digits.")
            new_phone = input(f"Enter new phone number ({contacts[phone]['Phone']}): ")
        email = input(f"Enter new email address ({contacts[phone]['Email']}): ") or contacts[phone]['Email']

        # Validates the new email address format using the email_regex.
        while not email_regex.match(email):
            print("Invalid email address format.")
            email = input(f"Enter new email address ({contacts[phone]['Email']}): ")

        additional_info = input(f"Enter new Additional information ({contacts[phone]['Additional Info']}): ")

        # Updating the contact details in the contacts dictionary.
        contacts[phone] = {
            "Name": name,
            "Phone": new_phone,
            "Email": email,
            "Additional Info": additional_info
        }

        print ("Contact updated successfully!")
    else:
        print ("Contact not found!")



def delete_contact():
    print ("\nDeleting a contact:")
    phone = input ("Enter phone number you would like to delete: ")
    if phone in contacts:
        del contacts[phone]
        print ("Contact deleted successfully!")
    else:
        print ("Contact not found.")


def search_contact_by_phone():
    print ("\nSerachong for a contact:")
    phone = input ("Enter phone number of the contact you would like to search: ")
    found_contacts = [contact for contact in contacts.values() if contact['Phone'] == phone]
    if found_contacts:
        print("\nContact found:")
        for contact in found_contacts:
            print_contact_details(contact)
    else:
        print ("Contact not found.")


def print_contact_details(contact):
    print ("Name:", contact["Name"])
    print ("Phone:", contact["Phone"])
    print ("Email:", contact["Email"]) 
    print ("Additional Info:", contact["Additional Info"])



def display_contacts():
    print ("\nAll contacts:")
    if contacts:
        for contact in contacts.values():
            print_contact_details(contact)
    else:
        print("No contacts avaiable.")


def export_contacts():
    filename = input ("Enter filename to export contacts (include extension, e. g., contacts.txt): ")
    with open(filename, 'w') as file:
        for contact in contacts.values():
            file.write(f"Name: {contact['Name']}\n")
            file.write(f"Phone: {contact['Phone']}\n")
            file.write(f"Email: {contact['Email']}\n")
            file.write(f"Additional Info: {contact['Additional Info']}\n") 
            file.write('\n') 
    print ("Contacts exported successfully!")



def import_contacts():
    filename = input ("Enter filename to import contacts from (include extension, e. g., contacts.txt): ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                name = lines[i].strip().split(": ")[1]
                phone = lines[i+1].strip().split(": ")[1]
                email = lines[i+2].strip().split(": ")[1]
                additional_info = lines[i+3].strip().split(": ")[1]
                contacts[phone] = {'Name': name, 'Phone': phone, 'Email': email, 'Additional Info': additional_info}
        print ("Contact important successfullly!")
    except FileNotFoundError:   
        print ("File not found.")


while True:
    display_menu()
    choice = input("\nEnter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact() 
    elif  choice == '4':
        search_contact_by_phone()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        export_contacts()
    elif choice == '7':
        import_contacts()
    elif choice == '8':
        print ("Thank you for using The Contact Managment System!")
        break 
    else:
        print ("Invalid choice. Please enter a number from 1 to 8")                   

