def add(a, b):
    print("Result:", a + b)

def subtract(a, b):
    print("Result:", a - b)

def multiply(a, b):
    print("Result:", a * b)

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", a / b)



if __name__ == "__main__":
    while(True) :
        print("--- Select an option ---")
        print("1. Add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. exit")

        try:
            choice = int(input("Enter the choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue
    

        if choice == 5:
            print("See you later! goodbye")
            break
        elif choice in (1,2,3,4):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == 1:
                add(a,b)
            elif choice == 2:
                subtract(a,b)
            elif choice == 3:
                multiply(a,b)
            else:
                divide(a,b)
        else:
            print("invalid option")
        

            