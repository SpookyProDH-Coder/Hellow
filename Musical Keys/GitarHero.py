import pygame
import sys

name = input("")

width = 640
height = 480

SongSpeed = [3,3]

class note(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("data/ball.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = width / 2
        self.rect.centery = height / 2

        self.speed = SongSpeed

    def update(self):
        self.rect.move_ip(self.speed)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Gitar Hero")

# Values
ball = note()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball.update()

    screen.blit(ball.image, ball.rect)

    pygame.display.flip()
