import pygame
import os
import random

#常量设置
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)           # 屏幕尺寸
START_BTN_UP_EVENT = pygame.USEREVENT               # 启动按钮用户事件
START_BTN_DOWN_EVENT = pygame.USEREVENT +1          # 启动按钮用户事件
PAUSE_BUTTON_EVENT = pygame.USEREVENT + 2           # 暂停按钮用户事件

class Background(pygame.sprite.Sprite):                   #背景精灵

    def __init__(self, is_alt=False,speed=1):
        super().__init__()

        self.image = pygame.image.load("./images/background.png")
        self.rect = self.image.get_rect()
        self.speed = speed

        if is_alt:
            self.rect.bottom = 0

    def update(self, *args):
        self.rect.top += self.speed

        if self.rect.top >= SCREEN_RECT.height:
            self.rect.bottom = 0         #
class button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image_nor = self.image = pygame.image.load("./images/resume_nor.png")
        self.image_pressed = self.image = pygame.image.load("./images/resume_pressed.png")

        self.image = self.image_nor
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_RECT.center

    def update(self, *args):
        super().update(args)

    def check_button_click(self,click):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):

            if click == "up":
                self.image = self.image_pressed
            elif click == "down":
                self.kill()

class Game:                                              #游戏主体类
    def __init__(self):
        print("游戏初始化...")

        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        Back1 = Background(False, 0)
        Back2 = Background(True, 0)
        self.back_group = pygame.sprite.Group(Back1, Back2)

        self.start_button = button()
        self.button_group = pygame.sprite.Group(self.start_button)

    def start_game(self):
        """开启游戏循环"""

        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        """事件处理"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.__finished_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.start_button.check_button_click("up")

            elif event.type == pygame.MOUSEBUTTONUP:
                self.start_button.check_button_click("down")

                for back in self.back_group.sprites():
                    back.speed = 2


    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.button_group.update()
        self.button_group.draw(self.screen)

    @staticmethod
    def __finished_game():
        """退出游戏"""
        print("退出游戏")
        pygame.quit()
        exit()




if __name__ == '__main__':

    Game().start_game()


