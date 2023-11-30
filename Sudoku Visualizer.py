#Some of the visualizer code was taken from https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/

# import pygame library
import pygame
from SolveSudoku import solve
 
# initialise the pygame font
pygame.font.init()
 
# Total window
screen = pygame.display.set_mode((500, 500))
 
# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
 
x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid =[
        [0, 0, 9, 0, 5, 3, 0, 4, 1],
        [0, 3, 0, 0, 2, 0, 0, 0, 0],
        [1, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 4, 0, 9],
        [0, 9, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 0, 0, 7, 0, 0, 6, 0],
        [3, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 4, 0, 0, 7],
        [0, 0, 4, 0, 0, 0, 0, 0, 2]
    ]

grid = solve(grid)
 
# Load test fonts for future use
font1 = pygame.font.SysFont("Calibri", 20)
font2 = pygame.font.SysFont("Calibri", 20)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 
# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
 
# Function to draw required lines for making Sudoku grid        
def draw():
    # Draw the lines
        
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and verticallyto form grid          
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
 
# Fill value entered in cell     
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
 
# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 
# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True
 
# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:
     
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        # Get the mouse position to insert number   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1()
    draw() 
    if flag1 == 1:
        draw_box()
 
    # Update window
    pygame.display.update() 

    
 
# Quit pygame window   
pygame.quit()    