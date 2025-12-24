
from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"

print("Keystroke Logging Demonstration (Educational)")
consent = input("Do you have consent to run this demo? (yes/no): ").strip().lower()
if consent != "yes":
    print("Consent not provided. Exiting.")
    exit()

print("Logging started. Press ESC to stop.")

def on_press(key):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            f.write(f"[{timestamp}] {key.char}\n")
        except AttributeError:
            f.write(f"[{timestamp}] {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping logging.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Logging stopped. Check keystrokes.log")
