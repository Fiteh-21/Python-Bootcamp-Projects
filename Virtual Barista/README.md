# ☕ OOP Coffee Machine Simulator

A modular, object-oriented Python application that simulates a professional coffee vending machine. The system manages resource inventory, processes multi-coin payments, and handles a dynamic menu of beverages.

---

## ✨ Features

- **Resource Management**  
  Tracks levels of water, milk, and coffee beans, ensuring orders are only processed if ingredients are sufficient.

- **Payment Processing**  
  Handles transactions using quarters, dimes, nickels, and pennies, including accurate change calculation.

- **Modular Architecture**  
  Built using four distinct classes (`Menu`, `MenuItem`, `CoffeeMaker`, and `MoneyMachine`) to demonstrate clean OOP principles.

- **Administrative Reporting**  
  Includes a `report` command to check current ingredient levels and total profit.

---

## 🧠 System Architecture

The project is structured into logical modules to separate concerns clearly:

| Module             | Responsibility                                                  |
| ------------------ | --------------------------------------------------------------- |
| `main.py`          | Controls the program flow and user interaction loop             |
| `coffee_maker.py`  | Manages resources (water, milk, coffee) and brewing logic       |
| `money_machine.py` | Handles coin input, payment validation, and profit tracking     |
| `menu.py`          | Defines `MenuItem` objects and manages the available drink menu |

---

## 🚀 Installation & Usage

### Prerequisites

- Python 3.x

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/oop-coffee-machine.git
   ```
2. Navigate to the project directory:
   ```bash
    cd oop-coffee-machine
   ```

### ▶️ Running the Simulator

Start the coffee machine simulator by running:
`bash
    python main.py
    `

## ⌨️ Commands

- Drink names:
  Type espresso, latte, or cappuccino to place an order.
- report:
  Displays current resource levels and total profit.
- off:
  Shuts down the coffee machine.

---

## ☕ Menu Details

The machine currently supports the following beverages:

### Espresso

- **Price:** $1.50
- **Ingredients:**
  - 50ml Water
  - 18g Coffee

---

### Latte

- **Price:** $2.50
- **Ingredients:**
  - 200ml Water
  - 150ml Milk
  - 24g Coffee

---

### Cappuccino

- **Price:** $3.00
- **Ingredients:**
  - 250ml Water
  - 50ml Milk
  - 24g Coffee

---

Enjoy brewing with your OOP-powered coffee machine! ☕🚀
