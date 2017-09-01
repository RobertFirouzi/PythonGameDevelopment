from game_level import LevelData #@UndefinedVariable

'''
This will create a simple practice level
blank border, with trees intersperced

'''

FILENAME = 'Level_test_3'
WIDTH = 20
HEIGHT = 15
BORDER = 3
TREESPACING = 5
LOWER_TILEMAP = 'lower.bmp'
UPPER_TILEMAP = 'upper.bmp'

BLANK_TILE = 0
GROUND_TILE = 1
BARRIER_TILE = 2
OVERHEAD_TILE = 1

'''
Barriers
  0
1   2
  3
represents bit position in 4 bit string
1 for barrier in that direction
EG
if a tile cannot be entered from the left =0b0010
if i tile cannot be entered from left or bottom = 0b1010  
'''
CLEAR =  0b0000 #0
TOP =    0b0001 #1
LEFT =   0b0010 #2
RIGHT =  0b0100 #4
BOTTOM = 0b1000 #8

backgrounds = []
foregrounds = []
gameEvents = []
actors = []

#Lower tiles are an array of ints, the ints are a key to the correct tile in the tilemap
def createLower():
    matrix = [ [GROUND_TILE] * WIDTH for _ in range(HEIGHT)]
        
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i < BORDER or i >= HEIGHT - BORDER or j < BORDER or j >= WIDTH-BORDER:
                matrix[i][j] = BLANK_TILE
    
    #add trees
    for i in range(HEIGHT):
        if i % TREESPACING == 0 and i > BORDER and i < HEIGHT - BORDER:
            for j in range(WIDTH):
                if j % TREESPACING == 0 and j > BORDER and j < WIDTH - BORDER:
                    if i < HEIGHT - 4:
                        matrix[i+2][j] = BARRIER_TILE 
                        matrix[i+3][j] = BARRIER_TILE
                               
    return tuple(matrix)

#Upper tiles are an array of ints, the ints are a key to the correct tile in the tilemap    
def createUpper():
    matrix = [ [BLANK_TILE] * WIDTH for _ in range(HEIGHT)]
            
    #add trees
    for i in range(HEIGHT):
        if i % TREESPACING == 0 and i > BORDER and i < HEIGHT - BORDER:
            for j in range(WIDTH):
                if j % TREESPACING == 0 and j > BORDER and j < WIDTH - BORDER:
                    if i < HEIGHT - 4:
                        matrix[i][j] = OVERHEAD_TILE 
                        matrix[i+1][j] = OVERHEAD_TILE
                               
    return tuple(matrix)

#border tiles are an array of 4bit sequences, if the bit is 1, that direction is not traversable on this tile
def createBorders(lowerTiles):
    matrix = [ [CLEAR] * WIDTH for _ in range(HEIGHT)]
        
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == 0:
                matrix[i][j] |= BOTTOM
            if i == HEIGHT-1:
                matrix[i][j] |= TOP      
            if j == 0:
                matrix[i][j] |= RIGHT          
            if j == WIDTH - 1:
                matrix[i][j] |= LEFT   
            if lowerTiles[i][j] == BARRIER_TILE:
                matrix[i][j] |= LEFT | RIGHT | TOP | BOTTOM   
                       
    return tuple(matrix)

def saveAsJson(filename = 'level'):
    pass


#this will only run if the module is run as the main module, not if imported.
if __name__ == '__main__':
    levelData = LevelData((WIDTH,HEIGHT), TILEMAP)
    levelData.lowerTiles = createLower()
    levelData.upperTiles = createUpper()
    levelData.borders = createBorders(levelData.lowerTiles)
    levelData.backgrounds = backgrounds
    levelData.foregrounds = foregrounds
    levelData.gameEvents = gameEvents
    saveAsJson(FILENAME)
    for i in range(len(levelData.lowerTiles)):
        print(levelData.lowerTiles[i])
    print('')
    for i in range(len(levelData.lowerTiles)):
        print(levelData.upperTiles[i])    
    print('')
    for i in range(len(levelData.lowerTiles)):
        print(levelData.borders[i])   
    
    
    
    
    
    
    
    
    
    
    