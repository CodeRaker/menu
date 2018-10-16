import pygame as pg
from settings import *

class MenuBoard(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        self._layer = 1
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((Width*0.9,Height*0.9))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.centery = Height / 2
        self.rect.centerx = Width / 2

class MenuCursor(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        self._layer = 2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((self.game.MenuBoard.rect.width * 0.97, self.game.MenuBoard.rect.height / 20))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.y = self.game.MenuBoard.rect.top + self.rect.height / 2
        self.rect.centerx = Width / 2
        self.selectedItem = 0

    def down(self):
        if self.selectedItem < len(self.game.MenuItems.items) - 1:
            self.rect.y += self.rect.height
            self.selectedItem += 1

    def up(self):
        if self.selectedItem != 0:
            self.rect.y -= self.rect.height
            self.selectedItem -= 1

    def select(self):
        print(str(self.selectedItem))

class MenuItems(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        self._layer = 3
        pg.sprite.Sprite.__init__(self, self.groups)
        self.items = []
        self.font = pg.font.SysFont('Consolas', round(self.game.MenuCursor.rect.height * 0.9))
        self.image = self.font.render('', False, (255,255,255))
        self.rect = self.image.get_rect()

    def draw(self):
        counter = 0
        for item in self.items:
            textItem = self.font.render(item, False, (255,255,255))
            self.game.screen.blit(textItem, (self.game.MenuCursor.rect.left * 1.2, (self.game.MenuBoard.rect.top + self.game.MenuCursor.rect.height / 2)  + (self.game.MenuCursor.rect.height*0.1) + (self.game.MenuCursor.rect.height * counter)))
            counter += 1
