Here is a clean and professional `README.md` file for your **Caesar Cipher - Encryption and Decryption** project:

---

```markdown
# 🔐 Caesar Cipher - Encryption and Decryption

This is a simple Python script that performs **encryption and decryption** using the classic **Caesar Cipher** technique. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.

---

## 📋 Features

- Encrypts any text using a user-provided shift value
- Decrypts automatically using reverse shift
- Maintains original punctuation, spaces, and case
- Easy to use with standard input/output

---

## 🧠 How It Works

- Each letter in the input message is shifted by a number (`shift`) in the alphabet.
- Non-alphabetic characters (spaces, punctuation) are left unchanged.
- Decryption is just encryption with the negative shift.

Example:
```

Input:  HELLO
Shift:  3
Encrypted: KHOOR
Decrypted: HELLO

````

---

## 🛠️ Requirements

- Python 3.x  
No additional packages are required.

---

## 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt in the folder.
3. Run the script:
   ```bash
   python caesar_cipher.py
````

4. Enter your message and a shift number when prompted.

---

## 📄 Code Overview

```python
def encrypt(text, shift):
    # Encrypts a message by shifting letters
    ...

def decrypt(text, shift):
    # Decrypts a message by reversing the shift
    ...
```

---

## 📌 Example

```
Enter your message: Hello, World!
Enter shift value (number): 5

🔐 Encrypted Message: Mjqqt, Btwqi!
🔓 Decrypted Message: Hello, World!
```
