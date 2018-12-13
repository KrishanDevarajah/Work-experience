from splashkit import *

def main():
        open_window("Cave Escape", 432, 768)

load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()




        while not window_close_requested_named("Cave Escape"):
            # Update
            process_events()
            handle_input(player)
            update_velocity(player)
            update_sprite(player)


            # Pre-Draw
            clear_screen(color_white())

            # Post-Draw
            refresh_screen()

        # Cleanup
        free_resource_bundle("CaveEscape")
        close_window("Cave Escape")

main()
def get_new_player():
    result = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result))
    sprite_set_y(result, screen_width() / 2)
    sprite_start_animation_named(result, "Fly")

    return result

    GRAVITY = 0.08
    MAX_SPEED = 6

    def update_velocity(player):
    sprite_set_dy(player, sprite_dy(player) + GRAVITY)

    if (sprite_dy(player) > MAX_SPEED):
        sprite_set_dy(player, MAX_SPEED)
    elif (sprite_dy(player) < -MAX_SPEED):
        sprite_set_dy(player, -MAX_SPEED)

GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED=-2

def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player, sprite_dy(player) - JUMP_RECOVERY_BOOST)

        class pole_data:
    def __init__(self, _score_limiter, _up_pole, _down_pole):
        self.score_limiter = _score_limiter
        self.up_pole = _up_pole
        self.down_pole = _down_pole

    def get_random_poles():
    resultUpPole = create_sprite_with_bitmap_named("UpPole")
    resultDownPole = create_sprite_with_bitmap_named("DownPole")

    sprite_set_x(resultUpPole, screen_width() + rnd_int(1200))
    sprite_set_y(resultUpPole, screen_height() - sprite_height(resultUpPole))

    sprite_set_x(resultDownPole, sprite_x(resultUpPole))
    sprite_set_y(resultDownPole, 0)

    sprite_set_dx(resultUpPole, FOREGROUND_SCROLL_SPEED)
    sprite_set_dx(resultDownPole, FOREGROUND_SCROLL_SPEED)

    result = pole_data(False, resultUpPole, resultDownPole)

    return result

    def update_poles(poles):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    def draw_poles(poles):
    draw_sprite(poles.up_pole)
    draw_sprite(poles.down_pole)

    def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    game_poles = get_random_poles()
    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        update_poles(game_poles)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_poles(game_poles)
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")
}main()

def get_new_player():
    result = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result))
    sprite_set_y(result, screen_width() / 2)
    sprite_start_animation_named(result, "Fly")

    return result
def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")
GRAVITY = 0.08
MAX_SPEED = 6
def update_velocity(player):
    sprite_set_dy(player, sprite_dy(player) + GRAVITY)

     if (sprite_dy(player) > MAX_SPEED):
        sprite_set_dy(player, MAX_SPEED)
    elif (sprite_dy(player) < -MAX_SPEED):
        sprite_set_dy(player, -MAX_SPEED)

def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")

    GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2

def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player, sprite_dy(player) - JUMP_RECOVERY_BOOST)

def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")


GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2

class pole_data:
    def __init__(self, _score_limiter, _up_pole, _down_pole):
        self.score_limiter = _score_limiter
        self.up_pole = _up_pole
        self.down_pole = _down_pole


def get_random_poles():
    resultUpPole = create_sprite_with_bitmap_named("UpPole")
    resultDownPole = create_sprite_with_bitmap_named("DownPole")

    sprite_set_x(resultUpPole, screen_width() + rnd_int(1200))
    sprite_set_y(resultUpPole, screen_height() - sprite_height(resultUpPole))

    sprite_set_x(resultDownPole, sprite_x(resultUpPole))
    sprite_set_y(resultDownPole, 0)

    sprite_set_dx(resultUpPole, FOREGROUND_SCROLL_SPEED)
    sprite_set_dx(resultDownPole, FOREGROUND_SCROLL_SPEED)

    result = pole_data(False, resultUpPole, resultDownPole)

    return result




def update_poles(poles):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)


def draw_poles(poles):
    draw_sprite(poles.up_pole)
    draw_sprite(poles.down_pole)



def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    game_poles = get_random_poles()
    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        update_poles(game_poles)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_poles(game_poles)
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")
}


