# Caesar Cipher - Encryption and Decryption

# Function to encrypt the message
def encrypt(text, shift):
    result = ""  # Start with an empty string to build the encrypted message
    for char in text:  # Go through each character in the message
        if char.isalpha():  # Check if the character is a letter
            # Set base depending on whether the letter is uppercase or lowercase
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and add it to the result
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep characters like space, punctuation, or numbers unchanged
    return result  # Return the final encrypted message

# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encrypting with a negative shift

# === User Input Section ===
message = input("Enter your message: ")  # Ask the user to type their message
shift_value = int(input("Enter shift value (number): "))  # Ask for the shift number

# === Perform Encryption and Decryption ===
encrypted_message = encrypt(message, shift_value)  # Encrypt the message
decrypted_message = decrypt(encrypted_message, shift_value)  # Decrypt to get the original message back

# === Output Results ===
print("\n🔐 Encrypted Message:", encrypted_message)  # Show encrypted message
print("🔓 Decrypted Message:", decrypted_message)  # Show decrypted (original) message

# === Example === 
Enter your message: hello world
Enter shift value (number): 3

🔐 Encrypted Message: khoor zruog
🔓 Decrypted Message: hello world
