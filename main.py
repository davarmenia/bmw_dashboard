# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
pygame.init()


# Parameters for game window
WIN_W = 1200
WIN_H = 500
FPS = 60

file_path = os.path.dirname(os.path.realpath(__file__))
speed_image_dir = (file_path + "\\wehicle_speed.png")
speed = pygame.image.load(speed_image_dir)
speed_tablo_image = pygame.transform.scale(speed, (497.5, 443.25))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (81, 81, 81)

# Set up the drawing window
screen = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption('Dashboard')

GAME_CLOCK = pygame.time.Clock()

class InfoText():
    def __init__(self):
        self.color_rgb = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.color_ind_to_change = [1,0,0,0,0,0,0,0,0,0,0,0]
        self.color_ind_en = 0
        self.speed_values = ["0", "20", "40", "60", "80", "100", "120", "140", "160", "180", "200", "220"]
        self.speed_values_position = [[125,390], [70,335], [40,265], [40,190], [70,125], [110,70], [175,35], [250,30], [320,50], [370,100], [405,165], [415,230]]

    def draw_numbers(self):
        font = pygame.font.Font('BlackOpsOne-Regular.ttf', 24)
        for id, value in enumerate(self.speed_values):
            text_for_show = "%s" % (value)
            text = font.render(text_for_show, True, (self.color_rgb[id], self.color_rgb[id], self.color_rgb[id]))
            if self.color_ind_to_change[id] and self.color_rgb[id] < 255:
                self.color_rgb[id] += 5
                if self.color_ind_en < len(self.color_rgb) - 1:
                    if self.color_rgb[self.color_ind_en] > 40:
                        self.color_ind_en += 1
                    if self.color_ind_to_change[self.color_ind_en] == 0:
                        self.color_ind_to_change[self.color_ind_en] = 1

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
    screen.blit(speed_tablo_image, (0, 0))
    pygame.time.get_ticks()

    # Flip the display

    info_text.draw_numbers()
    GAME_CLOCK.tick(FPS)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()