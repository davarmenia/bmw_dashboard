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
    def __init__(self):
        self.color_rgb = [1,1,1,1,1,1,1,1]
        self.color_ind_to_change = -1
        self.speed_values = ["30, 60, 90, 120, 150, 180, 210, 240"]
        self.speed_values_position = [[100,100], [100,120], [100,140], [100,160], [100,180], [100,200], [100,220], [100,240]]

    def draw_numbers(self):
        font = pygame.font.Font('AntonSC-Regular.ttf', 22)
        for id, value in enumerate(self.speed_values):
            text_for_show = "%s" % (value)
            text = font.render(text_for_show, True, (self.color_rgb[id], self.color_rgb[id], self.color_rgb[id]))
            if id > self.color_ind_to_change:
                if self.color_rgb[id] < 200:
                    self.color_rgb[id] += 3
                    if self.color_rgb[self.color_ind_to_change] > 100:
                        self.color_ind_to_change += 1
            textRect = text.get_rect()
            textRect.left = (self.speed_values_position[id][0])
            textRect.top = (self.speed_values_position[id][1])
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