def reset_pole_data(poles):
    free_sprite(poles.up_pole)
    free_sprite(poles.down_pole)

    poles = get_random_poles()
    return poles

def update_poles(poles):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    if ((sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0):
        poles = reset_pole_data(poles)

    return poles

get_random_poles()


game_poles = get_random_poles()

GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2
NUM_POLES = 4


def update_pole_array(pole_array):
    for i in range(len(pole_array)):
        pole_array[i] = update_poles(pole_array[i])

    return pole_array



def draw_pole_array(pole_array):
    for i in range(len(pole_array)):
        draw_poles(pole_array[i])



def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    game_poles = [get_random_poles() for i in range(NUM_POLES)]

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        game_poles = update_pole_array(game_poles)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_pole_array(game_poles)
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")



GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2
BACKGROUND_SCROLL_SPEED = -1
NUM_POLES = 4

class scene_data:
    def __init__(self, _background, _foreground, _foreroof):
        self.background = _background
        self.foreground = _foreground
        self.foreroof = _foreroof


class game_data:
    def __init__(self, _scene, _poles, _player):
        self.scene = _scene
        self.poles = _poles
        self.player = _player



def get_new_scene():
    resultBackground = create_sprite_with_bitmap_named("Background")
    sprite_set_x(resultBackground, 0)
    sprite_set_y(resultBackground, 0)
    sprite_set_dx(resultBackground, BACKGROUND_SCROLL_SPEED)

    resultForeground = create_sprite_with_bitmap_and_animation_named("Foreground", "ForegroundAnimations")
    sprite_set_x(resultForeground, 0)
    sprite_set_y(resultForeground, screen_height() - sprite_height(resultForeground))
    sprite_set_dx(resultForeground, FOREGROUND_SCROLL_SPEED)
    sprite_start_animation_named(resultForeground, "Fire")

    resultForeroof = create_sprite_with_bitmap_named("Foreroof")
    sprite_set_x(resultForeroof, 0)
    sprite_set_y(resultForeroof, 0)
    sprite_set_dx(resultForeroof, FOREGROUND_SCROLL_SPEED)

    return scene_data(resultBackground, resultForeground, resultForeroof)



def update_scene(scene):
    update_sprite(scene.background)
    update_sprite(scene.foreground)
    update_sprite(scene.foreroof)

    if sprite_x(scene.background) <= -(sprite_width(scene.background) / 2):
        sprite_set_x(scene.background, 0)

    if sprite_x(scene.foreground) <= -(sprite_width(scene.foreground) / 2):
        sprite_set_x(scene.foreground, 0)
        sprite_set_x(scene.foreroof, 0)



def update_player(player):
    update_velocity(player)
    update_sprite(player)



def update_game(game):
    process_events()
    handle_input(game.player)
    game.poles = update_pole_array(game.poles)
    update_player(game.player)
    update_scene(game.scene)
    return game


def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)


def get_new_game():
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    resultScene = get_new_scene()
    resultPoles = [get_random_poles() for i in range(NUM_POLES)]
    resultPlayer = get_new_player()

    return game_data(resultScene, resultPoles, resultPlayer)




def main():
    open_window("Cave Escape", 432, 768)

    game_data = get_new_game()

    while not window_close_requested_named("Cave Escape"):
        # Update
        game_data = update_game(game_data)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_game(game_data)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")






class player_data:
    def __init__(self, _sprite_data, _score, _is_dead):
        self.sprite_data = _sprite_data
        self.score = _score
        self.is_dead = _is_dead


class game_data:
    def __init__(self, _scene, _poles, _player):
        self.scene = _scene
        self.poles = _poles
        self.player = _player



def get_new_player():
    resultSpriteData = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(resultSpriteData, (screen_width() / 2) - sprite_width(resultSpriteData))
    sprite_set_y(resultSpriteData, screen_width() / 2)
    sprite_start_animation_named(resultSpriteData, "Fly")

    resultScore = 0
    resultIsDead = False

    return player_data(resultSpriteData, resultScore, resultIsDead)



