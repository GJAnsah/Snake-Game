import pygame
import random

pygame.init()


def food(cr=5):
    cx = random.randint(0+cr,disp_width-cr)
    cy = random.randint(0+cr,disp_height-cr)
    return ([cx,cy])



def text(msg,color):
    mesg=font.render(msg,True,color)
    mesgRect = mesg.get_rect()
    mesgRect.center = (S_startX,S_startY)
    disp.blit(mesg,mesgRect)
    

#game area
disp_height=500
disp_width=500

#start position and dimension of snake
S_startX = disp_height/2
S_startY = disp_width/2
S_height = 10
S_width = 10

#position increments
x=0
y=0

#creating game surface
disp=pygame.display.set_mode((disp_height,disp_width))
disp.fill((100,0,255))
pygame.display.set_caption("Snake Game")

#colors
white = (255,255,255)
red = (0, 0, 0)

#creating snake
SnakeColor = pygame.Color(255,255,255)
Snake= pygame.Rect(S_startX,S_startY,S_width,S_height)

#system font
font = pygame.font.SysFont('bell', 60)


#creating food
cr=5   
[cx,cy]=food(cr)


close=False
while not close:
    
    for event in pygame.event.get():
        # print(event)
        
        #close and exit if exit button is clikced.
        if event.type==pygame.QUIT: 
            close=True
        
        #moving snake
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x=-1
                y=0
            elif event.key==pygame.K_RIGHT:
                x=1
                y=0
            elif event.key==pygame.K_UP:
                x=0
                y=-1
            elif event.key==pygame.K_DOWN:
                x=0
                y=1
                
    Snake=Snake.move(x,y)
    disp.fill((100,0,255))
          
    
    #restart if snake hit boundary
    if (Snake[0]== 0 or Snake[0]== disp_width-Snake[2] 
        or Snake[1]==0 or Snake[1] == disp_height-Snake[3]):
        
        Snake= pygame.Rect(S_startX,S_startY,S_width,S_height)
        text('GAME OVER',red)

    
    pygame.draw.rect(disp,SnakeColor,Snake)
    pygame.draw.circle(disp, white, (cx,cy), cr)
   
    #check if food is eaten
    if Snake[1]<cy<Snake[1]+10 and Snake[0]<cx<Snake[0]+10 :
        print('Yummy')
        
    
    pygame.time.delay(10)  
    pygame.display.update()
    
pygame.quit()
