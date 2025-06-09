from PIL import Image
import numpy as np
import os

def load_image(path):
    return Image.open(r"C:\Users\Yashr\OneDrive\Desktop\image_encryption_tool\main.py\input_image.png")

def save_image(img_array, path):
    img = Image.fromarray(img_array.astype('uint8'))
    img.save(path)

def encrypt_image(image, key=50, do_swap=True):
    data = np.array(image, dtype=np.uint16)  # prevent overflow

    # Apply simple pixel value shift
    encrypted = (data + key) % 256

    # Optional: Swap pixels for scrambling
    if do_swap:
        encrypted = encrypted.copy()
        h, w, _ = encrypted.shape
        for i in range(0, h-1, 2):
            for j in range(0, w-1, 2):
                encrypted[i, j], encrypted[i+1, j+1] = encrypted[i+1, j+1], encrypted[i, j].copy()
    return encrypted

def decrypt_image(encrypted_image, key=50, do_swap=True):
    data = np.array(encrypted_image, dtype=np.uint16)

    # Optional: Undo pixel swap
    if do_swap:
        data = data.copy()
        h, w, _ = data.shape
        for i in range(0, h-1, 2):
            for j in range(0, w-1, 2):
                data[i, j], data[i+1, j+1] = data[i+1, j+1], data[i, j].copy()

    # Reverse the shift
    decrypted = (data - key) % 256
    return decrypted

if __name__ == "__main__":
    input_path = "input_image.png"
    enc_path = "output/encrypted.jpg"
    dec_path = "output/decrypted.jpg"
    key = 77

    # Load image
    img = load_image(input_path)

    # Encrypt and save
    encrypted_img = encrypt_image(img, key)
    save_image(encrypted_img, enc_path)

    # Decrypt and save
    decrypted_img = decrypt_image(encrypted_img, key)
    save_image(decrypted_img, dec_path)

    print("Encryption and decryption complete.")

