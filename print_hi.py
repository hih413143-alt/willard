import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
rndom=random.randint(1,800)
player = pygame.Rect(50, 200, 20, 100)
tree = pygame.Rect(rndom, 150, 50, 150)
is_jumping = False
jump_velocity = 0
obstacle = pygame.Rect(600, 250, 50, 50)
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        jump_velocity = -15  # jump force

    if is_jumping:
        player.y += jump_velocity
        jump_velocity += 1  # gravity effect

    if player.y >= 200:  # ground level
        player.y = 200
        is_jumping = False
        jump_velocity = 0
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    obstacle.x -= 5

    if obstacle.x <= 0:
        obstacle.x = 800
        score += 1  # add 1 point each time enemy crosses screen

   

    screen.fill((135, 206, 235))  # sky
    pygame.draw.rect(screen, (34, 139, 34), (0, 300, 800, 300))
    pygame.draw.rect(screen, (0, 255, 0), player)  # player
    pygame.draw.rect(screen,((101, 67, 33)),tree) # tree
    pygame.draw.circle(screen, (0, 100, 0), (tree.x + 25, tree.y), 60)  # tree foliage
    pygame.draw.rect(screen, (0, 255, 0), obstacle)  # obstacle
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
   # Game Over check
    if player.colliderect(obstacle):   # <-- better than x == x
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (250, 200))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
