from npc import NPC

class SoldierNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)

class CacoDemonNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/caco_demon/0.png', pos=(10.5, 6.5),
                 scale=0.7, shift=0.27, animation_time=250):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 150
        self.attack_damage = 25
        self.speed = 0.05
        self.accuracy = 0.35

class CyberDemonNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/cyber_demon/0.png', pos=(11.5, 6.0),
                 scale=1.0, shift=0.04, animation_time=210):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 6
        self.health = 350
        self.attack_damage = 15
        self.speed = 0.055
        self.accuracy = 0.25





















