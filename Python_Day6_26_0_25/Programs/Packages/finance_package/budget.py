def budget_calculator(income, expense):
    if not isinstance(income, (int, float)) or not isinstance(expense, (int, float)):
        raise ValueError("Income and expense must be numeric values only.")
    if income < 0 or expense < 0:
        raise ValueError("Income and expense cannot be negative.")
    return income - expense