# Loan Qualifier CLI Application

For all of those times that you have needed a fast way to evaluate loan candidates, LQ-CLI gives you a simple method to determine which banks will offer loans to your clients.

---

## Technologies

LQ-CLI runs on Python.  It imports the following:
- Questionary
- Sys
- Fire
- csv
- Path from pathlib

Additionally, LQ-CLI contains several imported functions found in the following:
- ./qualifier/filters
- ./qualifier/utils

Data is stored in the ./data/ folder.
---

## Installation Guide

To install, create a local clone of the github repository (https://github.com/justcb/loan_qualifier_app).  

To run LQ-CLI, in the root directory of the loan_qualifier_app, type 
`python app.py`.


---

## Usage

To use the app:

1.  When prompted, enter the directory for the daily_rate_sheet.csv by typing `./data/daily_rate_sheet.csv`.
2.  You will then be prompted for the following information:
    A.  Credit Score
    B.  Current Monthly Debt
    C.  Current Monthly Income
    D.  Total Monthly Income
    E.  Desired Loan Amount
    F.  Home Value
3.  After the data is entered, LQ-CLI will filter the loans based on the following filters:
    A.  Maximum Loan Size
    B.  Credit Score
    C.  Monthly Debt to Income 
    D.  Loan to Value
4.  You see the following results:
    A.  Debt to Income Ratio
    B.  Loan to Value Ratio
    C.  The number of qualifying loans
    D.  A list of the qualifying loan names
5.  You will be prompted to confirm whether you would like to save the loan list.
6.  If you do, you will be prompted to enter the path and file name for your list.

---

## Contributors

This project was created as a part of the Rice FinTech Bootcamp.

---

## License

This software is licensed for use under the included MIT License.