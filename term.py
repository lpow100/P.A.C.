from utils import *
from tictactoe import tic_tac_toe

def term(win):
    reset(win)
    x,y = 1,1
    while True:
        win.addstr(x,y,"P.A.T.>")
        cmd = get_written_str(win,x,y+8,53)
        x += 1
        if cmd == "exit()":
            break
        elif cmd == "exit":
            win.addstr(x,y,"Use exit() to exit.")
            x += 1
        elif cmd.startswith("echo"):
            echo_text = str(cmd)[5:]
            win.addstr(x,y,echo_text)
            x += 1
        elif cmd == "tic tac toe":
            reset(win)
            tic_tac_toe(win)
            reset(win)
            x = 1