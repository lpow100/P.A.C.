import curses
import os
import pickle

chars = """abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890!@#$%^&*()`~-=_+[]{}\|;:'",<.>/? \t"""
lines = ["─", "│", "┌", "┐", "└", "┘"]


def add_centered_str(window, y, x, text):
    x -= len(text) // 2
    window.addstr(y, x, text)
    window.border(0, 0, 0, 0, 0, 0, 0, 0)
    return x


def get_written_str(win, x, y):
    current_str = ""
    while True:
        key = win.getch()
        if key == 127:  # backspace
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
            if char in chars:
                current_str += char
                y += 1
                if len(current_str) < 30:
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
                win.addch(x, y - 2, "*")
        win.border(0, 0, 0, 0, 0, 0, 0, 0)
    return current_str


def main():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0, 0, 0, 0, 0, 0, 0, 0)

    centered_x = add_centered_str(win, 10, 30, "Enter your username")
    win.addstr(12, centered_x, "Enter your password")
    name = get_written_str(win, 11, centered_x)
    password = get_dotted_str(win, 13, centered_x)
    #try:

    curses.endwin()

def save(word_list,filename = 'mypickle.pk'):
    with open(filename, 'wb') as fi:
        pickle.dump(word_list, fi)

def load(filename = 'mypickle.pk'):
    with open(filename, 'rb') as fi:
        return pickle.load(fi)

if __name__ == "__main__":
    main()
