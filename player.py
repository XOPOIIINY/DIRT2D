import pygame
from settings import *
from math import sin, radians, degrees, copysign


class Car(pygame.sprite.Sprite):
    def __init__(self, pos, angle, length, max_sreering, max_acceleration,
                 max_speed, brake_deceleration, free_deceleration, sprite_groups):
        super().__init__(sprite_groups)
        self.image = pygame.image.load('wrc-ford-fiesta-rally-sverhu_reb.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.angle = 0
        self.length = length
        self.max_steering = max_sreering
        self.max_acceleration = max_acceleration
        self.max_speed = max_speed
        self.brake_deceleration = brake_deceleration
        self.free_deceleration = free_deceleration
        self.pos = pos
        self.clock = pygame.time.Clock()
        self.game_time = 0

        self.acceleration = 0
        self.steering = 0

        self.direction = pygame.math.Vector2()
        self.speed = 20

        self.clock = pygame.time.Clock()

    def input(self, game_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.direction.x < 0:
                self.acceleration = self.brake_deceleration
            else:
                self.acceleration += 3 * game_time
        elif keys[pygame.K_DOWN]:
            if self.direction.x > 0:
                self.acceleration = -self.brake_deceleration
            else:
                self.acceleration -= 3 * game_time
        # elif pressed[pygame.K_SPACE]:
        #     if abs(car.velocity.x) > game_time * car.brake_deceleration:
        #         car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
        #     else:
        #         car.acceleration = -car.velocity.x / game_time
        else:
            if abs(self.direction.x) > game_time * self.free_deceleration:
                self.acceleration = -copysign(self.free_deceleration, self.direction.x)
            else:
                if game_time != 0:
                    self.acceleration = -self.direction.x / game_time
        self.acceleration = max(-self.max_acceleration, min(self.acceleration, self.max_acceleration))

        if keys[pygame.K_RIGHT]:
            self.steering -= 30 * game_time
        elif keys[pygame.K_LEFT]:
            self.steering += 30 * game_time
        else:
            self.steering = 0

        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))
        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))

        self.direction += (self.acceleration * game_time, 0)
        self.direction.x = max(-self.max_speed, min(self.direction.x, self.max_speed))

        if self.steering:
            radius = self.length / sin(radians(self.steering))
            angular_velocity = self.direction.x / radius
        else:
            angular_velocity = 0

        self.pos += self.direction.rotate(-self.angle) * game_time
        self.angle += degrees(angular_velocity) * game_time

        # self.direction.x = self.acceleration

    def move(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        self.rect = rotated.get_rect()
        print(self.pos)
        screen.blit(rotated, self.pos * 32 - (self.rect.width / 2, self.rect.height / 2))

    def update(self, game_time, screen):
        self.input(game_time)
        self.move(screen)

