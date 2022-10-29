import pygame, csv, os

from gamecore.GameObject import GameObject

class Tile(GameObject):
    def __init__(self, scene, image, x, y, width, height, depth):
        super().__init__(scene, image, x, y, width, height, depth)

class TileMap():
    def __init__(self, scene, filename):
        self.scene = scene
        self.tile_size = 80
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles(filename)
        self.addToScene()
        
    def addToScene(self):
        for tile in self.tiles:
            self.scene.add(tile)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '5':
                    tiles.append(Tile(self.scene, x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 
                                            self.scene.game.loader.wall_image, 3))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles









