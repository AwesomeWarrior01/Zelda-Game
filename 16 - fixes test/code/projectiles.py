import pygame
from settings import *
#from player import *

class Projectiles(pygame.sprite.Sprite):
    def __init__(self, player, groups, projectile_move): #only works for player for now. For enemies, this would have to be
        super().__init__(groups)
        self.sprite_type = 'projectile'
        self.direction = player.status.split('_')[0]

        self.projectile_index = 0 #This is fine for now, but it will always select bullet.
        self.projectile = list(projectile_data.keys())[self.projectile_index]

        #projectile timer

        self.timer = pygame.time.get_ticks()

        # graphic

        full_path = f'../graphics/projectiles/{self.projectile}/{self.direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(24 + 7*projectile_move, 8))
        elif self.direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(-24 - 7*projectile_move, 8))
                #print('left') # succefully runs the function! Now the bullet needs to be printed
        elif self.direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 16 + 7*projectile_move))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, -16 - 7*projectile_move))
            #while current_time >= pygame.time.get_ticks() - 500: #This is probably not the right approach
                #pass #nothing = 1+1 #this statement is here to literally do nothing
            #I need to return the value of the image each time, but it gets overridden while in this function

    '''def projectile_go_vrmmmm(self, player, projectile_move, projectile_time): #probably delete this method
        #current_time = pygame.time.get_ticks()

        projectile_move += projectile_move
        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(24, 8 + projectile_move*0.1 ))
        elif self.direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(-24, 8))
            # print('left') # successfully runs the function! Now the bullet needs to be printed
        elif self.direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 16))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, -16))'''
