# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
import sys
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_qualifying_loans(qualifying_loan_list):
    """Prompts the user to confirm a save.  Then, saves the qualifying loans to a CSV file.

    Args:
        qualifying_loan_list (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.

    print (qualifying_loan_list)
    
    confirm_save = questionary.confirm("Would you like to save this loan list?").ask()
    
    if confirm_save:
        header = ["Loan Name"]        #sets the header row of the output CSV file here only loan name
        user_save_path = questionary.text("Where should the file be saved? (for example ./data/").ask()
        user_save_path = user_save_path + questionary.text("What would you like to name the file?").ask()
        output_path = Path(user_save_path)     # sets the path
        with open(output_path, 'w') as csvfile:      #writes each row to csvfile row
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in qualifying_loan_list:
                csvwriter.writerow([row])
        print(f"Your file is saved at {output_path}. Thank you for using the Loan Qualifier App.")
        sys.exit()
    else:
        print("Thank you for using the Loan Qualifier App.")
        sys.exit()
