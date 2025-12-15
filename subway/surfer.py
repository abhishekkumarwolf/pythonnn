import pygame
import random
import sys


pygame.init()
width, height = 600, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Subway Surfer Clone - Simple")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)


lanes = [150, 300, 450]

player_lane = 1
player_base_y = 550
player_y = player_base_y
player_width = 50
player_height = 80


is_jumping = False
jump_height = 18
jump_count = jump_height


obstacles = []
obstacle_speed = 8
spawn_timer = 0
SPAWN_INTERVAL = 40  # frames


score = 0
font = pygame.font.SysFont("Arial", 32)
big_font = pygame.font.SysFont("Arial", 56)


game_over = False


def spawn_obstacle():
    lane_idx = random.choice([0, 1, 2])
    obs = {
        "x": lanes[lane_idx] - 25,
        "y": -120,
        "w": 50,
        "h": 80,
        "lane": lane_idx,
        "scored": False  
    }
    obstacles.append(obs)

def draw_player(lane, y):
    x = lanes[lane]
    pygame.draw.rect(screen, BLUE, (x - player_width // 2, int(y), player_width, player_height))

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (obs["x"], int(obs["y"]), obs["w"], obs["h"]))

def check_collision(lane, y):
    player_rect = pygame.Rect(lanes[lane] - player_width // 2, int(y), player_width, player_height)
    for obs in obstacles:
        obs_rect = pygame.Rect(obs["x"], int(obs["y"]), obs["w"], obs["h"])
        if player_rect.colliderect(obs_rect):
            return True
    return False

def reset_game():
    global obstacles, score, obstacle_speed, spawn_timer, player_lane, player_y, is_jumping, jump_count, game_over
    obstacles = []
    score = 0
    obstacle_speed = 8
    spawn_timer = 0
    player_lane = 1
    player_y = player_base_y
    is_jumping = False
    jump_count = jump_height
    game_over = False


while True:
    clock.tick(60)
    screen.fill(WHITE)


    pygame.draw.rect(screen, GRAY, (0, player_base_y + player_height, width, height - (player_base_y + player_height)))
    for x in lanes:
        pygame.draw.line(screen, BLACK, (x, 0), (x, height), 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT and player_lane > 0:
                    player_lane -= 1
                elif event.key == pygame.K_RIGHT and player_lane < 2:
                    player_lane += 1
                elif event.key == pygame.K_UP and not is_jumping:
                    is_jumping = True
                    jump_count = jump_height
            else:
           
                if event.key == pygame.K_r:
                    reset_game()
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

    if not game_over:
       
        if is_jumping:
           
            if jump_count >= -jump_height:
                neg = 1
                if jump_count < 0:
                    neg = -1
                displacement = (jump_count ** 2) * 0.2 * neg
                player_y = player_base_y - displacement
                jump_count -= 1
            else:
                # reset jump
                is_jumping = False
                jump_count = jump_height
                player_y = player_base_y
        else:
            player_y = player_base_y  
       
        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            spawn_obstacle()
            spawn_timer = 0
         
            SPAWN_INTERVAL = random.randint(30, 55)

        
        for obs in obstacles:
            obs["y"] += obstacle_speed

        new_obs = []
        for obs in obstacles:
            if obs["y"] > height + 150:
                
                if not obs.get("scored", False):
                    score += 1
               
            else:
                
                if not obs.get("scored", False) and obs["y"] > player_base_y + player_height:
                    score += 1
                    obs["scored"] = True
                   
                    if score % 5 == 0:
                        obstacle_speed += 0.5
                new_obs.append(obs)
        obstacles = new_obs

        # Collision check
        if check_collision(player_lane, player_y):
            game_over = True

    # Drawing
    draw_player(player_lane, player_y)
    draw_obstacles()

    # HUD: score
    score_surf = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surf, (10, 10))

    # If game over show message
    if game_over:
        over_surf = big_font.render("GAME OVER", True, (180, 0, 0))
        over_rect = over_surf.get_rect(center=(width // 2, height // 2 - 40))
        screen.blit(over_surf, over_rect)

        info_surf = font.render("Press R to Restart  •  Q or ESC to Quit", True, BLACK)
        info_rect = info_surf.get_rect(center=(width // 2, height // 2 + 20))
        screen.blit(info_surf, info_rect)

        final_score_surf = font.render(f"Final Score: {score}", True, BLACK)
        final_rect = final_score_surf.get_rect(center=(width // 2, height // 2 + 60))
        screen.blit(final_score_surf, final_rect)

    pygame.display.flip()

