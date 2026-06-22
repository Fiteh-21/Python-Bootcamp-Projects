# 🧠 OOP Quiz Engine

A modular **Command Line Interface (CLI)** trivia application built with Python. This project demonstrates the use of **Object-Oriented Programming (OOP)** principles to manage game logic, data modeling, and user interaction.

---

## 🧠 How It Works

The application is split into four distinct modules to maintain a clean separation of concerns:

- **`main.py`**  
  The entry point of the application that initializes the quiz and manages the main execution loop.

- **`quiz_brain.py`**  
  Contains the `QuizBrain` class, which handles question flow, answer checking, and score updates.

- **`question_model.py`**  
  Defines the `Question` class—a simple template for creating question objects with text and answer attributes.

- **`data.py`**  
  A centralized repository containing the trivia questions and their correct boolean answers.

---

## 🚀 Features

- **Automated Question Bank**  
  Iterates through raw data to generate a list of `Question` objects.

- **Dynamic Scoring**  
  Tracks the user's score in real time and provides immediate feedback after each answer.

- **Input Validation**  
  Normalizes user input to ensure accuracy regardless of letter casing.

- **Completion Summary**  
  Displays the final score and total number of questions when the quiz ends.

---

## 🛠 Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/Fiteh-21/The-Brainy-Quiz/
```
2. Navigate to the project directory:

```bash
cd The-Brainy-Quiz
```
3. Run the application:

```bash
python main.py
```

---

## 📊 Example Output

```text
Q.1: A slug's blood is green. (True/False)?: True
You got it right!
The correct answer was: True.
Your current score is: 1/1
```

---

Test your knowledge and see how high you can score with this OOP-powered quiz engine! 🧩🎯
