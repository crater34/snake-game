#217716521
import random
import pygame


class Appear:
    def __init__(self,x=random.randint(0, 720),y=random.randint(0, 720)):
        self.x =x
        self.y =y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Apple(Appear):
    def __init__(self,x=random.randint(0, 720),
                 y=random.randint(0, 720),app_img=pygame.image.load('apple.png'),score=1):
        super().__init__(x,y)
        self.score=score
        self.app_img=app_img
    def get_score(self):
        return self.score
    def set_score(self,scr):
        self.score=scr
    def get_img(self):
        return self.app_img
    def get_img_width(self):
        return self.app_img.get_width()
    def get_img_height(self):
        return self.app_img.get_height()
    def change_coo(self):
        self.x=random.randint(0,720)
        self.y=random.randint(0,720)
class PowUp(Apple):
    def __init__(self,x=random.randint(0, 720),y=random.randint(0, 720)
                 ,rand_img=pygame.image.load('crate.png')):
        super().__init__(x,y,rand_img)
        self.start=0
        self.is_on=False
    def disappear(self):
        self.x,self.y=999,999
    def timer(self):
        self.is_on=True
        self.start=pygame.time.get_ticks()
    def time_over(self):
        if self.is_on and pygame.time.get_ticks()-self.start>10000:
            self.is_on=False
    def get_is_on(self):
        return self.is_on