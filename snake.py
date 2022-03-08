
import random
import pygame


pygame.init()
pygame.mixer.init()

white = (255, 217, 217)
blue = (0,0,255)
black = (0, 0, 0)
red = (255,0,0)
grey = (56, 56, 56)
light = (211, 211, 211)


display_width = 1200
display_hight = 600
gameWindow = pygame.display.set_mode((display_width, display_hight))

bgimg = pygame.image.load('anaconda.jpg')
bgimg = pygame.transform.scale(bgimg, (display_width,display_hight)).convert_alpha()

pygame.display.set_caption("Snake for Child")
pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(grey)
        text_screen("WELCOME TO CHILD SNAKE WORLD", red, 390,210)
        text_screen("Press the Space to start", red, 450,260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bgmusic.mp3')
                    pygame.mixer.music.play() 
                    gameloop()

        pygame.display.update()
        clock.tick(50)


def gameloop():

    exit_game = False
    game_over = False

    velocity_x = 0
    velocity_y = 0
    init_velocity = 20

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    snake_x = 50
    snake_y = 40
    snake_size = 10

    snake_list = []
    snake_length = 1


    apple_x = random.randint(5, display_width/1)
    apple_y = random.randint(5, display_hight/1)

    score = 0

    fps = 8
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Ooops!Game Over!", black, 480,230)
            text_screen("Please Enter to Continue", black, 450,280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()                
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0 

                      #this is use for cheatcode

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - apple_x)<13 and abs(snake_y - apple_y)<13:
                score +=10
                
                # print("score:", score)
                apple_x = random.randint(10, display_width)
                apple_y = random.randint(10, display_hight)
                snake_length +=5
                
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score:"+ str(score) + " Hiscore:"+ str(hiscore), light, 10,10)
            pygame.draw.rect(gameWindow,blue,[apple_x,apple_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
           

            if len(snake_list)>snake_length:
                del snake_list[0]
                
            
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('bomb.mp3')
                pygame.mixer.music.play()
            
            if snake_x<0 or snake_x>display_width or snake_y<0 or snake_y>display_hight:

                game_over = True
                pygame.mixer.music.load('bomb.mp3')
                pygame.mixer.music.play()
                
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
            
    pygame.quit()
    quit()

welcome()