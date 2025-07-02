import pygame as pg
import math
from data.maps import level_1, level_2

# _ = False
# mini_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
#     [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
#     [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
#     [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
#     [1, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, 2, _, _, _, _, _, 3, 4, _, 4, 3, _, 1],
#     [1, _, _, 5, _, _, _, _, _, _, 3, _, 3, _, _, 1],
#     [1, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
#     [1, 1, 3, 3, _, _, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
#     [1, 1, 1, 3, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 3, 3, 4, _, _, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, _, _, 5, _, _, _, 5, _, _, _, 5, _, _, _, 3],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
# ]

mini_map = level_2.mini_map


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.player = self.game.player
        self.minimap_scale = 5  # Échelle de la mini-map (ajuster selon les préférences) et taille d'une case sur la mini-map
        self.tile_size = self.minimap_scale * 2 # Facteur de conversion pour correspondre à l'échelle réelle, chaque tuile de la carte sera dessinée avec cette taille
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw_circle_object(self, color: tuple, center: tuple, radius: float):
        pg.draw.circle(self.game.screen, color, center, radius)
    
    def draw(self, object=None):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 10, pos[1] * 10, 10, 10), 1)
         for pos in self.world_map]
        
        
        
        # Dessiner la position du joueur 
        player_x = int(self.player.pos[0] * self.tile_size) # Conversion selon la même échelle
        player_y = int(self.player.pos[1] * self.tile_size)
        pg.draw.circle(self.game.screen, (0, 255, 0), (player_x, player_y), 5)  # Position du joueur

        # Surface temporaire pour le cône de vue
        cone_surface = pg.Surface((self.game.screen.get_width(), self.game.screen.get_height()), pg.SRCALPHA)

        # Dessiner le cône de vue (semi-transparent)
        view_distance = 30  # Longueur du cône
        half_fov = math.radians(30)  # Moitié du champ de vision (en radians, ici 60° total)
        

        # Calcul des extrémités du cône
        angle_left = self.player.angle - half_fov
        angle_right = self.player.angle + half_fov

        left_x = player_x + view_distance * math.cos(angle_left)
        left_y = player_y + view_distance * math.sin(angle_left)

        right_x = player_x + view_distance * math.cos(angle_right)
        right_y = player_y + view_distance * math.sin(angle_right)

        # Dessiner un triangle sur la surface temporaire
        pg.draw.polygon(
            cone_surface, 
            (0, 255, 0, 100),  # Couleur RGBA (100 pour la transparence)
            [(player_x, player_y), (left_x, left_y), (right_x, right_y)]
        )
        
        # Blitter la surface temporaire sur l'écran principal
        self.game.screen.blit(cone_surface, (0, 0))
        
