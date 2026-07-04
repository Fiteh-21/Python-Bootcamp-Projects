# 🐢 Turtle Crossing Game

A Python-based **arcade game** built using the **turtle** module, where the player controls a turtle attempting to cross a busy road without being hit by oncoming traffic.

---

## 🎮 Game Mechanics

- **Player Control**  
  Move the turtle forward using the **Up Arrow** key.

- **Car Generation**  
  Cars are randomly generated on the right side of the screen and move toward the left.

- **Collision Detection**  
  If the turtle comes within **20 pixels** of a car, the game ends.

- **Leveling Up**  
  Reaching the finish line at the top of the screen resets the turtle to the starting position and increases the speed of the cars.

---

## 📁 Project Structure

The project is organized into four main components:

| File | Responsibility |
|---|---|
| `main.py` | Manages the game loop, screen updates, and collision logic |
| `player.py` | Defines the `Player` class, handling movement and start/finish logic |
| `car_manager.py` | Handles car creation, movement, and speed increments |
| `scoreboard.py` | Manages the level display and the **GAME OVER** message |

---

## ⚙️ Constants and Configuration

Game behavior can be customized by adjusting constants within the scripts:

- **Move Distance:** Turtle moves **10 paces** per keypress  
- **Starting Speed:** Cars begin with a move distance of **5**  
- **Speed Increment:** Each level increases car speed by **10**  
- **Finish Line:** Level is completed when the turtle’s `y` coordinate exceeds **280**

---

## ▶️ How to Play

1. Ensure **Python** is installed on your system.
2. Run the game:

```bash
python main.py
```
3. Press the Up Arrow key to move across the road.
4. Avoid the colorful cars and reach the finish line to level up!

---

Good luck crossing the road safely! 🚦🐢🎮
