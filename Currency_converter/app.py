def convert_currency(amount, exchange_rate):  
    return amount * exchange_rate 

if __name__ == "__main__":

    print("Currency Converter") 
    print("1. USD to EUR") 
    print("2. EUR to USD") 

    choice = input("Enter your choice (1/2): ") 

    if choice == '1': 
        amount_usd = float(input("Enter amount in USD: ")) 
        exchange_rate_eur = 0.85  # Example exchange rate: 1 USD to EUR 
        amount_eur = convert_currency(amount_usd, exchange_rate_eur) 
        print(f"${amount_usd:.2f} USD is equal to €{amount_eur:.2f} EUR") 

    elif choice == '2': 
        amount_eur = float(input("Enter amount in EUR: ")) 
        exchange_rate_usd = 1.18  # Example exchange rate: 1 EUR to USD 
        amount_usd = convert_currency(amount_eur, exchange_rate_usd) 
        print(f"€{amount_eur:.2f} EUR is equal to ${amount_usd:.2f} USD") 

    else: 
        print("Invalid choice")

input("Press Enter to exit...")