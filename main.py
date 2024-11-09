import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader Project - Part 1")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load the background image
background = pygame.image.load("download.jpeg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Set up the player
player = pygame.Rect(375, 500, 50, 50)

# Set up the enemies (7 enemies total)
enemies = []
for _ in range(7):
    enemy = pygame.Rect(random.randint(0, screen_width - 50), random.randint(0, screen_height // 2), 50, 50)
    enemies.append(enemy)

# Set up the score and enemy speed
score = 0
enemy_speed = 3

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < screen_width:
        player.x += 5

    # Move the enemies
    for enemy in enemies[:]:  # Create a copy of the list to modify it while looping
        enemy.y += enemy_speed
        if enemy.top > screen_height:  # Remove enemy if it moves off the screen
            enemies.remove(enemy)

        # Collision detection
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)  # Remove the enemy after a collision

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    pygame.draw.rect(screen, YELLOW, player)

    # Draw the remaining enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Display the score
    font = pygame.font.SysFont(None, 50)
    score_text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(score_text, (500, 30))

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)

    # End the game if all enemies are gone
    if not enemies:
        running = False

# Quit the game properly
pygame.quit()
