import pygame
pygame.init()
clock=pygame.time.Clock()
  #display_surface
gd=pygame.display.set_mode((800,600))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
light_green=(0,200,0)
blue=(0,0,255)
car_img=pygame.image.load("gallery/sprites/bird.png")
background=pygame.image.load("gallery/sprites/background.png")
grass=pygame.image.load("gallery/sprites/bird.png")

def Message(size,mess,x_pos,y_pos):
    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,white)
    gd.blit(render , (x_pos,y_pos))

Message(100,"START",150,100)
clock.tick(1)

def button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,green,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        if click==(1,0,0) and mess_b=="PLAY":
            Game_loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            pygame.quit()
            quit()


def game_intro():
    intro=False
    while intro == False:
        gd.blit(background, (0, 0))
        button(100,300,"PLAY")
        button(600,300,"QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def Game_loop():
   x=300
   y=200
   x_change=0
   game_over=False
   while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=+10
            elif event.key==pygame.K_RIGHT:
                x_change=-10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
    gd.fill(black)
    pygame.draw.rect(gd,red,[x,y,50,50])
    x=x-x_change
    clock.tick(50)
    pygame.display.update()

game_intro()
pygame.quit()
quit()