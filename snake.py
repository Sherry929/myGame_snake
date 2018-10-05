# !/usr/bin/env python

# __*__ coding: utf-8 __*__


import pygame, sys, time, random

from pygame.locals import *

redColour = pygame.Color(255, 0, 0)

blackColour = pygame.Color(0, 0, 0)

whiteColour = pygame.Color(255, 255, 255)

greyColour = pygame.Color(150, 150, 150)


def gameOver(playSurface):
    gameOverFont = pygame.font.Font('arial.ttf', 72)

    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)

    gameOverRect = gameOverSurf.get_rect()

    gameOverRect.midtop = (320, 10)

    playSurface.blit(gameOverSurf, gameOverRect)

    pygame.display.flip()

    time.sleep(5)

    pygame.quit()

    sys.exit()


def main():
    pygame.init()

    playSurface = pygame.display.set_mode((640, 480))

    fpsClock = pygame.time.Clock()

    pygame.display.set_caption('Snake Liu')

    snakePosition = [100, 100]

    snakeSegments = [[100, 100], [80, 100], [60, 100]]

    raspberryPosition = [300, 300]

    raspberrySpawned = 1

    direction = 'right'

    changeDirection = direction

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:

                sys.exit()

            elif event.type == KEYDOWN:

                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'

                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'

                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'

                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'

                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 判断是否输入了反方向,与原文有改动

        if changeDirection == 'right':
            direction = changeDirection

        if changeDirection == 'left':
            direction = changeDirection

        if changeDirection == 'up':
            direction = changeDirection

        if changeDirection == 'down':
            direction = changeDirection

        # 根据方向移动蛇头的坐标

        if direction == 'right':
            snakePosition[0] += 20

        if direction == 'left':
            snakePosition[0] -= 20

        if direction == 'up':
            snakePosition[1] -= 20

        if direction == 'down':
            snakePosition[1] += 20

        # 增加蛇的长度

        snakeSegments.insert(0, list(snakePosition))

        # 判断是否吃掉了树莓

        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:

            raspberrySpawned = 0

        else:

            snakeSegments.pop()

        # 如果吃掉树莓，则重新生成树莓

        if raspberrySpawned == 0:
            x = random.randrange(1, 32)

            y = random.randrange(1, 24)

            raspberryPosition = [int(x * 20), int(y * 20)]

            raspberrySpawned = 1

        # 刷新pygame显示层

        playSurface.fill(blackColour)

        for position in snakeSegments:
            pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))

            pygame.draw.rect(playSurface, redColour, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))

        pygame.display.flip()

        # 判断是否死亡，后面几行和原文有改动

        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface)

        if snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver(playSurface)

        for snakeBody in snakeSegments[1:]:

            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface)

        fpsClock.tick(5)


if __name__ == "__main__":
    main()
