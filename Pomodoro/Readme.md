# Pomodoro Timer

A functional, desktop-based Pomodoro application built using Python and the Tkinter GUI library. This tool helps users stay productive by breaking work into 25-minute intervals, separated by short and long breaks.

## Features

- **Customizable Intervals:** Hard-coded constants for Work (25 min), Short Break (5 min), and Long Break (20 min).  
- **Visual Feedback:** The interface changes color and updates its title based on the current session (Work vs. Break).  
- **Automatic Progression:** Automatically transitions to the next session once the timer hits zero.  
- **Progress Tracking:** Displays checkmarks (✔) to visualize completed work sessions.  
- **Reset Functionality:** Allows you to clear the timer and progress at any time.  

## How It Works

The app follows the standard Pomodoro cycle:

1. **Work:** 25 minutes  
2. **Short Break:** 5 minutes  
3. **Work:** 25 minutes  
4. **Short Break:** 5 minutes  
5. **Work:** 25 minutes  
6. **Short Break:** 5 minutes  
7. **Work:** 25 minutes  
8. **Long Break:** 20 minutes (Triggered every 8th session)  

## Installation & Usage

**Prerequisites:** Ensure you have Python installed. Tkinter is usually included with standard Python installations.  

**File Setup:** Keep the `main.py` and the `tomato.png` image in the same directory.  

**Run the App:**

```bash
python main.py
```

## Controls

- **Start:** Click to begin the first work session.  
- **Reset:** Click to stop the timer and reset your progress.  

## Code Structure

- **`start_timer()`**: Manages the logic for determining which session type (Work/Break) is next based on the `reps` variable.  
- **`count_down()`**: Handles the recursive countdown mechanism using `window.after()`.  
- **`reset_timer()`**: Stops the active countdown and clears the UI.  
