import curses
from utils import *
import term

def main():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0, 0, 0, 0, 0, 0, 0, 0)

    x = add_centered_str(win, 10, 30, "Enter your username")
    win.addstr(12, x, "Enter your password")
    name = get_written_str(win, 11, x)
    password = get_dotted_str(win, 13, x)
    try:
        name_and_pass = load("names.pk")
    except:
        name_and_pass = {}
    new_password = ""
    reset(win)
    if name_and_pass.get(name) != None:
        if password == name_and_pass.get(name):
            win.addstr(10, x, "Welcome back.")
            win.getch()
            term.term(win)
        else:
            win.addstr(10, x, "Wrong password!")
            win.getch()
    else:
        win.addstr(10, x, "Welcome new user.")
        win.addstr(11, x, "Enter new password.")
        new_password = get_dotted_str(win, 12, x)
        if password != new_password:
            win.addstr(12, x, "Wrong password.")
        win.getch()
        while password != new_password:
            reset(win)
            win.addstr(9, x, "Welcome new user.")
            win.addstr(10, x, "Enter Your Password")
            password = get_dotted_str(win, 11, x)
            win.addstr(12, x, "Comfirm new password.")
            new_password = get_dotted_str(win, 13, x)
        name_and_pass[name] = password
        save(name_and_pass,"names.pk")

    curses.endwin()

if __name__ == "__main__":
    main()
