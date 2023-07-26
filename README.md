# Contact Information Extractor

## Description
This Python program extracts phone numbers and email addresses from a given text file using regular expressions. The extracted data is displayed in a tabular format using the PrettyTable library.

## Version
1.0

## Features
- Extracts phone numbers and email addresses from the input text file.
- Displays the extracted data in a tabular format with two columns: "Email Addresses" and "Phone Numbers."
- Handles cases where no phone numbers or email addresses are found in the text.

## Features to be added
- Extract all types of phone numbers from various countries.
- Export extracted information in a CSV file.

## Usage Instructions
1. Replace "input.txt" with the name of your text file containing the text data you want to analyze.
2. Make sure the input text file is in the same directory as this script, or provide the full file path.

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running: `pip install prettytable`
4. Replace "input.txt" with your desired text file.
5. Execute the script: `python contact_information_extractor.py`

## Example Output
```
+-----------------------+------------------+
|   Email Addresses     |  Phone Numbers   |
+-----------------------+------------------+
| john.doe@example.com  |  (123) 456-7890  |
| jane.smith@example.com |  (987) 654-3210  |
+-----------------------+------------------+
```

## Notes
- There are no notes currently.

Feel free to contribute to this project or suggest additional features to be added!
