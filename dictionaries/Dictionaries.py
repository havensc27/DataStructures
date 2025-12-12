cars = {}

while True:
    print("Select an option:")
    print("1 - Register a car")
    print("2 - Search for a car")
    print("3 - Exit")
    choice = input(" >>")

    if choice == "1":
        plate = input("Enter the new licence plate number!: ")
        if plate in cars:
            print("A car with this license plate # is already registered.")
        else:
            make = input("Enter your make of car: ")
            model = input("Enter your model of car: ")
            year = input("Enter the year of your car(YYYY): ")
            color = input("Enter your car's color: ")
            cars[plate] = [make, year, color, model]

    elif choice == "2":
        plate = input("Enter the licence plate for search: ")
        if plate in cars:
            details = cars[plate]
            print(f"Make: {details[0]}")
            print(f"Year: {details[1]}")
            print(f"Model: {details[2]}")
            print(f" Color: {details[3]}")
        else:
            print("There is no car with that plate found.")

    elif choice == "3":
        break

    else:
        print("Not an option. Try again.")













