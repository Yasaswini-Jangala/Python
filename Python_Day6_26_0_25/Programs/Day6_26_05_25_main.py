import module_mathematics as maths
def main():
  num1 = int(input("Enter num1 to perform Mathematical Operations: "))
  num2 = int(input("Enter num2 to perform Mathematical Operations: "))
  print(f'Addition of {num1} and {num2} is: {maths.addition(num1, num2)}')
  print(f'Subtraction of {num1} and {num2} is: {maths.subtraction(num1, num2)}')
  print(f'Product of {num1} and {num2} is: {maths.multiply(num1, num2)}')
  print(f'Modulo of {num1} and {num2} is: {maths.modulo(num1, num2)}')
  print(f'Div1, Div2 of {num1} and {num2} is: {maths.div(num1, num2)}')
main()