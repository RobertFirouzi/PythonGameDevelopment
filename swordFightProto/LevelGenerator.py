from game_level import LevelData #@UndefinedVariable

FILENAME = 'Level_'
WIDTH = 15
HEIGHT = 15
BORDER = 2
TREESPACING = 9
TILEMAP = ''

backgrounds = []
foregrounds = []
gameEvents = []
actors = []

#Lower tiles are an array of ints, the ints are a key to the correct tile in the tilemap
def createLower():
    row = []
    zerosRow = []
    matrix = []
        
    for i in range(WIDTH):
        if i > BORDER and i < WIDTH - BORDER - 1:
            row.append(1)
        else:
            row.append(0) #create a blank border 15 wide each side
        zerosRow.append(0)
        
    for i in range(HEIGHT):
        if i > BORDER and i < HEIGHT - BORDER - 1:
            matrix.append(row)
        else:
            matrix.append(zerosRow)#create a blank border 15 wide each side
    
    #add trees
    for i in range(HEIGHT):
        if i % TREESPACING == 0 and i > BORDER and i < WIDTH - BORDER:
            for j in range(WIDTH):
                if j % TREESPACING == 0 and j > BORDER and j < HEIGHT - BORDER:
                    if j < HEIGHT - 4:
                        matrix[i+2][j] = 2 #2 will be the tree trunk 
                        matrix[i+3][j+3] = 2
                               
    return tuple(matrix)

#Upper tiles are an array of ints, the ints are a key to the correct tile in the tilemap    
def createUpper():
    row = []
    matrix = []
    for i in range(WIDTH):
        row.append(0) #upper is mostly blank      
    for i in range(HEIGHT):
            matrix.append(row)
    
    #add trees
    for i in range(HEIGHT):
        if i % TREESPACING == 0 and i > BORDER and i < WIDTH - BORDER:
            for j in range(WIDTH):
                if j % TREESPACING == 0 and j > BORDER and j < HEIGHT - BORDER:
                    if j < HEIGHT - 2:
                        matrix[i][j] = 1 #1 will be the tree leaves
                        matrix[i+1][j] = 1
    
    return tuple(matrix)

#border tiles are an array of 4bit sequences, if the bit is 1, that direction is not traversable on this tile
def createBorders():
    pass

def saveAsJson(filename = 'level'):
    pass

levelData = LevelData((WIDTH,HEIGHT), TILEMAP)
levelData.lowerTiles = createLower()
levelData.upperTiles = createUpper()
levelData.borders = createBorders()
levelData.backgrounds = backgrounds
levelData.foregrounds = foregrounds
levelData.gameEvents = gameEvents

#this will only run if the module is run as the main module, not if imported.
if __name__ == '__main__':
    saveAsJson(FILENAME)
    print(levelData.lowerTiles)
    print(levelData.upperTiles)
    
    
    
    
    
    
    
    
    
    
    