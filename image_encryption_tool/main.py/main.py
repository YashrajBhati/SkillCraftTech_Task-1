# Import necessary libraries
from PIL import Image              # For opening and saving image files
import numpy as np                 # For fast array and numerical operations
import os                          # For file path handling (not used directly here)

# Function to load an image from a given path
def load_image(path):
    # Open the image using PIL and return the image object
    # NOTE: The path is hardcoded here, not using the 'path' parameter
    return Image.open(r"C:\Users\Yashr\OneDrive\Desktop\image_encryption_tool\main.py\input_image.png")

# Function to save a NumPy array as an image to the given path
def save_image(img_array, path):
    # Convert NumPy array to PIL image object (ensuring values are uint8 type)
    img = Image.fromarray(img_array.astype('uint8'))
    # Save the image to the specified path
    img.save(path)

# Function to encrypt an image
def encrypt_image(image, key=50, do_swap=True):
    # Convert the image to a NumPy array with uint16 type to avoid overflow during addition
    data = np.array(image, dtype=np.uint16)

    # Shift pixel values by 'key', and wrap around with modulo 256 to stay in 0-255 range
    encrypted = (data + key) % 256

    # Optionally swap pixels to further scramble the image
    if do_swap:
        encrypted = encrypted.copy()           # Make a copy to avoid modifying the original
        h, w, _ = encrypted.shape              # Get height, width, and color channels

        # Loop through pixels in 2x2 blocks
        for i in range(0, h-1, 2):
            for j in range(0, w-1, 2):
                # Swap diagonally opposite pixels in 2x2 block
                encrypted[i, j], encrypted[i+1, j+1] = encrypted[i+1, j+1], encrypted[i, j].copy()

    # Return the encrypted image array
    return encrypted

# Function to decrypt the encrypted image
def decrypt_image(encrypted_image, key=50, do_swap=True):
    # Convert image to NumPy array with uint16 to allow safe subtraction
    data = np.array(encrypted_image, dtype=np.uint16)

    # Optionally undo the pixel swaps in reverse
    if do_swap:
        data = data.copy()                    # Create a copy to avoid changing original
        h, w, _ = data.shape                  # Get image dimensions

        # Loop through the same 2x2 blocks as encryption
        for i in range(0, h-1, 2):
            for j in range(0, w-1, 2):
                # Reverse the pixel swap done during encryption
                data[i, j], data[i+1, j+1] = data[i+1, j+1], data[i, j].copy()

    # Subtract the key to reverse pixel shift, modulo 256 to wrap values correctly
    decrypted = (data - key) % 256
    # Return the decrypted image array
    return decrypted

# Main entry point of the script
if __name__ == "__main__":
    # Input image file name (used only for logical flow; actual path is hardcoded in load_image)
    input_path = "input_image.png"
    # Output file paths
    enc_path = "output/encrypted.jpg"
    dec_path = "output/decrypted.jpg"
    # Encryption key
    key = 77

    # Load the original image
    img = load_image(input_path)

    # Encrypt the image using the key
    encrypted_img = encrypt_image(img, key)
    # Save the encrypted image to disk
    save_image(encrypted_img, enc_path)

    # Decrypt the encrypted image using the same key
    decrypted_img = decrypt_image(encrypted_img, key)
    # Save the decrypted image to disk
    save_image(decrypted_img, dec_path)

    # Print confirmation message
    print("Encryption and decryption complete.")
