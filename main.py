import random, pygame

pygame.init()

Window_Width = 800
Window_Height = 600
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Burger Dog")

FPS = 60
Clock = pygame.time.Clock()

Player_Starting_Lives = 3
Player_Normal_Velocity = 5
Player_Boost_Velocity = 10
Staring_Boost_Level = 100
Starting_Burger_Velocity = 3
Burger_Acceleration = 0.5
Buffer_Distance = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = Player_Starting_Lives
player_velocity = Player_Normal_Velocity
boost_level = Staring_Boost_Level
burger_velocity = Starting_Burger_Velocity

Orange = (246, 170, 54)
Black = (0, 0, 0)
White = (255, 255, 255)

font = pygame.font.Font("WashYourHand.ttf", 32)



# NOTES:  text is a str, background_color is a tuple[int, int, int]
# NOTES:  **locations is basically a dictionary of str, tuple[int, int] or int
# NOTES:  this prep_text returns a tuple containing a Font object and a Rectangle object.
def prep_text(text: str, background_color: tuple[int, int, int], **locations):
    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()
    for location in locations:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "y":
            rect.y = locations["y"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "topright":
            rect.topright = locations["topright"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "center":
            rect.center = locations["center"]
    return text_to_return, rect


#result of call
(points_text, points_rect) = prep_text( f"Burger Points: {burger_points}", Orange, topleft=(10, 10))
(score_text, score_rect) = prep_text( f"Score: {score}", Orange, topleft=(10, 50))
(title_text, title_rect) = prep_text( f"Burger Dog", Orange, centerx=(Window_Width // 2, 10))
(eaten_text, eaten_rect) = prep_text( f"Burgers Eaten: {burgers_eaten}", Orange, centerx=(Window_Width // 2, 50))
(lives_text, lives_rect) = prep_text( f"Lives: {player_lives}", Orange,  topright=(Window_Width - 10, 10))
(boost_text, boost_rect) = prep_text( f"Boost: {boost_level}", Orange, topright=(Window_Width - 10, 50))
(game_over_text, game_over_rect) = prep_text( f"FINAL SCORE: {score}", Orange, center=(Window_Width // 2, Window_Height //2))
(continue_text, continue_rect) = prep_text( "Press any key to play again", Orange, center=(Window_Width // 2, Window_Height // 2 + 64))


bark_sound = pygame.mixer.Sound("bark_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("bd_background_music.wav")

player_image_right = pygame.image.load("dog_right.png")
player_image_left = pygame.image.load("dog_left.png")

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = Window_Width // 2
player_rect.bottom = Window_Height

burger_image = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()


burger_rect.topleft = (random.randint(0, Window_Width - 32), -Buffer_Distance)
#NOTES:  running and not pause, running and pause, not running


pygame.mixer.music.play()
running = True
is_paused = False

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def move_player():
    #set requires global(global(vairable your setting))
    global player_image
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    elif keys[pygame.K_RIGHT] and player_rect.right < Window_Width:
        player_rect.x -= player_velocity
        player_image = player_image_left

    #TODO: (2025-02-10): check if keys[pygame.K_UP] and player.rect.top > 100
    #TODO: (cont.): the if statement block
    #TODO: (cont.):  the if statement block should subtract player_velocity from player_rect.y
    #TODO: (cont.):  end of the if block

    #TODO: (2025-02-10): check if keys[pygame.K_DOWN] and player.rect.bottom < WINDOW_HEIGHT
    #TODO: (cont.): the if statement block
    #TODO: (cont.):  the if statement block should add player_velocity to player_rect.y
    #TODO: (cont.):  end of the if block

    engage_boost(keys)

    pass #TODO: (2025-02-10):  remove this when done.

def engage_boost(keys):
    global boost_level, player_velocity
    if keys[pygame.K_SPACE] and boost_level > 0:
        boost_level -= 1
    else:
        player_velocity = Player_Normal_Velocity

def move_burger():
    global burger_points
    burger_rect.y += burger_velocity
    burger_points = int(burger_velocity*(Window_Height - burger_rect.y + 100))


def handle_miss():
    global player_lives
    if burger_rect.y > Window_Height:
        player_lives -= 1
        miss_sound.play()
    burger_rect.topleft = (random.randint(0, Window_Width - 32), -Buffer_Distance)
    #TODO: (2025-02-10):  set burger_velocity to STARTING_BURGER_VELOCITY
    #TODO: (2025-02-10):  set player_rect.centerx to WINDOW_WIDTH // 2
    #TODO: (2025-02-10):  set player_rect.bottom to WINDOW_HEIGHT
    #TODO: (2025-02-10):  set boost_level to STARTING_BOOST_LEVEL
    pass #TODO: (2025-02-10):  remove this when done.

def check_collisions():
    global score, burgers_eaten
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burgers_eaten += 1
        bark_sound.play()
        #TODO: (2025-02-10):  add burger_points to score
        #TODO: (2025-02-10):  add 1 to burgers_eaten
        #TODO: (2025-02-10):  call bark_sounds' play method
        burger_rect.topleft = (random.randint(0, Window_Width - 32), -Buffer_Distance)
        #TODO: (2025-02-10):  add BURGER_ACCELERATION to burger_velocity

        #TODO: (2025-02-10):  add 25 to boost_level
        #TODO: (2025-02-10):  finally check if boost_level > STARTING_BOOST_LEVEL
        #TODO: (2025-02-10):  then set boost_level to STARTING_BOOST_LEVEL
        pass #TODO: (2025-02-10):  remove this when done.

def update_hud():
    points_text = font.render("Burger Points: " + str(burger_points), True, Orange)
    score_text = font.render("Score: " + str(score), True, Orange)
    eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, Orange)
    lives_text = font.render("Lives: " + str(player_lives), True, Orange)


def check_game_over():
    #TODO: hold till 2025-02-12
    pass #TODO: (2025-02-10):  remove this when done.


def display_hud():
    display_surface.fill(Black)
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, scorce_rect)
    display_surface.blits(title_text, title_rect)
    display_surface.blits(eaten_text, eaten_rect)
    display_surface.blits(lives_text, lives_rect)
    display_surface.blits(boost_text, boost_rect)
    #TODO (2025-02-10): We just blit points_text and points_rect
    #TODO (cont.):  repeat for score, title, eaten, lives, boost
    pygame.draw.line(display_surface, White, (0, 100), (Window_Width, 100), 3)
    display_surface.blits(player_image, player_rect)
    display_surface.blits(burger_image, burger_rect)

def handle_clock():
    pygame.display.update()
    Clock.tick(FPS)


## GAME LOOP COMING SOON.