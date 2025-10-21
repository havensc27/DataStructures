from stack import Stack

def main():
    back_stack = Stack()
    forward_stack = Stack()
    current_site = None

    while True:
        print("What would you like to do?")
        print("1: Go to a new website")
        print("2: Go back")
        print("3: Go forward")
        print("4: Exit")
        choice = input(">>")

        if choice == "1":
            new_site = input("Enter the website you want to visit: ")
            if new_site:
                back_stack.push(new_site)
            forward_stack = Stack()
            print(f"You are currently browsing this site: {new_site}")

        elif choice == "2":
            if back_stack.empty():
                print("You do not have any browser history")
            else:
                forward_stack.push(current_site)
                current_site = back_stack.pop()
                print(f"You are currently browsing this site: {current_site}")

        elif choice == "3":
            if forward_stack.empty():
                print("You do not have any browser history")
            else:
                back_stack.push(current_site)
                current_site = forward_stack.pop()
                print(f"You are currently browsing this site: {current_site}")

        elif choice == "4":
            print("Exiting browser")
            break
        else:
            print("Invalid choice: Pick 1, 2, 3, or 4")

if __name__ == "__main__":
    main()














