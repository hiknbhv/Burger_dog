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
#TODO: we need some constants.  WINDOW_WIDTH and WINDOW_HEIGHT, 800, 600
#TODO: create display_surface assign to it pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#TODO: call pygame.display.set_caption()  and pass in the argument "Burger Dog"

#TODO: create an FPS variable and assign 60 to it.
#TODO: create a clock variable and assign pygame.time.Clock()

#TODO: we need the following constants
#TODO: PLAYER_STARTING_LIVES, PLAYER_NORMAL_VELOCITY, PLAYER_BOOST_VELOCITY, STARTING_BOOST_LEVEL
#TODO: STARTING_BURGER_VELOCITY, BURGER_ACCELERATION, BUFFER_DISTANCE
#TODO: values of these variables are: 3, 5, 10, 100, 3, 0.5, 100


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
#TODO: create a player_lives variable and assign PLAYER_STARTING_LIVES to it
#TODO: create a player_velocity variable and assign PLAYER_NORMAL_VELOCITY to it
#TODO: create a boost_level variable and assign STARTING_BOOST_LEVEL to it
#TODO: create a burger_velocity variable and assign STARTING_BURGER_VELOCITY to it


#TODO: 3 colors, ORANGE, BLACK, AND WHITE.  BLACK and WHITE are standard RGB, ORANGE is a tuple (246, 170, 54)
#TODO: please note the colors are tuples.

#TODO: create a font variable and assign pygame.font.Font() passing in "WashYourHand.ttf", 32

#NOTES:  text is a str, background_color is a tuple[int, int, int]
#NOTES:  **locations is basically a dictionary of str, tuple[int, int] or int
#NOTES:  this prep_text returns a tuple containing a Font object and a Rectangle object.
#TODO: create a text_to_return variable and assign font.render(text, True, background_color)
#TODO: create a rect variable and assign text_to_return.get_rect()
#TODO: create a for location in locations loop
#TODO: for loop block start
def prep_text(text : str, background_color : tuple[int, int, int], **locations):
    text_to_return = font.render(text, True, background_color)
    text_to_return_rect =  text_to_return.get_rect()
    for locations in loctions:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        # NOTE:  We'll add more later.
    #TODO: for loop block end
    #TODO: return (text_to_return, rect)
    pass #TODO: remove this when done.