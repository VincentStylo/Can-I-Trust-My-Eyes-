import core_functions  # Assuming you're using a module named 'core_functions'
import dialogue

def main():
    initial_state = core_functions.game_start()
    game_over = initial_state["game_over"]

    print(f"Game over status: {game_over}")  # Just for demonstration
    player_x, player_y = initial_state["player_position"]

    dialogue.scene_one()
    while game_over == False:
        game_over = core_functions.overworld((player_x, player_y), game_over)
    print("And then it all turned to black...")


if __name__ == "__main__":
    main()
