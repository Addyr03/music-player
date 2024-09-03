import pygame
from pygame import mixer
import random 
pygame.init()
mixer.init()

#hardcodes 
player = True 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
dark_blue = (0,0,128)
light_blue =(0,0,100)
yellow = (255,255,0)
display_width = 800
display_height = 600
font_size = 25

#screen text 

font = pygame.font.SysFont(None, font_size)

def instructions (msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [font_size,display_height-font_size])

#display

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("music player")
gameDisplay.fill(black)
instructions("q = exit , P = pause , r = play again , s = skip g = start song again:)", white )
pygame.display.update()

#song list 
song_list = ['1.mp3' , '2.mp3' , '3.mp3' , '4.mp3' , '5.mp3']
song = random.choice(song_list)



def main ():
    mixer.music.load(song)
    mixer.music.set_volume(0.5)
    mixer.music.play()

    player = True 
    while player ==  True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                player = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player = False
                if event.key == pygame.K_p:
                    mixer.music.pause()
                if event.key == pygame.K_r:
                    mixer.music.unpause()
                if event.key == pygame.K_s:
                    mixer.music.load(random.choice(song_list))
                    mixer.music.play()
                if event.key == pygame.K_g:
                    mixer.music.load(song)
                    mixer.music.play()   
    pygame.quit()
    
main ()

