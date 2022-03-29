import pygame

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Minder")

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(30)   # FPS 값이 30으로 고정 (게임 속도가 일정하게 유지)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
