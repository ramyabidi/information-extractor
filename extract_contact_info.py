######################################################
#                                                    #
#    Contact Information Extractor - Version 1.0     #
#                                                    #
######################################################

import re
from prettytable import PrettyTable

file_path = "input.txt"  # Replace "input.txt" with the name of your TXT file containing the text data

# Read text from the file
with open(file_path, "r") as file:
    text = file.read()

phone_pattern = re.compile(r'''
    (                   # Start of phone number group
    \d{3}               # Three digits for area code
    [-.\s]?             # Optional separator (dash, dot, or space)
    \d{3}               # Three digits for exchange code
    [-.\s]?             # Optional separator
    \d{4}               # Four digits for line number
    )                   # End of phone number group
''', re.VERBOSE)

email_pattern = re.compile(r'''
    [a-zA-Z0-9._%+-]+  # Username
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # Domain name
    \.[a-zA-Z]{2,}    # Top-level domain (e.g., .com, .org)
''', re.VERBOSE)

phone_numbers = phone_pattern.findall(text)  # Find all phone numbers in the text
email_addresses = email_pattern.findall(text)  # Find all email addresses in the text

if not phone_numbers and not email_addresses:
    print("No phone numbers or email addresses found in the text.")
else:
    table = PrettyTable()  # Create a PrettyTable instance to display the results
    table.field_names = ["Email Addresses", "Phone Numbers"]  # Set table column headers

    # Extend lists to have equal length to create rows in the table
    max_length = max(len(email_addresses), len(phone_numbers))
    email_addresses.extend([""] * (max_length - len(email_addresses)))
    phone_numbers.extend([""] * (max_length - len(phone_numbers)))

    # Add email addresses and phone numbers to the table row by row
    for email, phone in zip(email_addresses, phone_numbers):
        table.add_row([email, phone])

    print(table)  # Display the table with email addresses and phone numbers