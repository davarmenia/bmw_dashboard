# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Parameters for game window
WIN_W = 500
WIN_H = 500
FPS = 60

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GRAY = (81, 81, 81)

# Set up the drawing window
screen = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption('Dashboard')

GAME_CLOCK = pygame.time.Clock()

class InfoText():
    def draw_numbers(self):
        font = pygame.font.Font('AntonSC-Regular.ttf', 22)
        text_for_show = "%d" % (30)
        text = font.render(text_for_show, True, WHITE)
        textRect = text.get_rect()
        textRect.left = (100)
        textRect.top = (100)
        screen.blit(text, textRect)


info_text = InfoText()

# Run until the user asks to quit
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(BLACK)
    pygame.time.get_ticks()

    # Flip the display

    info_text.draw_numbers()
    GAME_CLOCK.tick(FPS)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()