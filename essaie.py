import pygame
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Paramètres du joueur
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0
player_speed = 3


# Gérer les mouvements du joueur
def move_player(keys, player_pos, player_angle):
    if keys[pygame.K_z]:
        player_pos[0] += player_speed * math.cos(player_angle)
        player_pos[1] += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_pos[0] -= player_speed * math.cos(player_angle)
        player_pos[1] -= player_speed * math.sin(player_angle)
    if keys[pygame.K_q]:
        player_angle -= 0.05
    if keys[pygame.K_d]:
        player_angle += 0.05
    return player_pos, player_angle

# Carte du monde (1 = mur, 0 = vide)
world_map = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

# Dimensions des carrés de la carte
TILE_SIZE = 64
map_width = len(world_map[0])
map_height = len(world_map)

# Fonction pour lancer les rayons
def cast_rays(screen, player_pos, player_angle):
    num_rays = 120  # Nombre de rayons lancés
    fov = math.pi / 3  # Champ de vision du joueur
    max_depth = 800  # Profondeur maximale

    for i in range(num_rays):
        # Calcul de l'angle de chaque rayon
        ray_angle = player_angle - fov / 2 + fov * i / num_rays
        x, y = player_pos

        # Tracer le rayon jusqu'à toucher un mur
        for depth in range(max_depth):
            target_x = x + depth * math.cos(ray_angle)
            target_y = y + depth * math.sin(ray_angle)

            # Vérifier si le rayon touche un mur
            if world_map[int(target_y // TILE_SIZE)][int(target_x // TILE_SIZE)] == 1:
                # Calculer la distance au mur
                distance = depth * math.cos(ray_angle - player_angle)
                
                # Calculer la hauteur de la colonne à afficher
                wall_height = 5000 / (distance + 0.0001)  # pour éviter la division par zéro
                
                # Dessiner une colonne de pixels pour simuler le mur
                color = (255 - min(255, int(distance * 0.1)),) * 3
                pygame.draw.rect(screen, color, (i * (WIDTH // num_rays), HEIGHT // 2 - wall_height // 2, WIDTH // num_rays, wall_height))
                break



# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches
    keys = pygame.key.get_pressed()
    player_pos, player_angle = move_player(keys, player_pos, player_angle)

    # Affichage des rayons (et des murs)
    screen.fill((0, 0, 0))
    cast_rays(screen, player_pos, player_angle)

    # Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(60)

# Quitter le jeu
pygame.quit()
