# 🏛️ Caesar Cipher Python Tool

A lightweight, interactive **command-line interface (CLI)** application that allows users to encrypt and decrypt messages using the classic **Caesar Cipher** technique.

---

## 🏛️ About the Project

The **Caesar Cipher** is one of the earliest and simplest forms of encryption. It is a substitution cipher where each letter in the original message is replaced by a letter a fixed number of positions down the alphabet.

This project provides a **user-friendly way to experiment** with this historical cryptographic method directly from the terminal.

---

## ⚙️ How it Works

The script utilizes a mathematical shift to transform text.  
For any given character \( x \) and shift \( n \), the encryption \( E \) is defined as:

$$
E_n(x) = (x + n) \mod 26
$$


### In this implementation, the code handles:

- **Encoding**  
  Shifts characters forward to hide the message.
- **Decoding**  
  Shifts characters backward to reveal the original text.
- **Non-Alphabetical Characters**  
  Symbols, numbers, and spaces are preserved and remain unchanged.

---

## ✨ Features

- **Interactive Loop**  
  Encrypt or decrypt multiple messages without restarting the program.
- **Shift Protection**  
  Uses modulo arithmetic (`shift % 25`) to safely handle shift values larger than the alphabet length.
- **Input Cleaning**  
  Automatically converts user input to lowercase for consistent processing.
- **ASCII Art**  
  Includes a stylized *Caesar Cipher* logo for an enhanced user experience.

---

## 🚀 Installation

Ensure you have **Python 3.x** installed on your machine.

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/CaesarShift-Py.git
    ```
2. Navigate to the project directory:

  ```bash
  cd CaesarShift-Py
  ```

---

## 🛠 Usage

Run the script from your terminal:

  ```bash
  python caesarCipher.py
  ```

Follow the on-screen prompts:

  - Choose encode or decode
  - Type your secret message
  - Enter the shift number (the encryption key)

---

Have fun exploring one of history’s oldest encryption techniques! 🔐📜
