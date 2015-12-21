import pygame

Black = (0,0,0)
White = (255,255,255)
Blue = (204,229,255)

pygame.init()
surface = pygame.display.set_mode((640,400))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

img = pygame.image.load('flappy.png')
x = 150
y = 200
y_move = 0

def flying_bird(x, y, image):
    surface.blit(image, (x,y))

    
def gameOver():
    pygame.quit()
    quit()
    
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5

    y += y_move

    
    surface.fill(Blue)
    flying_bird(x, y, img)
    
    if y > 360 or y < 0:
        gameOver()
    
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
