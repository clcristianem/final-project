import pygame
import random


#Game info
#Creates arcade look: Main is bigger than play screen
screenWidth = 1000
screenHeight = 900
playWidth = 400
playHeight = 800
blockSize = 30
topLeftX = (screenWidth = playWidth) // 2
topLeftY = screenHeight - playHeight

#Start with normal tetris blocks, then create new blocks
#New block ideas - "H" block, extended "O" block, "U" block, create more ideas later

#BLOCK SHAPES

#SHORT-I 
SI = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '.....',
      '.....']]

#U BLOCK
U = [['.....',
      '..0.0',
      '..000',
      '.....',
      '.....'],
      ['.....',
      '..00.',
      '..0..',
      '..00.',
      '.....'],
      ['.....',
      '.000.',
      '.0.0.',
      '.....',
      '.....'],
      ['.....',
      '.....',
      '.00..',
      '..0..',
      '.00..']]

      
#EXT-O BLOCK
EO = [['.....',
       '.00..',
       '.00..',
       '.00..',
       '.....'],
      ['.....',
       '.....',
       '.000.',
       '.000.',
       '.....']]

#SHORT-L BLOCK
SL = [['.....',
      '...0.',
      '..00.',
      '.....',
      '.....'],
      ['.....',
      '.....',
      '..0..',
      '..00.',
      '.....'],
      ['.....',
      '.....',
      '.00..',
      '.0...',
      '.....'],
      ['.....',
      '.00..',
      '..0..',
      '.....',
      '.....']]
      
#T BLOCK
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
      ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

#S BLOCK
S = [['...0.',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '...00',
      '.000.',
      '.....'],
     ['.0...',
      '.0...',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '..000',
      '.00..',
      '.....']]

#Z-BLOCK
Z = [['.....',
      '.0...',
      '.00..',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '..000',
      '.00..',
      '.....'],
     ['.....',
      '...0.',
      '...0.',
      '..00.',
      '..0..'],
     ['.....',
      '.....',
      '.00..',
      '..000',
      '.....']]


#SHAPE INFO
shapes = [SI, S, SL, U, T, EO, Z]
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shape.index(shape)]
            self.rotation = 0

def createGrid(locked_pos={}):
      grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
      
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j, i) in locked_pos:
                  c = locked_pos[(j, i)]
                  grid[i][j] = c
      return grid
      
def convertShapeFormat(shape):
      position = []
      format = shape.shape[shape.rotation % len(shape.shape)]
      
      for i, line in enumerate(format):
            positions[i] = (pos[0] - 2, pos[1] - 4)
      return positions
      
def validSpace(shape, grid):
      acceptedPos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0) for i in range(20)]
      acceptedPos = [j for sub in accepted_pos for j in sub]
      
      formatted = convertShapeFormat(shape)
      
      for pos in formatted:
            if pos not in acceptedPos
                  if pos[1] > -1:
                        return False
      return True
      
def checkLost(positions):
      for pos in positions:
            x, y = pos
            if y < 1:
                  return True
      return False 

def getShape():
      return Piece(6, 0, random.choice(shapes))

def drawTextMiddle(surface, text, size, color):
      font = pygame.font.SysFont("monaco", size, bold = True)
      label = font.render(text, 1, color)
      
      surface.blit(label, (topLeftX + playWidth /2 - (label.getWidth()/2), topLeftY + playHeight/2 - label.getHeight()/2))

def drawGrid(surface, grid)
      screenX = topLeftX
      screenY = topLeftY
      
      for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (screenX, screenY + i*block_size), (screenX+playWidth, screenY + i*blockSize))
            for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (screenX + j*blockSize, screenY),(screenX + j*blockSize, screenY + playHeight))

def clearRows(grid, locked):
      inc = 0
      for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if (0,0,0) not in row:
                  inc += 1
                  ind = i
                  for j in range(len(row)):
                        try:
                              del locked[(j,i)]
                        except:
                              continue
      if inc > 0: 
            for key in sorted(list(locked), key = lambda x: x[1]) [::-1=]:
                  x, y = key
                  if y < ind:
                        newKey = (x, y + inc)
                        locked[newKey] = locked.pop(key)
      return inc
      
def drawNextShape(shape, surface):
      font = pygame.font.SysFont('monaco', 30)
      label = font.render('Next Shape', 1, (255, 255, 255))
      screenX = topLeftX + playWidth + 50
      sy = topLeftY + playHeight/2 - 100
      for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        pygame.draw.rect(surface, shape.color, (screenX + j*blockSize, screenY + i*blockSize, blockSize, blockSize), 0)
      surface.blit(label, (sx + 10, sy - 30))
      
def drawWindow(surface, grid, score=0):
      surface.fill((0,0,0))
      pygame.font.init()
      font = pygame.font.SysFont('monaco', 60)
      label = font.render('Tetris', 1, (255,0,0))
      surface.blit(label, (topLeftX + playWidth / 2 - (label.getWidth() / 2), 30))
    
    #displays current score
      font = pygame.font.SysFont('monaco', 30)
      label = font.render('Score: ' + str(score), 1, (255 ,255 , 255))
                      
      screenX = topLeftX + playWidth + 50
      screenY = topLeftY + playHeight/2 - 100
                      
      surface.blit(label, (screenX + 20, screenY + 160))
      for i in range(len(grid)):
          for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (topLeftX, topLeftY, playWidth, playHeight), 6)
      
      pygame.draw.rect(surface, (255, 0, 0), (topLeftX, topLeftY, playWidth, playHeight), 6)
                      
      drawGrid(surface, grid)


def main(win):
   locked 
