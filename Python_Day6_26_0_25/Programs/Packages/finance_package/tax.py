def calculate_tax(income, tax_rate):
    if not isinstance(income, (int, float)) or not isinstance(tax_rate, (int, float)):
        raise ValueError("Income and tax-rate must be numeric values only.")
    if income < 0 or tax_rate < 0:
        raise ValueError("Income and tax-rate cannot be negative.")
    return income * (tax_rate / 100)