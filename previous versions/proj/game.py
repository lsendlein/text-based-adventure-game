import classes.game_item as game_item
import classes.game_room as game_room
import classes.player_class as player_class
import json
import glob
import parser
import datetime
import os.path

class Game:
    def __init__(self):
        self.game_instances = {}

    def get_game_instances(self):
        return self.game_instances

    def add_game_instance(self):
        self.game_instances[str(datetime.datetime.now())] = Game()

    def delete_game_instance(self, game_instance):
        del self.game_instances[game_instance]

class GameInstance:
    def __init__(self):
        self.player = None
        self.game_rooms = None
        self.game_items = None
    
    def load_rooms_json(self):
        rooms_json = {}

        # os.path.sep will decide which file separator to use depending on os
        files = glob.glob(f"rooms{os.path.sep}*", recursive=True)

        for single_file in files:
            with open(single_file, 'r') as f:
                try:
                    json_file = json.load(f)
                    rooms_json[json_file["name"]] = json_file
                except KeyError:
                    print(f'Skipping {single_file}')
        return rooms_json

    def load_items_json(self):
        items_json = {}

        # os.path.sep will decide which file separator to use depending on os
        files = glob.glob(f"items{os.path.sep}*", recursive=True)

        for single_file in files:
            with open(single_file, 'r') as f:
                try:
                    json_file = json.load(f)
                    items_json[json_file["name"]] = json_file
                except KeyError:
                    print(f'Skipping {single_file}')
        return items_json

    def init_game(self):
        rooms_json = self.load_rooms_json()
        items_json = self.load_items_json()

        # create player object
        self.player = player_class.Player("foyer")

        # initialize room objects
        self.game_rooms = {rooms_json[room]["name"]:game_room.GameRoom(rooms_json[room]["name"], rooms_json[room]["short_desc"], rooms_json[room]["long_desc"], rooms_json[room]["init_items"],
 rooms_json[room]["current_items"], rooms_json[room]["exits"]) for room in rooms_json}

        # initialize item objects
        self.game_items = {items_json[item]["name"]:game_item.GameItem(items_json[item]["name"], items_json[item]["room_description"], items_json[item]["starting_loc"], items_json[item]["current_loc"], items_json[item]["look_description"],
 items_json[item]["holdable"], items_json[item]["synonyms"], items_json[item]["verbs"], items_json[item]["is_game_key"],
  items_json[item]["is_story_item"], items_json[item]["related_items"]) for item in items_json}

    def create_new_game(self):
        new_game.init_game()
        new_game.play_game()

    def play_game(self):
        # custom code to display the first room -- this only executes once per game
        parser.display_location('foyer')
        parser.printw(self.game_rooms['foyer'].long_desc)
        print('')
        parser.printw(self.game_items['letter'].room_description)

        while True:
            parser.parser_read_input(self.player, self.game_rooms, self.game_items)

new_game = GameInstance()
new_game.create_new_game()
