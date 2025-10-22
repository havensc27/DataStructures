from stack import Stack

def rpn_calculator():
    stack = Stack()
    print("RPM Calculator. Type 'exit' to quit.")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            break

        if user_input in {"+", "-", "*", "/"}:
            if stack.size() < 2:
                print("Error, there is not enough #'s")
                continue

            a = stack.pop()
            b = stack.pop()

            try:
                if user_input == "+":
                    result = a + b
                elif user_input == "-":
                    result = b - a
                elif user_input == "*":
                    result = a * b
                elif user_input == "/":
                    result = a / b

                print(result)
                stack.push(result)
            except ZeroDivisionError:
                print("Error, / by 0")
                stack.push(a)
                stack.push(b)

        else:
            try:
                number = float(user_input)
                stack.push(number)
            except ValueError:
                print("Error, invalid input")

if __name__ == "__main__":
    rpn_calculator()