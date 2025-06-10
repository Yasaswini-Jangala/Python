try:
  balance = float(input("Enter the Balance Amount in the Account: "))
except ValueError:
  print("Please Enter Only {Integer.Decimal} Values")
def calculate_balance(amount):
  try:
    amount = float(input("Enter the amount to Withdraw: "))
    if amount < 0:
      raise ValueError("Withdrawal amount must be greateer than 0")
    if amount > balance:
      raise Exception("Insufficient Balance")
    balance -= amount
    print(f"Withdrawal Successful, Remaining Balance: ₹{balance}")
  except ValueError as ve:
    print(f"ValueError: {ve}")
  except ZeroDivisionError:
    print("Can't diivde by Zero")
  except FileNotFoundError:
    print("Log File not Found. Cannot Log Transaction")
  except Exception as e:
    print(f"An Error Occured: {e}")
  else:
    print("Transaction Processed Without any Error")
  finally:
    print("ThankYou Visit Again")
calculate_balance(balance)