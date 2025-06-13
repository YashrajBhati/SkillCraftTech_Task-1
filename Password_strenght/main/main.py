import re  # Importing the regular expressions module for pattern matching

# Define a function to check the strength of a given password
def check_password_strength(password):
    strength = 0  # This variable will store the strength score of the password
    remarks = []  # This list will store suggestions if the password is weak

    # --- Check against various criteria ---

    # Check if password length is less than 8 characters
    length_error = len(password) < 8

    # Check if password does NOT contain any lowercase letters
    lowercase_error = re.search(r'[a-z]', password) is None

    # Check if password does NOT contain any uppercase letters
    uppercase_error = re.search(r'[A-Z]', password) is None

    # Check if password does NOT contain any digits (0-9)
    digit_error = re.search(r'\d', password) is None

    # Check if password does NOT contain any special characters
    special_char_error = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None

    # --- Scoring system based on criteria passed ---

    if not length_error:  # If length is OK
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if not lowercase_error:  # If it has at least one lowercase letter
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")

    if not uppercase_error:  # If it has at least one uppercase letter
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")

    if not digit_error:  # If it has at least one digit
        strength += 1
    else:
        remarks.append("Include at least one digit.")

    if not special_char_error:  # If it has at least one special character
        strength += 1
    else:
        remarks.append("Include at least one special character (!@#$%^&* etc.).")

    # --- Define strength levels based on total score ---
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong 🔐",
        3: "Moderate 🟡",
        2: "Weak ⚠️",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    # Return both the strength description and suggestions
    return strength_levels[strength], remarks

# --- Main Program Execution ---
if __name__ == "__main__":
    # Prompt user for input
    user_password = input("Enter a password to check its strength: ")

    # Call the function with the entered password
    strength, tips = check_password_strength(user_password)

    # Print the strength description
    print(f"\nPassword Strength: {strength}")

    # If there are any improvement suggestions, print them
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f"- {tip}")

