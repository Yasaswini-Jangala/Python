from finance_package import tax as t, budget as b
def main():
    try:
        income = float(input("Enter the Income: "))
        tax_rate = float(input("Enter the Tax Rate (%): "))
        expense = float(input("Enter the Expense: "))
        print(f"Tax: {t.calculate_tax(income, tax_rate)}")
        print(f"Budget: {b.budget_calculator(income, expense)}")
    except ValueError as err:
        print("Error:", err)
main()