import curses
import os
import pickle

lines = ["─","│","┌","┐","└","┘"]

def addcenteredstr(window,y:int,x:int,text:str) -> int:
    """adds a centered string to the sepicfied win at x and y. returns the centered x"""
    x -= len(text)//2
    window.addstr(y,x,text)
    return x
 
def getstr(win,x,y):
    key = " "
    currentstr = ""
    win.move(x,y)
    while not (ord(key) in (10,13)): #enter or return
        next_key = chr(win.getch())
        key = key if next_key == -1 else next_key
        if key == chr(127): #backspace
            currentstr = currentstr[:-1]
        else:
            currentstr += key
    return currentstr

def main():
    curses.initscr()
    win = curses.newwin(20,60,0,0)
    win.keypad(1)
    curses.curs_set(0)
    win.border(0, 0, 0, 0, 0, 0, 0, 0)

    centeredx = addcenteredstr(win,10,30,"enter your username")
    name = getstr(win,11,centeredx)

    curses.endwin()

if __name__ == "__main__":
   main()
