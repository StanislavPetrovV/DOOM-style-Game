from sprite_object import *


class Weapon(AnimatedSprite):
    """
    Represents a weapon in the game that can be animated and drawn on the screen. 
    This class manages the weapon's images, position, and shooting animations.

    The weapon can be animated to show the shooting action and is responsible for rendering itself 
    at the correct position on the game screen. It also handles the reloading state and updates 
    the animation frames accordingly.

    Args:
        game: The game instance that the weapon belongs to.
        path: The file path to the weapon's sprite images.
        scale: The scale factor for the weapon's sprite.
        animation_time: The duration for the weapon's animation.

    Attributes:
        images: A deque containing the weapon's images for animation.
        weapon_pos: The position where the weapon is drawn on the screen.
        reloading: A boolean indicating if the weapon is currently reloading.
        num_images: The total number of images for the weapon's animation.
        frame_counter: A counter for the current animation frame.
        damage: The damage dealt by the weapon when fired.
    """

    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def animate_shot(self):
        if not self.reloading:
            return
        self.game.player.shot = False
        if self.animation_trigger and self.images:
            self.images.rotate(-1)
            self.image = self.images[0]
            self.frame_counter += 1
            if self.frame_counter >= self.num_images:  # Use >= to handle edge case
                self.reloading = False
                self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        

    def update(self):
        self.check_animation_time()
        self.animate_shot()