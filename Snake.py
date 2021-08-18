import pygame
import time

pygame.init()


disp_height=500
disp_width=500

S_startX = disp_height/2
S_startY = disp_width/2
S_height = 10
S_width = 10


x=0
y=0


disp=pygame.display.set_mode((disp_height,disp_width))
disp.fill((100,0,255))
pygame.display.set_caption("Snake Game")

red = (0, 0, 0)
SnakeColor = pygame.Color(255,255,255)
Snake= pygame.Rect(S_startX,S_startY,S_width,S_height)

''''---TEXT---'''
font = pygame.font.SysFont('bell', 60)

def text(msg,color):
    mesg=font.render(msg,True,color)
    mesgRect = mesg.get_rect()
    mesgRect.center = (S_startX,S_startY)
    disp.blit(mesg,mesgRect)

close=False
while not close:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            close=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x=-10
                y=0
            elif event.key==pygame.K_RIGHT:
                x=10
                y=0
            elif event.key==pygame.K_UP:
                x=0
                y=-10
            elif event.key==pygame.K_DOWN:
                x=0
                y=10
            
            Snake=Snake.move(x,y)
            disp.fill((100,0,255))
            #restart if snake hit boundary
            if (Snake[0]== 0 or Snake[0]== disp_width-Snake[2] 
                or Snake[1]==0 or Snake[1] == disp_height-Snake[3]):
                
                Snake= pygame.Rect(S_startX,S_startY,S_width,S_height)
                text('GAME OVER',red)
        # print(event)
    
    
    
    pygame.draw.rect(disp,SnakeColor,Snake)
    
    pygame.display.update()
    
pygame.quit()