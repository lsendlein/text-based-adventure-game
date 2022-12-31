items_json = {
    "FirePoker": {"name": "Fire Poker",
                "description": "description",
                "starting_location": "Furnace Room",
                "curr_location": "Furnace Room",
                "synonyms": [],
                "holdable": True,
                "verbs": [],
                "is_game_key": True,
                "is_story_item": False},
    "Furnace": {"name": "Furnace",
                "description": "description",
                "starting_location": "Furnace Room",
                "curr_location": "Furnace Room",
                "synonyms": [],
                "holdable": False,
                "verbs": [],
                "is_game_key": False,
                "is_story_item": False},
    "Barrels": {"name": "Barrels",
                "description": "description",
                "starting_location": "Furnace Room",
                "curr_location": "Furnace Room",
                "synonyms": [],
                "holdable": False,
                "verbs": [],
                "is_game_key": False,
                "is_story_item": False},
}

rooms_json = {
    "Foyer": {"name": "Foyer",
            "long_desc": "long desc",
            "short_desc": "short_desc",
            "init_items": [],
            "current_items": [],
            "exits": [],
            },
    "Attic": {"name": "Attic",
            "long_desc": "long desc",
            "short_desc": "short_desc",
            "init_items": [],
            "current_items": [],
            "exits": [],
            },
    "Kitchen": {"name": "Kitchen",
            "long_desc": "long desc",
            "short_desc": "short_desc",
            "init_items": [],
            "current_items": [],
            "exits": [],
            },

}

class GameItem:
    def __init__(self, name, description, start_location, curr_location, synonyms, holdable, verbs, isGameKey, isStoryItem) -> None:
        self.name = name
        self.description = description
        self.start_location = start_location
        self.curr_location = curr_location
        self.synonyms = synonyms
        self.holdable = holdable
        self.verbs = verbs
        self.isGameKey = isGameKey
        self.isStoryItem = isStoryItem

class GameRoom:
    def __init__(self, name, short_desc, long_desc, init_items, current_items, exits) -> None:
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.init_items = init_items
        self.current_items = current_items
        self.exits = exits

# GameItems are filled with info from items JSON?
# we could convert to objects using list comprehension but then idk how we would easily access them later
game_items = [GameItem(items_json[item]["name"], items_json[item]["description"], items_json[item]["starting_location"], items_json[item]["curr_location"],
 items_json[item]["holdable"], items_json[item]["synonyms"], items_json[item]["verbs"], items_json[item]["is_game_key"],
  items_json[item]["is_story_item"]) for item in items_json]

# i think a dictionary comprehension would be nice bc we can make the key the name of the room (and even do away with the 'name' attribute entirely if we wanted)
# and access like game_items_dict["Fire Poker"].start_location
game_items_dict = {items_json[item]["name"]:GameItem(items_json[item]["name"], items_json[item]["description"], items_json[item]["starting_location"], items_json[item]["curr_location"],
 items_json[item]["holdable"], items_json[item]["synonyms"], items_json[item]["verbs"], items_json[item]["is_game_key"],
  items_json[item]["is_story_item"]) for item in items_json}

# can use the same method for rooms as well
game_rooms = {rooms_json[room]["name"]:GameRoom(rooms_json[room]["name"], rooms_json[room]["long_desc"], rooms_json[room]["short_desc"], rooms_json[room]["init_items"],
 rooms_json[room]["current_items"], rooms_json[room]["exits"]) for room in rooms_json}

print(game_items_dict["Fire Poker"].start_location)
print(game_rooms["Attic"].name)