def get_random_poles():

    resultUpPole = create_sprite_with_bitmap_named("UpPole")
    resultDownPole = create_sprite_with_bitmap_named("DownPole")

    sprite_set_x(resultUpPole, screen_width() + rnd_int(1200))
    sprite_set_y(resultUpPole, screen_height() - sprite_height(resultUpPole) - rnd_int(bitmap_height_of_bitmap_named("Foreground")) + 1)

    sprite_set_x(resultDownPole, sprite_x(resultUpPole))
    sprite_set_y(resultDownPole, rnd_int(bitmap_height_of_bitmap_named("Foreroof")) + 1)

    sprite_set_dx(resultUpPole, FOREGROUND_SCROLL_SPEED)
    sprite_set_dx(resultDownPole, FOREGROUND_SCROLL_SPEED)

    return pole_data(True, resultUpPole, resultDownPole)



def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST)



def update_poles(poles, player):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    if sprite_x(poles.up_pole) < sprite_x(player.sprite_data) and poles.score_limiter:
        poles.score_limiter = False
        player.score += 1

    if (sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0:
        poles = reset_pole_data(poles)

    return poles




def update_pole_array(game):
    for i in range(len(game.poles)):
        game.poles[i] = update_poles(game.poles[i], game.player)

    return game


def update_player(player):
    update_velocity(player)
    update_sprite(player.sprite_data)


def check_for_collisions(game):
    if sprite_collision(game.player.sprite_data, game.scene.foreground) or sprite_collision(game.player.sprite_data, game.scene.foreroof):
        game.player.is_dead = True

    for pole in game.poles:
        if sprite_collision(game.player.sprite_data, pole.up_pole) or sprite_collision(game.player.sprite_data, pole.down_pole):
            game.player.is_dead = True

    return game



def reset_player(player):
    free_sprite(player.sprite_data)
    player = get_new_player()
    return player


def reset_game(game):
    game.player = reset_player(game.player)
    for i in range(len(game.poles)):
        game.poles[i] = reset_pole_data(game.poles[i])

    return game




def update_game(game):
    if not game.player.is_dead:
        game = check_for_collisions(game)
        process_events()
        handle_input(game.player)
        game = update_pole_array(game)
        update_player(game.player)
        update_scene(game.scene)
    else:
        game = reset_game(game)

    return game



def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player.sprite_data)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)

    draw_text_font_as_string(str(game.player.score), color_white(), "GameFont", 21, 10, 0)


def get_new_game():
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    resultScene = get_new_scene()
    resultPoles = [get_random_poles() for i in range(NUM_POLES)]
    resultPlayer = get_new_player()

    return game_data(resultScene, resultPoles, resultPlayer)


class player_state(Enum):
    MENU = 1
    PLAY = 2


class player_data:
    def __init__(self, _sprite_data, _score, _is_dead, _state):
        self.sprite_data = _sprite_data
        self.score = _score
        self.is_dead = _is_dead
        self.state = _state


def get_new_player():
    resultSpriteData = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(resultSpriteData, (screen_width() / 2) - sprite_width(resultSpriteData))
    sprite_set_y(resultSpriteData, screen_width() / 2)
    sprite_start_animation_named(resultSpriteData, "Fly")

    resultScore = 0
    resultIsDead = False
    resultState = player_state.MENU

    return player_data(resultSpriteData, resultScore, resultIsDead, resultState)


def handle_input(player):
    if key_typed(KeyCode.space_key):
        if player.state == player_state.PLAY:
            sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST)
        else:
            player.state = player_state.PLAY



def update_player(player):
    if player.state == player_state.PLAY:
        update_velocity(player)

    update_sprite(player.sprite_data)


def update_game(game):
    if not game.player.is_dead:
        game = check_for_collisions(game)
        process_events()
        handle_input(game.player)
        update_player(game.player)
        update_scene(game.scene)

        if game.player.state == player_state.PLAY:
            game = update_pole_array(game)

    else:
        game = reset_game(game)

    return game



def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player.sprite_data)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)

    if game.player.state == player_state.PLAY:
        draw_text_font_as_string(str(game.player.score), color_white(), "GameFont", 21, 10, 0)
    else:
        draw_bitmap_named("Logo", 0, 40)
        draw_text_font_as_string("PRESS SPACE!", color_white(), "GameFont", 21, 55, 550)


asw23aqQ]]while  V:
    pass








