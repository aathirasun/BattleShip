import pygame
import pygame_menu
from pygame_menu import themes
import sys
pygame.init()
width=800
height=400
screen=pygame.display.set_mode((width,height))
screen.fill('blue')
pygame.display.set_caption('BATTLESHIPS')
clock=pygame.time.Clock()
menu=pygame_menu.Menu('Lobby',800,400)
username=''
def go_online():
    
    menu.add.button('Waiting for incoming connections')
    events=pygame.event.get()
    while True:
        for event in events:
            if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)

def play_against():
    opponent=menu.add.text_input('Username:',onchange='',default='opponent',maxchar=20)
    print(opponent.get_value())
    events=pygame.event.get()
    while True:
        for event in events:
            if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)

    
def refresh():
    pass

def lobby_menu():
    menu=pygame_menu.Menu('Lobby',800,400)
    username=menu.add.text_input('Username:',onchange='',default='user',maxchar=20)
    print(username.get_value())
    menu.add.button('GO ONLINE',go_online)
    menu.add.button('PLAY AGAINST AN ONLINE PLAYER',play_against)
    menu.add.button('REFRESH',refresh())
    menu.add.button('EXIT',pygame_menu.events.EXIT)
    events=pygame.event.get()
    while True:
        for event in events:
            if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)
            
            #if (menu.get_current().get_selected_widget()):
        pygame.display.update()
lobby_menu()          
