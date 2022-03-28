import pygame

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True
while running:
    
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False
        


pygame.quit()
