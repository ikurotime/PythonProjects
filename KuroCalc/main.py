from art import logo

print(logo)
def calculator():
    def add(n1, n2):
        return n1 + n2

    def substract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What's the first number?\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation\n")
        num2 = float(input("What's the next number?\n"))
        calc_fn = operations[operation_symbol]
        answer = calc_fn(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()