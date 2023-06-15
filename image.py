from datetime import datetime
import pygame
import random
import numpy as np

        
class Image:
    def __init__(self, screen, settings,k,array,value,picnum):
        self.screen = screen
        self.settings = settings
        self.first_time = datetime.now()
        self.value = 99
        self.k =0
        self.get_image(self.k)
        self.array = np.zeros(30)
        self.k = 1
        self.picnum = picnum
        
    def image_update(self):

        second_time = datetime.now()
        if (second_time - self.first_time).seconds >= self.settings.change_image_seconds:
            self.screen.fill(self.settings.screen_bg_color)
            if (second_time - self.first_time).seconds >= self.settings.change_image_microseconds:
                self.get_image(self.k)
                self.array[self.k-1]=value
                self.first_time = second_time
                self.image_show()              
                self.k=self.k+1
        else:
            self.image_show()
        return (self.first_time,self.array,self.k)
    
    def image_show(self):
        self.screen.blit(self.image, self.rect)
    def get_image(self,k):
        global value
        if self.k==0 or self.k== self.picnum:
            value=99
        else:
            value = random.randint(1, self.settings.image_number)
        self.image = pygame.image.load(self.settings.image_path % value)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center