

````markdown
# Basic Keylogger in Python

## 📋 Overview

This project demonstrates a **simple keylogger** using Python and the `pynput` library. A keylogger is a tool that records every keystroke made on a keyboard, useful in ethical hacking and cybersecurity training environments.

⚠️ **This tool is for educational purposes only. Do not use it to violate privacy or security policies.**

---

## 🧠 How It Works

- It listens to all keyboard events using `pynput.keyboard.Listener`.
- Each keypress is recorded in a file called `keylog.txt`.
- Normal characters (e.g., `a`, `b`, `1`) are recorded directly.
- Special keys (e.g., `Enter`, `Shift`, `Space`) are logged in square brackets (e.g., `[enter]`).

---

## 🛠 Requirements

- Python 3.x
- `pynput` library

Install it using pip:

```bash
pip install pynput
````

---

## 🚀 Running the Keylogger

1. Open your terminal or command prompt.
2. Navigate to the folder containing `keylogger.py`.
3. Run the script:

```bash
python keylogger.py
```

4. It will start logging keys in the background to `keylog.txt` in the same directory.
5. To stop the keylogger, press `Ctrl + C` in the terminal window.

---

## 📂 Output Example

```
hello[space]world[enter]
```

---

## ⚠️ Legal Disclaimer

This script is intended for **educational** and **ethical** use only. Logging keystrokes without permission is **illegal** and against most ethical guidelines. Always get explicit permission before using this tool.


