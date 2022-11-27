import pygame
import random


#Game info
#Creates arcade look: Main screen is bigger than play screen
screen_width = 1000
screen_height = 900
play_width = 400
play_height = 800

#Start with normal tetris blocks, then create new blocks
#New block ideas - "H" block, extended "O" block, "U" block, create more ideas later

#BLOCK SHAPES

#SHORT-I 
SI = [['.....',
      '..0..',
      '..0..',
      '.....',
      '.....'],
      ['.....',
      '.....',
      '..00.',
      '.....',
      '.....']]

#J BLOCK
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '.00..',
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

      
#L BLOCK
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
      ['.....',
      '......',
      '.000.',
      '.0...',
      '.....'],
      ['.....',
      '.00..',
      '..0..',
      '..0..',
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

#LOWER-T BLOCK
LT = [['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....']]


#SHAPE INFO
shapes = [LT, I, SL, U, T, L]
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shape.index(shape)]
            self.rotation = 0

def create_grid(locked_pos={}):
      grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
      
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j, i) in locked_pos:
                  c = locked_pos[(j, i)]
                  grid[i][j] = c
      return grid
      
def convert_shape_format(shape):
      position = []
      format = shape.shape[shape.rotation % len(shape.shape)]
      
      for i, line in enumerate(format):
            positions[i] = (pos[0] - 2, pos[1] - 4)
      return positions
      
def valid_space(shape, grid):
      accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0) for i in range(20)]
      accepted_pos = [j for sub in accepted_pos for j in sub]
      
      formatted = convert_shape_format(shape)
      
      for pos in formatted:
            if pos not in accepted_pos
                  if pos[1] > -1:
                        return False
      return True
      
def check_lost(positions):
      for pos in positions:
            x, y = pos
            if y < 1:
                  return True
      return False 

def get_shape():
      return Piece(5, 0, random.choice(shapes))

def draw_text_middle(surface, text, size, color):
      font = pygame.font.SysFont("monaco", size, bold = True)
      label = font.render(text, 1, color)
      
      surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))

def draw_grid(surface, grid)
      sx = top_left_x
      sy = top_left_y
      
      for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
            for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))

def clear_rows(grid, locked):
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
      
def draw_next_shape(shape, surface):
      font = pygame.font.SysFont('monaco', 30)
      label = font.render('Next Shape', 1, (255, 255, 255))
      sx = top_left_x + play_width + 50
      sy = top_left_y + play_height/2 - 100
      for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
      surface.blit(label, (sx + 10, sy - 30))
      
def draw_window(surface, grid, score=0):
      surface.fill((0,0,0))
      pygame.font.init()
      font = pygame.font.SysFont('monaco', 60)
      label = font.render('Tetris', 1, (255,0,0))
      surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))


