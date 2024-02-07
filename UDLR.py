import pygame
import random
import time

# Constants for colors and screen dimensions
WHITE = (255, 255, 255)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Constants for directions and scores
DIRECTIONS = ["Up", "Down", "Left", "Right"]
CORRECT_SCORE = 100
INCORRECT_PENALTY = 50
GAME_DURATION = 30  # 30 seconds

def display_direction():
    return random.choice(DIRECTIONS)

def draw_arrow(screen, direction):
    font = pygame.font.Font(None, 36)
    text = font.render(direction, True, WHITE)
    screen.blit(text, (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2 - 20))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Directions Game")

    clock = pygame.time.Clock()
    score = 0
    missed = 0
    start_time = time.time()
    end_time = start_time + GAME_DURATION

    while time.time() < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
        pygame.display.update()

        target_direction = display_direction()
        draw_arrow(screen, target_direction)

        user_input = None
        while user_input is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        user_input = "Up"
                    elif event.key == pygame.K_DOWN:
                        user_input = "Down"
                    elif event.key == pygame.K_LEFT:
                        user_input = "Left"
                    elif event.key == pygame.K_RIGHT:
                        user_input = "Right"

        if user_input.lower() == target_direction.lower():
            print("Correct! You earn 100 points.")
            score += CORRECT_SCORE
        else:
            print("Incorrect! You lose 50 points.")
            score -= INCORRECT_PENALTY
            missed += 1

    pygame.quit()
    
    print("\nGame Over!")
    print(f"Your score: {score} points")
    print(f"Missed directions: {missed} times")

if __name__ == "__main__":
    main()
