import pygame
import os
import math

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position
        
        self.direction = LEFT  # 집게의 이동방향
        self.angle_speed = 2.5   # 집게의 각도 변경폭 (좌우 이동 속도)
        self.angle = 10  # 최초 각도 정의 (오른쪽 끝)
        

    def update(self, to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed

        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x
        self.rotate()


    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)

        offset_rotated = self.offset.rotate(self.angle)

        self.rect = self.image.get_rect(center=self.position + offset_rotated)
        pygame.draw.rect(screen, RED, self.rect, 1)
    
    def set_direction(self, direction):
        self.direction = direction

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed

    def set_position(self, position, angle):
        r = self.rect.size[0] // 2  # 반지름
        rad_angle = math.radians(angle)  # 각도
        to_x = r * math.cos(rad_angle)  # 삼각형의 밑변
        to_y = r * math.sin(rad_angle)  # 삼각형의 높이

        self.rect.center = (position[0] + to_x, position[1] + to_y)

    

def setup_gemstone():

    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7

    small_gold = Gemstone(gemstone_images[0], (200, 380), small_gold_price, small_gold_speed)
    gemstone_group.add(small_gold)
    big_gold = Gemstone(gemstone_images[1], (300, 500), big_gold_price, big_gold_speed)
    gemstone_group.add(big_gold)
    stone = Gemstone(gemstone_images[2], (300, 380), stone_price, stone_speed)
    gemstone_group.add(stone)
    diamond = Gemstone(gemstone_images[3], (900, 420), diamond_price, diamond_speed)
    gemstone_group.add(diamond)

def update_score(score):
    global curr_score
    curr_score += score

def display_score():
    txt_curr_score = game_font.render(f"Curr Score : {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (50, 20))

    txt_goal_score = game_font.render(f"Goal Score : {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 80))

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Minder")
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('arialrounded', 30)

# 점수 관련 변수
goal_score = 1500
curr_score = 0

# 게임 관련 변수
default_offset_x_claw = 40  # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0  # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수
caught_gemstone = None  # 집게를 뻗어서 잡은 보석 정보

# 속도 변수
move_speed = 12  # 발사할 때 이동 스피드 (x 좌표 기준으로 증가되는 값)
return_speed = 20

# 방향 변수
LEFT = -1  # 왼쪽 방향
STOP = 0  # 이동방향 고정 (집게를 뻗을때)
RIGHT = 1  # 오른쪽 방향


# 색깔
RED = (255, 0, 0)
BLACK = (0, 0, 0)

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()
    ]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw = Claw(claw_image, (screen_width//2, 110))

running = True

while running:
    clock.tick(30)   # FPS 값이 30으로 고정 (게임 속도가 일정하게 유지)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x = move_speed

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed

    if claw.offset.x < default_offset_x_claw:
        to_x = 0
        claw.set_init_state()

        if caught_gemstone:
            update_score(caught_gemstone.price)    # 점수 업데이트 처리
            gemstone_group.remove(caught_gemstone)
            caught_gemstone = None

    if not caught_gemstone:
        for gemstone in gemstone_group:
            #if claw.rect.colliderect(gemstone.rect):  # 직사각형 기준으로 충돌 처리
            if pygame.sprite.collide_mask(claw, gemstone):  # 실제 이미지 영역으로 충돌 처리
                caught_gemstone = gemstone   # 잡힌 보석 정보
                to_x = -gemstone.speed   # 잡힌 보석의 속도에 - 한 값을 이동속도로 설정
                break

    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)

    screen.blit(background, (0, 0))

    # 그룹 내 모든 스프라이트를 screen에 그리기
    gemstone_group.draw(screen)
    claw.update(to_x)
    claw.draw(screen)

    display_score()

    pygame.display.update()

pygame.quit()
