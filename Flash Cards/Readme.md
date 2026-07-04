# Flashy Card: Language Learning App

A Python-based flashcard application designed to help users learn French vocabulary using the **Spaced Repetition** concept. The app displays a French word, waits for three seconds, and then flips the card to reveal the English translation.

## 🚀 Features

- **Auto-Flipping Mechanics:** The card automatically flips from French to English after a 3-second delay.  
- **Progress Tracking:** Words you already know are removed from the deck and saved to a `words_to_learn.csv` file, ensuring you only study words you haven't mastered yet.  
- **Dynamic Data Loading:** The app prioritizes your custom "words to learn" list but defaults to the full French dictionary if no progress file is found.  
- **Interactive UI:** Built with Tkinter, featuring clean graphics and smooth transitions.  

## 🛠️ How It Works

1. **Start:** The app picks a random word from the dataset.  
2. **The Challenge:** You see the French word first. You have 3 seconds to recall the meaning.  
3. **The Reveal:** The card "flips" (changes color and language) to show the English translation.  
4. **Feedback:**  
   - Click the ✔️ (**Right**) button if you knew it. The word is removed from your deck.  
   - Click the ❌ (**Wrong**) button if you missed it. The word stays in the deck for future practice.  


## ⚙️ Requirements

- Python 3.x  
- **pandas** library: Used for data manipulation and CSV handling.  
- **Tkinter**: Usually comes pre-installed with Python (standard GUI library).  

To install the necessary dependency:

```bash
pip install pandas
```

## 🎮 How to Run

1. Ensure you have the `data/` and `images/` folders in the same directory as `main.py`.  
2. Execute the script:

```bash
python main.py
```


