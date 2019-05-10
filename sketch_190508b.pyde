import random

dictionary=['jets','jams','gets','zoos','part','alps','band','call','dear','fish','kick','quit','vibe','wind','knit','yeti','xmas','come','owns','dope']
class Cell:
    def __init__(self):
        self.explored = False
        #k = random.randint(0,25)
        #self.alphabet = chr(k+65)
        
        
class Board:
    def __init__(self):
        self.numrow = 7
        self.numcol = 7
        self.end_game = 0
        # 0 if not end, -1 if u lost, 1 if u win
        self.create_board()
    def create_board(self):
        self.board = []
        for row in range(7):
            tmp = []
            for col in range(7):
                tmp.append(Cell())
            self.board.append(tmp)
        self.center = chr(random.randint(0,25)+65)
        self.board[4][4] = self.center
    def 
        
        
        








def setup():
    load_images()
    size(10*64,10*64)
    background(255)

def draw():
    background(255)
    for row in range(10):
        for col in range(10):
            
