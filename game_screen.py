import pygame
from sys import exit
from gamec import game_server, game_client
#font=pygame.font.SysFont('Corbel',35)
screen=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
cood_opp=[(0,2),(3,3),(1,4),(2,1)]

grid1=[]
cood=[]
pygame.init()
pygame.display.set_caption('BATTLESHIPS')
test_surface=pygame.Surface((750,350))
def make_grid(grid):
    for row in range(5):
        grid.append([])
        for column in range(5):
            grid[row].append(0)


def g_screen():
    pygame.init()
    test_surface= pygame.Surface((750,350))
    test_surface.fill('Black')
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(test_surface,(25,25) )
        blockSize = 50 
        i=0
        for x in range(400, 650, 50):
            for y in range(50, 300, 50):
                rect = pygame.Rect(x, y, 50, 50)
                pygame.draw.rect(screen,"green", rect,2)
        for x in range(50, 300, blockSize):
            for y in range(50, 300, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                row=int((x-50)/50)
                col=int((y-50)/50)
                pygame.draw.rect(screen,"white", rect, 2)
        for i in cood:
            
            if x==0:
                x=50
            else:
                x=(i[1]*50)+50
            if y==0:
                y=50
            else:
                y=(i[0]*50)+50
            #x=i[0]*50
            #y=i[1]*50
            pygame.draw.rect(screen,'white',pygame.Rect(x,y,50,50))
            pygame.display.update()
            clock.tick(30)
        #send_cood(cood)
        atk()
        

       
    

        


         
       
def atk():
    pygame.init()
    print('attack')
    count=0
    test_surface= pygame.Surface((750,350))
    #test_surface.fill('Black')
    x=0
    y=0
    while True:
            #attack...
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    c=pos[0]
                    r=pos[1]
                    x=int((c-400)/50)
                    y=int((r-50)/50)
                    #coordinate to be sent
                    atk=y,x
                    print("click",pos)
                    print(atk)
                    if x==0:
                        x=400
                    else:
                        x=(x*50)+400
                        
                    if y==0:
                        y=50
                    else:
                        y=(y*50)+50
                    print(x,y)
                    t=x,y
                    pygame.draw.rect(screen,'green',pygame.Rect(x,y,50,50))
                    pygame.time.delay(300)
                    if check(atk,count):
                        pygame.draw.rect(screen,'red',pygame.Rect(x,y,50,50))
                        return atk
                    else:
                        print('missed!')
                        return atk
            

            pygame.display.update()
            clock.tick(30)


def check(t,count):
    
    pygame.init()
    if (count==4):
        print("GAME OVER")
    if t in cood_opp:
        print("HIT!")
        count+=1
        return True
    else:
        return False


def atk_opp(move,count):
     pygame.init()
     while True:
            #attack...
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                x=int(move[0])
                y=int(move[1])
                t=x,y
                if check(t,count):
                    count+=1
                    pygame.draw.rect(screen,'red',pygame.Rect(x,y,50,50))
                else:
                    pygame.draw.rect(screen,'green',pygame.Rect(x,y,50,50))
            pygame.display.update()
            clock.tick(30)


                
def text_ip():
    pass

def place_ships():
    pygame.init()
    MARGIN=5
    WIDTH=50
    HEIGHT=50    
    grid1 = []
    make_grid(grid1)
    grid2=[]
    count=0
    make_grid(grid2)
    img=pygame.image.load('C:\\Users\\aathi\\OneDrive\\Desktop\\Stuff\\programs\\LAN-Game-Template-main\\img\\bs_placeships.png')
    img.convert()
    rect=img.get_rect()
    rect.center=500,200
    
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                c=pos[0]
                r=pos[1]
                print("click",pos,"Grid Coordinates:",r,c)
                count+=1
                row=int((r-5)/50)
                col=int((c-5)/50)
                print(row,col)
                t=row,col
                cood.append(t)
                grid1[row][col]=1
                #game.attack(row,col)
            screen.fill('black')
            
            screen.blit(img,rect)
            if count!=4:
                for row in range(5):
                    for column in range(5):
                        color = 'WHITE'
                        if grid1[row][column] == 1:
                            color = 'GREEN'
                            
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            else:
                pygame.time.delay(300)
                return cood
                break
        pygame.display.update()
        clock.tick(30)
            
            
            #text='SHIPS HAVE BEEN PLACED!'
            #text=font.render("SHIPS HAVE BEEN PLACED",True,"Green")
            #screen.blit(text,(300,300))
                    
       
place_ships()


