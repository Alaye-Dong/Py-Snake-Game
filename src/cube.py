import pygame
from assets import load_images  # 导入加载图像的函数

class cube():
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, is_snake_head=False, is_snake_body=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        # 加载图像
        claus_img, gift_img, beer_img = load_images(self.w, self.rows)

        # 绘制蛇头
        if is_snake_head:
            surface.blit(beer_img, (i * dis, j * dis))  # 使用 beer_img 绘制蛇头
        # 绘制蛇身
        elif is_snake_body:
            surface.blit(claus_img, (i * dis, j * dis))  # 使用 claus_img 绘制蛇身
        # 绘制食物
        else:
            surface.blit(gift_img, (i * dis, j * dis))  # 使用 gift_img 绘制食物