# 🔐 PyPassword Generator

A simple yet effective Python script that generates **strong, randomized passwords** based on user-defined criteria for letters, symbols, and numbers.

---

## 🚀 How It Works

The program prompts the user to specify how many characters they want from each category:

- Letters
- Symbols
- Numbers

It then:

1. Randomly selects characters from predefined lists.
2. Combines all selected characters into a single list.
3. Shuffles the list to eliminate predictable patterns (e.g., letters first, then symbols, then numbers).
4. Outputs the final password as a secure string.

---

## 🛠️ Features

- **Customizable Length**  
  Choose exactly how many letters, symbols, and numbers your password contains.

- **True Randomization**  
  Uses Python’s `random.shuffle()` to prevent ordered character grouping.

- **Easy to Use**  
  Run directly from any Python-enabled terminal—no extra dependencies required.

---

## 📋 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Fiteh-21/pypassword-generator.git
```
### 2️⃣ Navigate to the Project Directory
```bash
cd pypassword-generator
```
### 3️⃣ Run the Script
```bash
python project5.py
```
## 🧠 Logic Breakdown

The core logic converts the generated characters into a list to allow shuffling, ensuring a stronger password:
```bash
# The combined list is shuffled to ensure a 'Hard' password level
combined = list(letters_password + symbols_password + numbers_password)
random.shuffle(combined)
password = ''.join(combined)
```
