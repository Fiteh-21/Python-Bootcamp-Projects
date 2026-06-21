# 🃏 Python Blackjack CLI

A terminal-based implementation of the classic casino game, **Blackjack (21)**. This project uses Python to handle **card dealing**, **score calculation** (including Ace adjustments), and a **computer opponent** following automated dealer rules.

---

## 🚀 Features

- **Automated Dealer AI**  
  The computer automatically hits until it reaches a score of at least 17.

- **Dynamic Ace Scoring**  
  Aces are intelligently treated as 11 or 1 depending on whether the player would bust.

- **Blackjack Detection**  
  Automatically detects "Natural" Blackjacks (Ace + 10-value card) for instant wins.

- **ASCII Art**  
  Includes a stylized splash screen logo when starting a new game.

---

## 🎮 How to Play

1. Ensure **Python 3.x** is installed on your machine.
2. Run the script:

```bash
python blackjack.py
```
3. Follow the prompts:
  - Type y to draw another card (hit)
  - Type n to stay (pass)

4. Objective: Get as close to 21 as possible without going over.
  - If your score is higher than the computer’s, or the computer busts, you win!

---

## 🛠️ Code Structure

- **`deal_card()`**  
  Randomly selects a card from a standard deck. Cards 10, Jack, Queen, and King are all worth 10.

- **`calculate_score()`**  
  Checks for a Blackjack (score of 0) and adjusts the Ace value (11 → 1) if the total exceeds 21.

- **`compare()`**  
  Determines the winner based on final scores of both the user and the computer using conditional logic.

---

Enjoy testing your luck against the Python dealer! 🃏🎲
