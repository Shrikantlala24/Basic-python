def C_to_F(c):
    return c * (9 / 5) + 32

def F_to_C(f):
    return (f - 32) * (5 / 9)

if __name__ == "__main__":

    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter the Option: "))
    except ValueError:
        print("❌ Error: Enter a number")
        exit()

    if choice == 1:
        try:
            c = float(input("Enter the temperature in Celsius: "))
            f = C_to_F(c)
            print(f"{c}°C is equal to {f:.2f}°F")
        except ValueError:
            print("❌ Enter a valid real number")

    elif choice == 2:
        try:
            f = float(input("Enter the temperature in Fahrenheit: "))
            c = F_to_C(f)
            print(f"{f}°F is equal to {c:.2f}°C")
        except ValueError:
            print("❌ Enter a valid real number")

    else:
        print("❌ Invalid Choice number")

# Your logic here...
input("\nPress Enter to exit...")
