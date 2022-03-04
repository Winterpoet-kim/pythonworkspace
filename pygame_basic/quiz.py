import pygame
from random import *

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Dalbit Game")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/admin/Desktop/Code/pythonworkspace/pygame_basic/background.png")

character = pygame.image.load("C:/Users/admin/Desktop/Code/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.5
enemy_speed = 8


enemy = pygame.image.load("C:/Users/admin/Desktop/Code/pythonworkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randrange(0, screen_width-enemy_width)
enemy_y_pos = 0


# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (None(디폴트 폰트), 크기)


# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시간 tick 을 받음

running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            

    character_x_pos += to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if 0 <=  enemy_y_pos < (screen_height):
        enemy_y_pos += enemy_speed
    else:
        enemy_x_pos = randrange(0, screen_width-enemy_width)
        enemy_y_pos = 0

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False


    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 # 경과 시간을 1000으로 나누어서 초 단위로 표시
    
    # render(출력할 글자, True(안티일라이징), 흰색)
    timer = game_font.render(str(int(elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    
    pygame.display.update()

pygame.quit()
