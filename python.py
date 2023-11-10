import sys
import readline
from utils import get_written_str

indents = ["def", "if", "while", "for", "with"]
oldCmds = []


def isindent(text):
    for indent in indents:
        if text.startswith(indent):
            return True
    return False


def seplist(list: list[str], sep=" ") -> str:
    things = ""
    for item in list:
        if item != list[-1]:
            things += (item + sep)
        else:
            things += item
    return things


def isvalidindent(text):
    try:
        exec(text + "\n\tpass")
    except:
        return False
    else:
        return True


def pythonterm(win):
    x,y = 1,1
    oldCmds = []
    while True:
        win.addstr(x,y,">>> ")
        pythonCmd = get_written_str(x,y+4,win)
        x += 1
        if pythonCmd == "exit()":
            return 0
        try:
            pythonOut = eval(pythonCmd)
            if pythonOut != None:
                win.addstr(pythonOut)
        except:
            try:
                if isindent(pythonCmd):
                    if not isvalidindent(pythonCmd):
                        win.addstr(x,y,
f"SyntaxError: invalid syntax\n{pythonCmd} is not valid")
                        x += 1
                    else:
                        oldCmds.append(pythonCmd)
                        while True:
                            if oldCmds[-1] == "" and pythonCmd == "":
                                exec(seplist(oldCmds, "\n"))
                                break
                            win.addstr("... ")
                            pythonCmd = get_written_str(x,y+4,win)
                            oldCmds.append(pythonCmd)
                            x += 1
                else:
                    exec(pythonCmd)
            except Exception as e:
                win.addstr(x,y,f"SyntaxError: invalid syntax\n{pythonCmd} is not valid")
                x += 1