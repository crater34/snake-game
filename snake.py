import pygame

class Snake:
    def __init__(self,x_s=300,y_s=300,image=pygame.image.load('head_up.png'),speed=3):
        self.x_s=x_s
        self.y_s=y_s
        self.image=image
        self.speed=speed
    def get_x_s(self):
        return self.x_s
    def get_y_s(self):
        return self.y_s
    def set_image(self,img):
        self.image=img
    def get_image(self):
        return self.image
