
import arcade

# Screen.
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Battles"

# Player globals.
SPRITE_SIZE = 0.6
MOVEMENT_SPEED = 10
HORIZONTAL_START_POS = 60
VERTICAL_START_POS = 60


class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
        # Move player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        # Call the parent class initializer.
        super().__init__(width, height, title)

        # Variables that will hold sprite lists.
        self.player_list = None

        # Set up the player info.
        self.player_sprite = None

        # Set up the background.
        self.background = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Set up the background.
        self.background = arcade.load_texture("game_art/background.png")

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player("game_art/ship.png", SPRITE_SIZE)
        self.player_sprite.center_x = HORIZONTAL_START_POS
        self.player_sprite.center_y = VERTICAL_START_POS

        # Add the player.
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background.
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)

        # Draw all the sprites.
        self.player_list.draw()


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Change player speed when left or right key is pressed.
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # Stop moving when key is released.
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """Main controls the gameplay."""

    # Set up the window.
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()

    # Play the game.
    arcade.run()


if __name__ == "__main__":
    main()