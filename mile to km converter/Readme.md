# 🔁 Mile to Kilometer Converter (Tkinter)

A simple, lightweight **GUI application** built with Python’s **Tkinter** library to convert distances from miles to kilometers.

---

## 🚀 Features

- **Real-time Conversion**  
  Instantly calculates kilometers from user input.

- **Clean GUI**  
  Minimalist interface built using the Tkinter `.grid()` layout system.

- **Precision**  
  Results are rounded to **two decimal places** for accuracy.

---

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Fiteh-21/mile-to-km-converter.git
    ```
2. Navigate to the project directory:
   ```bash
    cd mile-to-km-converter
    ```
3. Run the application:
    ```bash
    python main.py
    ```

---

## 📖 How It Works

The application uses the standard conversion factor:

$$
1 \text{ mile} \approx 1.60934 \text{ kilometers}
$$


1. The user enters a value (in miles) into the input field.  
2. Clicking the **Calculate** button triggers the `calc()` function.  
3. The function converts the value and updates the output label in real time.

---

## 📝 Technical Details

- **Language:** Python 3.x  
- **Library:** Tkinter (Python Standard Library)  
- **Layout Manager:** `.grid()`

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit a pull request to add features such as:

- Kilometer → Mile conversion  
- Dark mode UI  

Happy converting! 🚗📏
