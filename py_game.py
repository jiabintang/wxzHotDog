import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化窗口
pygame.display.set_caption('wxz & Hot dog war')  # 设置窗口标题

# 载入背景图
background = pygame.transform.scale(pygame.image.load('./resources/image/1.png'), (1800, 400))
game_over_img = pygame.transform.scale(pygame.image.load('./resources/image/game_over.jpg'), (600, 400))
# 载入王思聪
wsc_img = pygame.transform.scale(pygame.image.load('./resources/image/wsc.png'), (50, 50))
# 载入热狗
hot_dog_img = pygame.transform.scale(pygame.image.load('./resources/image/hot_dog.png'), (30, 30))

# 定义王思聪起始位置
wsc_x = 20
wsc_y = 200
wsc_pos = [wsc_x, wsc_y]

# 定义热狗位置
hot_dog_y = 200
hot_dog_x = 550
hot_dog_pos = [hot_dog_x, hot_dog_y]

# 定义背景图位置
bg_h = 0
bg_w = 0
bg_pos = [bg_h, bg_w]
game_over_pos = [600, 0]

# 定义跳跃
jump = False
jump_h = 10

# 定义开始 等级 结束
start = False
end = False
level = 5
score = 0

# 得分
font = pygame.font.SysFont('arial', 36, True)

while True:

    # 加载背景图
    screen.blit(background, bg_pos)
    screen.blit(font.render('%d' % score, True, [255, 0, 0]), [60, 20])
    screen.blit(hot_dog_img, (20, 16))

    # 加载王思聪
    screen.blit(wsc_img, wsc_pos)

    # 加载热狗
    screen.blit(hot_dog_img, hot_dog_pos)

    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 控制
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if start:
                    jump = True
                else:
                    start = True

            # 退出事件
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump = False

    if start:

        # 同步热狗
        hot_dog_x -= 1 * level
        hot_dog_pos = [hot_dog_x, hot_dog_y]
        if hot_dog_x <= 0:
            hot_dog_x = 600
            hot_dog_y = random.randint(5, 355)

        # 背景循环
        bg_h -= 1 * level
        bg_pos = [bg_h, bg_w]
        if bg_h <= -1200:
            bg_h = 0
            level += 1

        # 跳跃
        if jump:
            wsc_y -= 5
            wsc_pos = [wsc_x, wsc_y]
        else:
            if wsc_y < 400:
                wsc_y += 4
                wsc_pos = [wsc_x, wsc_y]

        # 结束验证
        if wsc_y > 380 or wsc_y < 0:
            game_over_pos = [0, 0]
            start = False
            end = True

        # 验证热狗和王思聪

        if hot_dog_x > wsc_x and hot_dog_x < wsc_x + 50:
            if hot_dog_y > wsc_y and hot_dog_y < wsc_y + 50:
                score += 1
                hot_dog_x = 600
                hot_dog_y = random.randint(5, 355)
                screen.blit(font.render('%d' % score, True, [255, 0, 0]), [60, 20])

    # 结束
    if end:
        screen.blit(game_over_img, game_over_pos)

    # 更新窗口
    pygame.display.update()
