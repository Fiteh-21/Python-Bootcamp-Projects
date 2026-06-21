# BlindBid 🏆

A sleek, command-line interface (CLI) application designed to facilitate a "blind" or "silent" auction where bidders can enter their offers privately.

---

## 🛠️ How It Works
The program operates on a simple loop that collects user data and stores it in a dictionary. Once all participants have placed their bids, the script calculates the highest offer and announces the winner.

1. **Input**: Each user enters their name and their bid amount.
2. **Privacy**: The program asks if there are other bidders, allowing the screen to be cleared or passed between users.
3. **Logic**: It iterates through the collected bids to identify the maximum value.
4. **Result**: The winner's name and the winning amount are printed to the console.

## 🚀 Features
* **ASCII Art**: Includes a classic trophy logo for a better user experience.
* **Dynamic Bidding**: Handles an unlimited number of participants using Python dictionaries.
* **Input Validation**: Uses clear prompts to guide users through the bidding process.

## 💻 Usage
To run the auction, ensure you have Python installed and execute the script:

```bash
python secret_auction.py
```

### Example Interaction:
```text
What is your name?: Alice
What's your bid?: $150
Are there any other bidders? Type 'yes' or 'no'.
yes
...
The winner is Alice with a bid of $150
```
