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


# Set Text Blocks

# TODO: (2025-02-06): assign to (points_text, points_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burger Points: {burger_points}", ORANGE,
# TODO: (continued): topleft=(10, 10)

# TODO: (2025-02-06): assign to (score_text, score_rect)
# TODO: (continued): the result of the call to prep_text() given f"Score: {score}", ORANGE,
# TODO: (continued): topleft=(10, 50)

# TODO: (2025-02-06): assign to (title_text, title_rect)
# TODO: (continued): the result of the call to prep_text() given "Burger Dog", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=10

# TODO: (2025-02-06): assign to (eaten_text, eaten_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burgers Eaten: {burgers_eaten}", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=50

# TODO: (2025-02-06): assign to (lives_text, lives_rect)
# TODO: (continued): the result of the call to prep_text() given f"Lives: {player_lives}", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 10)

# TODO: (2025-02-06): assign to (boost_text, boost_rect)
# TODO: (continued): the result of the call to prep_text() given f"Boost: (boost_level)", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 50)

# TODO: (2025-02-06): assign to (game_over_text, game_over_rect)
# TODO: (continued): the result of the call to prep_text() given f"FINAL SCORE: {score}", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2)

# TODO: (2025-02-06): assign to (continue_text, continue_rect)
# TODO: (continued): the result of the call to prep_text() given "Press any key to play again", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2 + 64)

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
