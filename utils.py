import os
import pickle

chars = """abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890!@#$%^&*()`~-=_+[]{}\|;:'",<.>/? \t"""
lines = ["─", "│", "┌", "┐", "└", "┘"]


def add_centered_str(window, y:int, x:int, text:str)->int:
    x -= len(text) // 2
    window.addstr(y, x, text)
    window.border(0, 0, 0, 0, 0, 0, 0, 0)
    return x


def get_written_str(win, x=0, y=0, max=30)->str:
    current_str = ""
    while True:
        key = win.getch()
        if str(key) in ('KEY_BACKSPACE', '\b', '\x7f'): # backspace
            if len(current_str) > 0:
                current_str = current_str[:-1]
                y -= 1
                win.delch(x, y)
                win.addstr(x, y, "  ")
                win.delch(x, 58)
        elif key in (10, 13):  # enter or return
            break
        else:
            char = chr(key)
            if char in chars and len(current_str) < max:
                current_str += char
                y += 1
                win.addch(x, y - 1, char)
        win.border(0, 0, 0, 0, 0, 0, 0, 0)
    return current_str


def get_dotted_str(win, x, y):
    current_str = ""
    while True:
        key = win.getch()
        if key == 127:  # backspace
            if len(current_str) > 0:
                current_str = current_str[:-1]
                y -= 1
                win.delch(x, y)
                if len(current_str) > 1:
                    win.delch(x, y - 1)
                    win.addch(x, y - 1, current_str[-1])
                win.delch(x, 58)
        elif key in (10, 13):  # enter or return
            break
        else:
            char = chr(key)
            if char in chars:
                current_str += char
                y += 1
                if len(current_str) < 30:
                    win.addch(x, y - 1, char)
                if len(current_str) != 1:
                    win.addch(x, y - 2, "*")
        win.border(0, 0, 0, 0, 0, 0, 0, 0)
    return current_str

def reset(win):
    win.clear()
    win.border(0, 0, 0, 0, 0, 0, 0, 0)

def save(word_list, filename='mypickle.pk'):
    with open(filename, 'wb') as fi:
        pickle.dump(word_list, fi)


def load(filename='mypickle.pk'):
    with open(filename, 'rb') as fi:
        return pickle.load(fi)