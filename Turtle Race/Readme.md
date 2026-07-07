# 🐢 Turtle Derby

A fun, interactive Python game where players place bets on a multi-colored turtle race. Built using Python’s built-in **turtle graphics** library.

---

## 🎮 How It Works

1. **Place Your Bet**  
   When the game starts, a popup asks you to choose a color from the racing lineup.

2. **The Race**  
   Six turtles—**Red, Orange, Yellow, Green, Blue, and Purple**—line up at the starting gate.

3. **Randomized Movement**  
   Each turtle moves forward by a random distance between **0 and 10 pixels** on every turn.

4. **The Winner**  
   The first turtle to cross the finish line (x-coordinate **230**) is declared the winner.

5. **Result**  
   The console announces whether your bet was correct or if another color won.

---

## 🛠️ Features

- **Dynamic Turtle Generation**  
  Uses a loop to create multiple `Turtle` objects with unique colors and starting positions.

- **Coordinate Mapping**  
  Precisely positions turtles using a coordinate system to ensure a fair start.

- **Interactive UI**  
  Utilizes `screen.textinput()` to collect the player’s bet.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x**
- The **turtle** module (included with Python’s standard library)

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/Fiteh-21/python-turtle-race.git
    ```
2. Navigate to the project directory:
  ```bash
  cd turtle-race
  ```
3. Run the script:
  ```bash
  python main.py
  ```

---

## 📜 Code Structure

- **Setup**  
  Initializes the screen dimensions (**500 × 400**) and prepares the race track.

- **Initialization**  
  Creates a list of turtle objects and assigns their colors and starting positions.

- **Game Loop**  
  A `while` loop runs until a turtle’s `xcor()` exceeds the finish line threshold.
