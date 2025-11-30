import descriptions

def describe_location(player_position):
    location = descriptions.map_description.get(player_position)
    items = descriptions.map_items.get(player_position)["items"]
    if location:
        print(location)
        if items:
            print("You see the following items:", ", ".join(items))
        else:
            print("There are no items here.")
    else:
        print("You are in an unknown location.")