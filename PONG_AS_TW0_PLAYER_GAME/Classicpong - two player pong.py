# Step 1: Import and Initialize
import pygame
import sys

pygame.init()

# Step 2: Screen Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Pong")

# Step 3: Colors and Clock
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 60

# Step 4: Game Objects
# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player = pygame.Rect(20, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 30, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_SIZE = 15
ball = pygame.Rect(WIDTH//2 - 7, HEIGHT//2 - 7, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Scores
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 50)

# Sounds
paddle_hit_sound = pygame.mixer.Sound("paddle_hit.wav")
score_sound = pygame.mixer.Sound("score.wav")

# Step 5: Main Game Loop
while True:
    # Step 6: Handle Events (User Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys for both players
    keys = pygame.key.get_pressed()

    # Player 1 (Left Paddle) Controls: W and S
    if keys[pygame.K_w] and player.top > 0:
        player.y -= 7
    if keys[pygame.K_s] and player.bottom < HEIGHT:
        player.y += 7

    # Player 2 (Right Paddle) Controls: UP and DOWN Arrows
    if keys[pygame.K_UP] and opponent.top > 0:
        opponent.y -= 7
    if keys[pygame.K_DOWN] and opponent.bottom < HEIGHT:
        opponent.y += 7

    # Step 7: Move Ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Step 8: Ball Collision with Top/Bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Step 9: Ball Collision with Paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        paddle_hit_sound.play()

    # Step 10: Scoring
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1
        score_sound.play()

    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1
        score_sound.play()

    # Step 11: Drawing Everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display Scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (WIDTH*3//4, 20))

    # Update Screen
    pygame.display.flip()
    clock.tick(FPS)
