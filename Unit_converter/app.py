def meters_to_feet(meters): 
    return meters * 3.281 
 
def feet_to_meters(feet): 
    return feet / 3.281 

if __name__ == "__main__":
    print("Unit Converter: Length") 
    print("1. Meters to Feet") 
    print("2. Feet to Meters") 
    
    choice = input("Enter your choice (1/2): ") 
    
    if choice == '1': 
        meters = float(input("Enter length in meters: ")) 
        feet = meters_to_feet(meters) 
        print(f"{meters} meters is equal to {feet:.2f} feet") 
    elif choice == '2': 
        feet = float(input("Enter length in feet: ")) 
        meters = feet_to_meters(feet) 
        print(f"{feet} feet is equal to {meters:.2f} meters") 
    else: 
        print("Invalid choice")

input("Press Enter to exit...")