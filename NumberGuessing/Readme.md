# 🎯 Number Guessing Game

A simple, interactive **command-line game** where the player tries to guess a hidden number between 1 and 100. The game features difficulty levels and a retry loop to keep the fun going.

---

## 🚀 Features

- **Difficulty Settings**  
  Choose between `easy` (10 attempts) and `hard` (5 attempts).

- **Dynamic Feedback**  
  Informs you if your guess is "Too high" or "Too low" after every turn.

- **ASCII Art**  
  A custom-designed logo gives a classic terminal game feel.

- **Replayability**  
  Prompts the player to play again once a round ends.

---

## 🛠️ How to Run

1. **Prerequisites**  
   Ensure you have **Python 3** installed on your machine.

2. **Download**  
   Save the code as `number_guessing.py`.

3. **Execute**  
   Run the script in your terminal or command prompt:

```bash
python number_guessing.py
```

---

## 🎮 How to Play

1. When prompted, type **"yes"** to start a new game.  

2. Select your challenge:  
   - **Easy:** 10 chances to guess the number  
   - **Hard:** 5 chances to guess the number  

3. Enter a number between **1 and 100**.  

4. Follow the hints (**"Too high"** or **"Too low"**) to narrow down the target number before you run out of attempts.

---

## 📝 Code Logic Overview

- **`play_game()`**  
  The main function that initializes the game state and difficulty settings.

- **`checking_num()`**  
  A nested function that handles the game loop, user input validation, and decrements the attempts counter.

- **Global Loop**  
  A while loop allows continuous play without restarting the script manually.
