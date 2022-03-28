import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height-120)


# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False
        
    # 화면 전체를 까맣게 칠하기
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()

pygame.quit()
