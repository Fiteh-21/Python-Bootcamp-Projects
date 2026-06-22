# 🧮 Pythonista CLI Calculator

A clean, recursive **command-line calculator** built with Python. This tool uses a modular **function-mapping approach** to perform basic arithmetic operations and supports **continuous calculations** without restarting.

---

## 🚀 Features

- **Modular Arithmetic**  
  Separate functions for addition, subtraction, multiplication, and division.

- **Dictionary Mapping**  
  Uses a dispatch table (operations dictionary) to link mathematical symbols to functions.

- **Continuous Calculation**  
  Allows users to use the result of a previous calculation as the starting point for the next one.

- **Recursive Restart**  
  Automatically resets and starts a fresh calculation session when requested.

- **ASCII Interface**  
  Includes a stylized *Pythonista* digital calculator logo for a better user experience.

---

## 🛠️ How It Works

The program follows a clear execution flow:

1. **Input**  
   Accepts the first number (`num1`).

2. **Select**  
   Displays available operators (`+`, `-`, `*`, `/`) for selection.

3. **Compute**  
   Performs the calculation using the function mapped to the chosen symbol.

4. **Loop**  
   Asks the user if they want to continue with the current answer or start a new session.

---

## 💻 Installation & Usage

1. Clone the repository:

```bash
git clone [https://github.com/Fiteh-21/Python-CLI-Calculator/]
```
2. Navigate to the project directory:

```bash
cd PyCalc-Flow
```
3. Run the application:

```bash
python calculator.py
```

---

## 📝 Code Structure

- **`operations` Dictionary**  
  Acts as the engine of the calculator, mapping operator symbols to callable functions.

- **`calculator()` Function**  
  The main driver that handles user input, calculations, and session state.

- **Recursion**  
  The script calls itself (`calculator()`) to reset memory and start a fresh calculation without exiting the program.

