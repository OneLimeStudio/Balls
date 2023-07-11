import pymunk 
import pygame
import random
space = pymunk.Space()

SCREEN_WIDTH,SCREEN_HEIGHT = 1900,900
display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
space = pymunk.Space()
clock = pygame.time.Clock()
FPS = 60
space.gravity = 0,-1000
x,y,radius,r,g,b = 0,0,10,0,0,0

def convert_coord(position):
    return position[0], SCREEN_HEIGHT - position[1]


class Ball():
    def __init__(self,x,y):

        self.r , self.g, self.b = r,g,b
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x,y
        self.shape = pymunk.Circle(self.body,radius)
        #self.body.velocity =(random.randint(-100,200),random.randint(-100,200))
        self.shape.density = 0.5
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    def draw(self,r,g,b):
        x,y = convert_coord(self.body.position)
        pygame.draw.circle(display,(r,g,b),(int(x),int(y)),radius)


#(10,10),(700,10)
def createSegement(startx,starty,endx,endy):
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body,(startx,starty),(endx,endy),7)
    space.add(segment_body,segment_shape)
    segment_shape.elasticity = 1
    pygame.draw.line(display,(255,255,255),(startx,int(SCREEN_HEIGHT - starty)),(endx,int(SCREEN_HEIGHT - endy)) ,7)


def game():
    balls = [Ball(random.randint(50,SCREEN_WIDTH -50),random.randint(SCREEN_HEIGHT/2.5,SCREEN_HEIGHT - 50)) for i in range(0,100)]


    running = True
    xd = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((0,0,0))
        createSegement(10,10,SCREEN_WIDTH - 10,10)
        createSegement(10,SCREEN_HEIGHT - 10,SCREEN_WIDTH - 10,SCREEN_HEIGHT - 10)
        createSegement(10,10,10,SCREEN_HEIGHT - 10)
        createSegement(SCREEN_WIDTH -10,10,SCREEN_WIDTH -10,SCREEN_HEIGHT - 10)
        [ball.draw(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for ball in balls]   
        

        print(FPS)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/ FPS)

game()
pygame.quit()