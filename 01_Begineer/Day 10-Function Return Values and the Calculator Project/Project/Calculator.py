import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    }

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


def calculation_recursive(result):
    keep_calculating = input(f"Type 'y' to calculating with {result}, or type 'n' to exit.:  ").lower()
    if keep_calculating == 'n':
        return result
    opera_symbol = input("Pick another operation: ")

    num3 = float(input("What's the next number?: "))
    calculation = operations[opera_symbol]
    second_answer = calculation(result, num3)

    print(f"{result} {opera_symbol} {num3} = {second_answer}")
    calculation_recursive(second_answer)


calculation_recursive(answer)
