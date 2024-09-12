import pyperclip
import keyboard


from audio import listen


def writing():
    print("Что написать?")
    text = listen()
    pyperclip.copy(text)
    keyboard.press_and_release("ctrl + v")
