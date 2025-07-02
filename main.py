import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.map = Map(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        self.enemies_positions = self.object_handler.npc_positions

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.enemies_positions = self.object_handler.npc_positions

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
    
    def draw_minimap(self):            
        """
        Renders a minimap of the game world, displaying walls, the player's position, 
        and the player's field of view. This function provides a visual representation 
        of the game environment to assist the player in navigation.

        The minimap is scaled for clarity, with walls drawn as rectangles, the player 
        indicated by a circle, and the view cone represented as a triangle. This helps 
        players understand their surroundings and orientation within the game.

        Args:
            self: The instance of the class that contains the game state and rendering context.

        Returns:
            None
        """
        minimap_scale = 5  # Échelle de la mini-map (ajuster selon les préférences) et taille d'une case sur la mini-map
        tile_size = minimap_scale * 2 # Facteur de conversion pour correspondre à l'échelle réelle, chaque tuile de la carte sera dessinée avec cette taille
        # for y, row in enumerate(self.map.world_map):
        #     for x, value in enumerate(row):
        #         if value == 1:  # Si c'est un mur
        #             # On dessine un rectangle pour représenter un mur
        #             pg.draw.rect(self.screen, (255, 255, 255), 
        #                         (x * tile_size, y * tile_size, tile_size, tile_size))
        
        # Dessiner la position du joueur 
        player_x = int(self.player.pos[0] * tile_size) # Conversion selon la même échelle
        player_y = int(self.player.pos[1] * tile_size)
        pg.draw.circle(self.screen, (0, 255, 0), (player_x, player_y), 5)  # Position du joueur

        for enemy in self.enemies_positions:
            enemy_x = int(enemy[0] * tile_size)
            enemy_y = int(enemy[1] * tile_size)
            pg.draw.circle(self.screen, (255, 0, 0), (enemy_x, enemy_y), 5)  # Position de l'ennemi

        
        # Surface temporaire pour le cône de vue
        cone_surface = pg.Surface((self.screen.get_width(), self.screen.get_height()), pg.SRCALPHA)

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
        self.screen.blit(cone_surface, (0, 0))
        



    def run(self):
        while True:
            self.check_events()
            # self.draw_minimap()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
