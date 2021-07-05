# Import pathlib
from pathlib import Path
import csv
#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    csvpath = Path("./data/output/qualifying_loans.csv")

# Set the output header
header = ["credit_score", "debt_to_income", "loan_to_value", "max_loan_size"]

# Set the output file path
output_path = Path("qualifying_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

csvpath = Path("./data/output/qualifying_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write our header row first!
    csvwriter.writerow(header)

    # Then we can write the data rows
    for row in csvfile:
        csvwriter.writerow(row.values())
 

def  test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!

def test_save_csv():       
         
         assert test_save_csv() == True
