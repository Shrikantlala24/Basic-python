import random
import string

def Pass_gen(length = 12, up = True, low = True, num = True, sym = True):
    # let's generate a random password
    characters = ''
    if up:
        characters += string.ascii_uppercase   
    if low:
        characters += string.ascii_lowercase
    if num:
        characters += string.digits
    if sym:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    password = "".join(random.choice(characters) for i in range(length))

    return password

if __name__ == "__main__":
    print("🔐 Password Generator 🔐")

    try:
        length = int(input("Enter the length of Password: "))

        print("--- Choose the type of Password ---")
        print("1. All Capital")
        print("2. All Small")
        print("3. Capital + Small + Digits (no Symbols)")
        print("4. Everything should be included")

        choice = int(input("Enter the option: "))

        if choice == 1:
            password = Pass_gen(length, True, False, False, False)
        elif choice == 2:
            password = Pass_gen(length, False, True, False, False)
        elif choice == 3:
            password = Pass_gen(length, True, True, True, False)
        elif choice == 4:
            password = Pass_gen(length, True, True, True, True)
        else:
            print("invalid option")
            exit()

        print("Password :",password)
    except ValueError:
        print("Invalid Length number")


input("Press Enter to exit....")