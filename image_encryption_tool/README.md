Here's a simple and clean `README.md` for your image encryption tool that explains the purpose, how it works, how to use it, and requirements:

---

## 🖼️ Image Encryption Tool

This Python project provides a basic **image encryption and decryption tool** using **pixel manipulation** techniques like value shifting and optional pixel swapping.

---

### 🔐 Features

* Encrypt images by shifting pixel values and optionally scrambling pixel positions.
* Decrypt the image back using the same key.
* Works with common image formats like PNG or JPG.

---

### 🧠 How It Works

1. **Encryption**:

   * Shifts the pixel values by a given key (modulo 256).
   * Optionally swaps adjacent pixel pairs to increase obfuscation.

2. **Decryption**:

   * Reverses the pixel swap.
   * Shifts pixel values back using the key.

---

### 🛠️ Requirements

* Python 3.x
* [`Pillow`](https://python-pillow.org/) - For image operations
* `numpy` - For fast array manipulation

Install dependencies:

```bash
pip install pillow numpy
```

---

### 📁 File Structure

```
image_encryption_tool/
├── main.py
├── input_image.png
└── output/
    ├── encrypted.jpg
    └── decrypted.jpg
```

---

### 🚀 Usage

1. **Place your input image** (e.g. `input_image.png`) in the same directory as `main.py`.

2. **Run the script**:

```bash
python main.py
```

3. **Output**:

   * Encrypted image saved at `output/encrypted.jpg`
   * Decrypted image saved at `output/decrypted.jpg`

---

### ✏️ Customize

* Change `key` value in `main.py` to use a different encryption key.
* Toggle pixel swapping on/off with the `do_swap` flag in the `encrypt_image()` and `decrypt_image()` calls.

---

### 📌 Notes

* Ensure the `output/` folder exists before running the script.
* This is a simple encryption method and **not suitable for secure or real-world cryptographic purposes**.

---


