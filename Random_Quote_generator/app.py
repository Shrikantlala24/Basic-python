import random

def Quote_gen() :
     quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs", 
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost", 
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson", 
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt", 
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "You miss 100%% of the shots you don’t take. - Wayne Gretzky",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Dream big and dare to fail. - Norman Vaughan",
    "Act as if what you do makes a difference. It does. - William James",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Don’t wait. The time will never be just right. - Napoleon Hill",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "If you’re going through hell, keep going. - Winston Churchill",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi"
    ]


     return random.choice(quotes)

if __name__ == "__main__":
     print("Welcome to Random Quote generator")
     print("\n---> ✏️",Quote_gen())


input("\nPress Enter to exit...")