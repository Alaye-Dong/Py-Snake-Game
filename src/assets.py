# assets.py
import pygame

def load_images(width, rows):
    # 加载和缩放图像
    claus_img_pre = pygame.image.load('./assets/img/claus.png')  # 加载蛇的图像
    gift_img_pre = pygame.image.load('./assets/img/gift.png')    # 加载食物的图像
    deer_img_pre = pygame.image.load('./assets/img/deer.png')    # 加载鹿的图像

    dis = width // rows  # 获取每个格子的大小
    claus_img = pygame.transform.scale(claus_img_pre, (dis, dis))  # 调整蛇的图像大小
    gift_img = pygame.transform.scale(gift_img_pre, (dis, dis))    # 调整食物的图像大小
    deer_img = pygame.transform.scale(deer_img_pre, (dis, dis))    # 调整鹿的图像大小

    return claus_img, gift_img, deer_img