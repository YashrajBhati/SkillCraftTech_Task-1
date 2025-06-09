# Caesar Cipher - Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # keep spaces and punctuation
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # decryption is just reverse shifting

# User Input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (number): "))

# Encrypt and Decrypt
encrypted_message = encrypt(message, shift_value)
decrypted_message = decrypt(encrypted_message, shift_value)

# Output Results
print("\n🔐 Encrypted Message:", encrypted_message)
print("🔓 Decrypted Message:", decrypted_message)
