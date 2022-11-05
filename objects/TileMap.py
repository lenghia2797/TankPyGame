import pygame, csv, os

from gamecore.GameObject import GameObject
from objects.Coin import Coin
from objects.Enemy import Enemy
from objects.Item import Item
from objects.Wall import Wall

class TileMap():
    def __init__(self, scene, filename):
        self.scene = scene
        self.tile_size = 80
        self.start_x, self.start_y = 0, 0
        self.tiles = []
        self.enemies = []
        self.coins = []
        self.items = []
        self.load_tiles(filename)
        self.addToScene()
        
    def addToScene(self):
        for tile in self.tiles:
            self.scene.add(tile)
        for enemy in self.enemies:
            self.scene.add(enemy)
        for coin in self.coins:
            self.scene.add(coin)
        for item in self.items:
            self.scene.add(item)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        map = self.read_csv(filename)
        x, y = 0, 0
        loader = self.scene.game.loader
        for row in map:
            x = 0
            for tile in row:
                pos_x = x * self.tile_size
                pos_y = y * self.tile_size
                size = self.tile_size
                if tile == '0':
                    self.enemies.append(Enemy(self.scene, pos_x, pos_y, size, size, 
                                            loader.tank_blue_image, 3))
                    
                if tile == '2':
                    self.items.append(Item(self.scene, pos_x, pos_y, 60, 50, 
                                            loader.wrench_red_image, 3))
                    
                if tile == '3':
                    self.tiles.append(Wall(self.scene, pos_x, pos_y, size, size, 
                                            loader.wall_image, 3))
                    
                if tile == '5':
                    self.coins.append(Coin(self.scene, pos_x, pos_y, size, size, 
                                            loader.coin_image, 3))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size









