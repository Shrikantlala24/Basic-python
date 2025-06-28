# 🔐 Password Generator

A simple, interactive Python script to generate secure and customizable passwords directly from the terminal.

---

## 💡 Features

* ✅ Generate random passwords of any length
* 🔠 Four preset modes to choose from:

  * All Capital Letters
  * All Small Letters
  * Capital + Small + Digits (No Symbols)
  * Capital + Small + Digits + Symbols
* ❓ Input validation for length and selection
* 🔹 Clear user interface and exit prompt

---

## 📁 Project Structure

```bash
├── app.py
└── README.md
```

---

## 💥 How to Run

1. **Install Python 3** if not already installed

2. **Clone the Repository**

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

3. **Run the Script**

```bash
python password_generator.py
```

---

## 🎓 How It Works

* Prompts the user to enter the desired length of the password.
* Displays four options:

  * `1`: Only uppercase characters
  * `2`: Only lowercase characters
  * `3`: Uppercase + lowercase + digits
  * `4`: All of the above + symbols
* Generates the password using the built-in `random` and `string` libraries.
* Displays the result and waits for user confirmation to exit.

---

## 🚀 Example Output

```
🔐 Password Generator 🔐
Enter the length of Password: 12
--- Choose the type of Password ---
1. All Capital
2. All Small
3. Capital + Small + Digits (no Symbols)
4. Everything should be included
Enter the option: 4

Password : hG3&n8P#qD!m
Press Enter to exit....
```

---

## 💼 License

This project is licensed under the MIT License.

---

## ✨ Contributions

Pull requests and suggestions are welcome!

---

## 🚀 Author

Built with ❤️ in python
