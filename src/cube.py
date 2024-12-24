import pygame
from assets import load_images  # 导入加载图像的函数
class cube():
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
            
    def draw(self, surface, is_snake=True):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        # 在绘制时加载图像
        claus_img, gift_img = load_images(self.w, self.rows)
        # 如果是蛇，绘制蛇图像
        if is_snake:
            surface.blit(claus_img, (i*dis, j*dis))  # 绘制蛇的图像
        else:
            surface.blit(gift_img, (i*dis, j*dis))  # 绘制食物的图像
