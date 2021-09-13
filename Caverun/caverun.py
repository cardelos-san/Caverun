import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

#Setting variables
#Window Width & Height
TITLESCREEN_SONG = os.path.join('Assets', 'MixedDream2.mp3')

WHITE = (255, 255, 255)
WIDTH = 1000
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caverun")
titleFont = pygame.font.SysFont("Arial, Times New Roman", 30)
mainScreenFont = pygame.font.SysFont("Arial, Times New Roman", 20)
gameTitle = titleFont.render("Caverun", True, WHITE )
mainScreenText = mainScreenFont.render("Press Space to continue", True, WHITE)
userInput = ''
game_over = False

def generate_game_dialogue(text):
    dialogueFont = pygame.font.SysFont("Arial, Times New Roman", 20)
    return dialogueFont.render(text, True, WHITE )

def center_text(text, y_offset):
    return (WIDTH/2 - text.get_rect().width/2, HEIGHT/2 - y_offset)

def text_align_top_left(text, y_offset):
    return ()

#Draws frames
def draw_title_screen():
    #screen.blit(text, pos)
    screen.blit(gameTitle, center_text(gameTitle, 100))
    screen.blit(mainScreenText, center_text(mainScreenText, 50))
    pygame.display.update()

def draw_main_game_screen():
    text = generate_game_dialogue("Type 'inspect' to gather hints about your surroundings")
    screen.blit(text, center_text(text, 250)) 
    pygame.display.update()

#Music Player
def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def main():
    clock = pygame.time.Clock()
    play_song(TITLESCREEN_SONG)

    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            print(event)
            print(clock)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_title_screen()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]: # Space
            draw_main_game_screen()

if __name__ == "__main__":
    main()  



       

        
        
 

