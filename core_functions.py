import world

def game_start():
    game_over = False
    player_position = (0, 0)
    
    game_state = {
        "game_over": game_over,
        "player_position": player_position
    }
    return game_state

def overworld(player_position, game_over):
    print("What do you want to do?")
    print("A) Move Forward")
    print("B) Move Backwards")
    print("C) Turn Left")
    print("D) Turn Right")
    print("E) Check your inventory.")
    print("F) Look Around.")
    print("Type 'QUIT' to exit the game.")
    user_input = input("Choose an option (A, B, or C): ").strip().upper()
    match user_input:
        case 'A':
            print("You move forward.")
        case 'B':
            print("You move backwards.")
        case 'C':
            print("You turn left.")
        case 'D':
            print("You turn right.")
        case 'E':
            print("You check your inventory.")
        case 'F':
            print("You look around.")
            world.describe_location(player_position)
            return game_over
        case 'QUIT':
            print("Static fills your vision as you feel yourself slipping away...")
            game_over = True
            return game_over