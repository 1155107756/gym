import pygame
from Box2D import Box2D

from gym.envs.box2d.car_dynamics import Car
from gym.envs.box2d.car_racing_multi_players import CarRacing

if __name__ == "__main__":
    import sys, pygame

    world = Box2D.b2World(
        (0, 0),
        )
    pygame.init()
    size = width, height = 680,340
    speed = [2, 2]
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    fake_screen = screen.copy()

    car = Car(world, 0, 200, 200)
    playground = pygame.surface.Surface((10, 10))
    playground.fill(white)
    screen.fill(white)
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        car.draw_for_pygame(playground)
        fake_screen.blit(playground, (0, 0))

        #screen.blit(pygame.transform.rotozoom(fake_screen, 0, 10), (0,0))
        car.draw_for_pygame(screen)
        pygame.display.update()
