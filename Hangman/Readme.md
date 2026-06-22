# 🎯 Hangman Python Game

A complete, terminal-based **Hangman game** developed in Python. The game challenges players to guess a randomly selected word from a diverse dictionary by entering letters one at a time—before the hangman visual is fully completed.

---

## ✨ Features

- **Extensive Vocabulary**  
  Includes a list of over **200 challenging words**, ranging from *“abyss”* to *“zigzagging”*.

- **Dynamic Visuals**  
  Features **7 stages of ASCII art** that visually represent the hangman’s progress as lives are lost.

- **Interactive Gameplay**
  - Tracks and displays correctly guessed letters in real time  
  - Warns the player if a letter has already been guessed  
  - Reduces lives and updates the ASCII art for every incorrect guess  

- **Win / Loss Logic**  
  - Automatically detects when the player completes the word  
  - Ends the game after **6 incorrect guesses**

---

## 🎮 How to Play

1. **Start the game**  
   Run the script in your terminal.

2. **The Goal**  
   Guess the hidden word displayed as underscores (`_ _ _ _`).

3. **Input**  
   Type **one letter** at a time and press **Enter**.

4. **Feedback**
   - ✅ Correct letters appear in the correct position(s)  
   - ❌ Incorrect guesses reduce a life and advance the hangman drawing  

5. **Game End**
   - 🎉 **Win** by revealing all letters  
   - 💀 **Lose** if the hangman is fully drawn (6 incorrect guesses)

---

## 🧠 Technical Implementation

- **Randomization**  
  Uses `random.choice()` to select a unique word each session.

- **List Manipulation**  
  Lists are used to manage:
  - The word display
  - Previously guessed letters
  - The current state of the game board

- **Control Flow**  
  A `while` loop runs until the `end_of_game` flag is triggered by a win or loss condition.

---

## 🚀 Installation & Running the Game

1. Clone this repository.
2. Ensure **Python** is installed on your system.
3. Run the game with:

```bash
python project7.py
```
---

## ⚠️ Note

The current version includes a **cheat print statement** for testing purposes:

```python
print(f"Pssst, the solution is {chosen_word}.")
```
Remove or comment out this line for a genuine challenge.

---

Have fun—and good luck saving the stick figure! 😄🎯
