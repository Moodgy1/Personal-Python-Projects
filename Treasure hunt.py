import pygame
import random
import sys
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 50
NUM_ROWS = SCREEN_HEIGHT // GRID_SIZE
NUM_COLS = SCREEN_WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TREASURE_CHANCE = 0.06
BOMB_CHANCE = 0.03
TREASURES = ["Gold coins", "Precious gems", "Ancient artifacts"]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mysterious Island Adventure")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Find the path to the directory
directory = r"C:\Users\hp\Downloads"
path_to_treasure_img = os.path.join(directory, "m507t0009_24june22_treasure_chest_01.png")

# Load images for treasure chests
try:
    treasure_img = pygame.image.load(path_to_treasure_img)
    treasure_img = pygame.transform.scale(treasure_img, (GRID_SIZE, GRID_SIZE))
except pygame.error:
    print("Could not load treasure chest image!")
    sys.exit()

# Function to draw the player, treasures, and bombs
def draw_element(x, y, color):
    pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Function to display text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw treasure chests
def draw_treasure_chest(x, y):
    screen.blit(treasure_img, (x * GRID_SIZE, y * GRID_SIZE))

# Function to restart the game
def restart_game():
    os.execv(sys.executable, ['python'] + sys.argv)

# Main game loop
def main():
    player_x = NUM_COLS // 2
    player_y = NUM_ROWS // 2

    # Set up initial player position, treasures, and bombs
    player_position = (player_x, player_y)
    treasures = {(i, j): None for i in range(NUM_ROWS) for j in range(NUM_COLS) if random.random() < TREASURE_CHANCE}
    print("Total treasures:", len(treasures))
    bombs = {(i, j): False for i in range(NUM_ROWS) for j in range(NUM_COLS) if random.random() < BOMB_CHANCE and (i, j) != player_position}

    # Track collected treasures
    collected_treasures = 0

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player_y > 0:
                    player_y -= 1
                elif event.key == pygame.K_s and player_y < NUM_ROWS - 1:
                    player_y += 1
                elif event.key == pygame.K_a and player_x > 0:
                    player_x -= 1
                elif event.key == pygame.K_d and player_x < NUM_COLS - 1:
                    player_x += 1
                elif event.key == pygame.K_r:
                    restart_game()
        
        # Check if the player steps on a bomb
        if (player_x, player_y) in bombs and not bombs[(player_x, player_y)]:
            # Player dies from bomb
            with open("death_message.txt", "w") as f:
                f.write(f"You died from a bomb. Collected treasures: {collected_treasures}, Remaining treasures: {sum(1 for t in treasures.values() if t is None)}")
            running = False
            break
        elif (player_x, player_y) in bombs:
            # If the player encounters a bomb, reveal it
            draw_element(player_x, player_y, RED)
            pygame.display.flip()
            pygame.time.delay(1000)  # Delay for a moment to show the bomb
            with open("death_message.txt", "w") as f:
                f.write(f"You died from a bomb. Collected treasures: {collected_treasures}, Remaining treasures: {sum(1 for t in treasures.values() if t is None)}")
            running = False
            break
        
        # If the player moves to a position containing a treasure, mark it as collected
        if (player_x, player_y) in treasures and not treasures[(player_x, player_y)]:
            treasures[(player_x, player_y)] = random.choice(TREASURES)
            collected_treasures += 1
        
        # Draw player
        draw_element(player_x, player_y, GREEN)

        # Draw treasures as treasure chests
        for pos, treasure in treasures.items():
            if treasure:
                draw_treasure_chest(pos[0], pos[1])

        # Display counts for collected treasures and remaining treasures
        draw_text(f"Collected: {collected_treasures}", GREEN, 20, 20)
        draw_text(f"Remaining: {sum(1 for t in treasures.values() if t is None)}", GREEN, 20, 60)

        pygame.display.flip()
        clock.tick(30)

    # Delete the death message file if it exists
    if os.path.exists("death_message.txt"):
        os.remove("death_message.txt")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


#Made By: Mohamed
#Special thanks to Asser,Ezz
#This code is licensed under the MIT License.
#https://opensource.org/licenses/MIT
#s