# 🐢 Turtle Etch-A-Sketch

A simple, interactive drawing application built with Python’s **turtle** module. This project demonstrates the use of **higher-order functions** and **event listeners** to capture keyboard input and manipulate objects on the screen in real time.

---

## 🚀 How It Works

The application opens a graphics window where you control a *turtle cursor* using your keyboard.  
As the turtle moves, it leaves a trail behind—letting you create digital sketches just like an Etch-A-Sketch.

---

## 🎮 Controls

| Key | Action |
|---|---|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Turn left (counter-clockwise) |
| **D** | Turn right (clockwise) |
| **C** | Clear drawing and reset to center |

---

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Fiteh-21/TurtleSketch.git
   ```
2. Navigate to the project directory:
  ```bash
  cd TurtleSketch
  ```
3. Ensure Python is installed on your system, then run the application:
  ```bash
  python main.py
  ```

---

## 🧠 Concepts Applied

- **Event Listeners**  
  Uses `screen.listen()` and `screen.onkey()` to map physical key presses to Python functions.

- **State Management**  
  Manages the turtle’s position, heading, and drawing state (`penup` / `pendown`).

- **Coordinate Systems**  
  Navigates a 2D Cartesian plane using polar coordinates (distance and heading).
