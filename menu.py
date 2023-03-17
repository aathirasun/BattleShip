import pygame
from sys import exit
from lobby import *

import pygame_menu

#from pg_lby import lobby_menu
#from src.game_screen import g_screen
pygame.init()
width=800
height=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('BATTLESHIPS')
clock=pygame.time.Clock()
test_surface= pygame.Surface((750,350))
test_surface.fill('Black')
font=pygame.font.SysFont('Corbel',35)
title=pygame.image.load("C:\\Users\\aathi\\OneDrive\\Desktop\\Stuff\\programs\\LAN-Game-Template-main\\img\\bs_title.png")
title_click=pygame.image.load("C:\\Users\\aathi\\OneDrive\\Desktop\\Stuff\\programs\\LAN-Game-Template-main\\img\\bs_title_1.png")
title_click_ON=pygame.image.load('C:\\Users\\aathi\\OneDrive\\Desktop\\Stuff\\programs\\LAN-Game-Template-main\\img\\bs_title_1ON.png')
global username

def collide_button(button,text,a,b):
    a,b=pygame.mouse.get_pos()
    if (button.x <= a <= button.x+100) and (button.y <= b <= button.y+100):
        pygame.draw.rect(screen,'White',button)
    else:
        pygame.draw.rect(screen,'blue',button)
    screen.blit(text,(button.x +5 , button.y +5))


def lobby():
    pygame.init()
    screen.fill('black')
    button_1=pygame.Rect(300,195,100,50)
    b_text_1=font.render("GO ONLINE",True,"Green")
    button_2=pygame.Rect(300,255,100,50)
    b_text_2=font.render("PLAY AGAINST AN ONLINE PLAYER",True,"Green")
    button_3=pygame.Rect(300,310,100,50)
    b_text_3=font.render("REFRESH",True,"Green")
    button_4=pygame.Rect(300,360,100,50)
    b_text_4=font.render("EXIT",True,"Green")  
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):
                    go_online()
                elif button_2.collidepoint(event.pos):
                    play_against()
                elif button_3.collidepoint(event.pos):
                    refresh()
                elif button_4.collidepoint(event.pos):
                    pygame.quit()
            a,b=pygame.mouse.get_pos()
            collide_button(button_1,b_text_1,a,b)
            collide_button(button_2,b_text_2,a,b)
            collide_button(button_3,b_text_3,a,b)
            collide_button(button_4,b_text_4,a,b)
        pygame.display.update()
        clock.tick(60)
            

def enter_username():
    screen.blit(test_surface,(25,15))
    screen.fill('Black')
    user_ip=''
    text_box=pygame.Rect(350,300,100,50)
    active=False
    colour=pygame.Color('purple')
    button=pygame.Rect(550,300,150,50)
    text_button=font.render("next",True,"Green")
    screen.blit(title,(200,50))
    user=input('enter username')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                if event.type==pygame.KEYDOWN:
                    if active:
                        if event.key==pygame.K_RETURN:
                            print(user_ip)
                        elif event.key==pygame.K_BACKSPACE:
                            user_ip=user_ip[:-1]
                        else:
                            user_ip+=event.unicode
            if active:
                colour=pygame.Color('red')
            else:
                colour=pygame.Color('purple')

            pygame.draw.rect(screen,colour,text_box,4)

            surf=font.render(user_ip,True,'black')
            test_surface.blit(surf,(text_box.x+5,text_box.y+5))
            text_box.w=max(100,surf.get_width()+10)

            #next button
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    lobby()
            a,b=pygame.mouse.get_pos()
            if (button.x <= a <= button.x+100) and (button.y <= b <= button.y+100):
                pygame.draw.rect(screen,'White',button)
            else:
                pygame.draw.rect(screen,'Black',button)
            screen.blit(text_button,(button.x +5 , button.y +5))
        pygame.display.update()
        clock.tick(60)

def go_online():
    pygame.init()
    screen.blit(test_surface,(25,15))
    screen.fill('Black')
    img1=pygame.image.load("C:\\Users\\aathi\\OneDrive\\Desktop\\Stuff\\programs\\LAN-Game-Template-main\\img\\bs_waiting.png")
    rect=img1.get_rect()
    rect.center=350,200
    screen.blit(img1,rect)
    button=pygame.Rect(200,300,350,50)
    b_text=font.render("Back",True,"Green")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    lobby()
            a,b=pygame.mouse.get_pos()
            collide_button(button,b_text,a,b)
        pygame.display.update()
        clock.tick(60)

def play_against():
    
    users=online_users()
    text=''
    for user in users:
      text+=user+' '+users[user]['status']
      text+='\n'
    if not users:
      print('None Online.')
    pygame.init()
    screen.blit(test_surface,(25,15))
    screen.fill('Black')
    button=pygame.Rect(200,300,350,50)
    b_text=font.render("Back",True,"Green")
    text1=font.render("ONLINE USERS",True,"Green")
    text2=font.render("a b c",True,"Green")
    screen.blit(text1,(300,50))
    screen.blit(text2,(300,100))
    opp=input('enter opponent username')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    lobby()
            a,b=pygame.mouse.get_pos()
            collide_button(button,b_text,a,b)
            menu=pygame_menu.Menu('Enter opponent username',800,400)
            username=menu.add.text_input('Username:',onchange='',default='user',maxchar=20)
            print(username.get_value())
        pygame.display.update()
        clock.tick(60)

def refresh():
    pass  
                

    
    
def home_screen():
    pygame.init()
    text_1=font.render("BATTLE SHIPS",True,"Green")
    text_button=font.render("click to begin",True,"Green") 
    rect=title_click.get_rect()
    rect.center=275,325
    
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        
        #click to enter username
        test_surface.blit(title,(200,50))
        #test_surface.blit(title_click,(200,300))
        

        screen.blit(test_surface,(25,25))
        button=pygame.Rect(200,300,350,50)
        test_surface.blit(title_click,rect)
        
        #screen.blit(text_1, (325,50))
        if event.type==pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                enter_username()
        a,b=pygame.mouse.get_pos()
        if (button.x <= a <= button.x+100) and (button.y <= b <= button.y+100):
            pygame.draw.rect(screen,'White',button)
        else:
            pygame.draw.rect(screen,'blue',button)
        #rect.blit(text_button,(rectr.x +5 , button.y +5))
        
        #test_surface.blit(title_click,(200,300))

        #text input   
        pygame.display.update()
        clock.tick(60)
#lobby()
home_screen()
