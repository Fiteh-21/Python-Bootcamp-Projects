# PyPass Vault

A secure, desktop-based password manager built with Python and Tkinter. This application allows users to generate strong, randomized passwords, store them securely in a local JSON database, and search for existing credentials via a clean graphical user interface.

## 🚀 Features

- **Secure Storage:** Saves website credentials and emails into a local `data.json` file using structured JSON formatting.  
- **Password Generator:** Creates complex passwords using a mix of letters, numbers, and symbols with built-in randomization.  
- **Smart Search:** Includes a search function to instantly retrieve passwords for specific websites.  
- **Clipboard Integration:** Automatically copies generated passwords to your clipboard for immediate use.  
- **Error Handling:** Robust validation to prevent empty fields and manage missing data files gracefully.  

## 🛠️ Requirements

- Python 3.x  
- Tkinter (usually included with Python)  
- Pyperclip (used for clipboard functionality)  

To install dependencies:

```bash
pip install pyperclip
```

---

## 🖥️ How to Use

- **Add Data:** Enter a website and email. Click **Generate Password** or type your own, then click **Add**.  
- **Search:** Type the name of a website in the "Website" field and click **Search** to retrieve your credentials in a pop-up window.  
- **Security:** Your data is stored locally in `data.json` within the project folder.  

## 📂 Project Structure

- **`main.py`**: The core application logic, including UI setup and data management.  
- **`logo.png`**: Branding used for the application canvas.  
- **`data.json`**: The local database (generated automatically upon first save).  


