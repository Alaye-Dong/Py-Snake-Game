import pygame
from snake import snake
from cube import cube
from utils import drawGrid, randomSnack

width = 500
height = 500
cols = 25
rows = 20

def redrawWindow():
    global win
    win.fill((0,0,0))
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    # 显示得分
    font = pygame.font.Font(None, 36)  # 创建字体对象
    score_text = font.render(f"Score: {len(s.body)-1}", True, (255, 255, 255))  # 渲染得分文本
    win.blit(score_text, (10, 10))  # 将得分文本绘制到屏幕上
    pygame.display.update()

def main():
    pygame.init()
    global s, snack, win
    win = pygame.display.set_mode((width,height))
    s = snake((255,0,0), (10,10))
    s.addCube()
    snack = cube(randomSnack(rows,s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(8)
        s.move()
        headPos = s.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s), color=(0,255,0))
            
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score:", len(s.body))
                s.reset((10,10))
                break
                    
        redrawWindow()

if __name__ == "__main__":
    main()
