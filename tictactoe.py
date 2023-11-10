from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

def writetiles(window, tiles, selected):
    window.border(0, 0, 0, 0, 0, 0, 0, 0)
    window.addstr(7,22,"  |   |  ")
    window.addstr(8,21,"---+---+---")
    window.addstr(9,22,"  |   |  ")
    window.addstr(10,21,"---+---+---")
    window.addstr(11,22,"  |   |  ")

    for x, row in enumerate(tiles):
        for y, char in enumerate(tiles[x]):
            if char == 0:
                char = "-"
            if char == 1:
                char = "X"
            if char == 2:
                char = "O"
            if [x, y] == selected:
                window.addstr(x * 2 + 7, y * 4 + 21, f"[{char}]")
            else:
                window.addstr(x * 2 + 7, y * 4 + 22, f"{char}")

def wincheck(board, player):
    for row in board:
        if row == [player,player,player]:
            return player
    for iter, tile in enumerate(board[0]):
        if tile == player and board[1][iter] == player and board[2][iter] == player:
            return player
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return player
    return 0

def drawchecker(board):
    isdraw = True
    for row in board:
        for tile in row:
            if tile == 0:
                isdraw = False
    return isdraw
    
def tic_tac_toe(window):    
    tiles = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    pos = [0, 0]
    
    writetiles(window, tiles, pos)
    
    key = 0
    turn = 1
    playerwin = 0
    
    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key
    
        if key == KEY_DOWN or key == ord("s"):
            pos[0] += 1
            window.erase()
        if key == KEY_UP or key == ord("w"):
            pos[0] -= 1
            window.erase()
        if key == KEY_LEFT or key == ord("a"):
            pos[1] -= 1
            window.erase()
        if key == KEY_RIGHT or key == ord("d"):
            pos[1] += 1
            window.erase()
        if key == ord("\n") and tiles[pos[0]][pos[1]] == 0:
            tiles[pos[0]][pos[1]] = turn
            if wincheck(tiles,turn) == turn:
                playerwin = turn
                window.erase()
                window.border(0, 0, 0, 0, 0, 0, 0, 0)
                break
            elif drawchecker(tiles):
                playerwin = 0
                window.erase()
                window.border(0, 0, 0, 0, 0, 0, 0, 0)
                break
            turn = 2 if turn == 1 else 1
    
        if pos[0] < 0:
            pos[0] = 0
        elif pos[0] > 2:
            pos[0] = 2
        if pos[1] < 0:
            pos[1] = 0
    
        elif pos[1] > 2:
            pos[1] = 2
    
    
        writetiles(window, tiles, pos)
    
    if playerwin != 0:
        wintext = f"player {playerwin} won"
        window.addstr(10,25-len(wintext)//2,wintext)
        window.getch()
    else:
        losetext = f'tie game'
        window.addstr(10,25-len(losetext)//2,losetext)
        window.getch()
    