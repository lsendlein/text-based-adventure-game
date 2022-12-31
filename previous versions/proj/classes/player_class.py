# Exceptions to handle errors - could be replaced by the 'return False' comments, but I kept the Exceptions in case
# we need to do more with error handling, etc
class ItemNotFound(Exception):
    pass


class ItemAlreadyHeld(Exception):
    pass


class LocationAlreadyVisited(Exception):
    pass


class Player:
    def __init__(self, cur_location, inventory=[], locs_visited=None):

        # list - holds the players inventory
        # e.g. ['coin', 'piano_cartridge', 'fire_poker', ...]
        self.inventory = inventory

        # list - holds the locations that the player has visited (to track giving long/short desc)
        # e.g. ['Foyer', 'Office', 'Music Room', 'Library', ...]
        self.locs_visited = locs_visited

        # holds the players current location
        self.cur_location = cur_location
        # add the location to locs_visited
        self.add_location(cur_location)

    def add_item(self, item) -> bool:
        # adds an item to the player's inventory
        # check to see if inventory has been initialized
        if self.inventory is None:
            self.inventory = []

        # check to see if the item is already in the player's inventory
        if self.has_item(item):
            raise Exception(ItemAlreadyHeld)
            # return False

        # add the item to the player's inventory
        self.inventory.append(item)
        return True

    def remove_item(self, item) -> bool:
        # removes an item from the player's inventory
        # try to remove item from inventory
        if self.has_item(item):
            self.inventory.remove(item)
            return True
        else:
            # player does not have item in inventory
            raise Exception(ItemNotFound)
            # return False

    def view_inventory(self) -> list:
        # return the contents of the player's inventory
        return self.inventory

    def add_location(self, location) -> bool:
        # adds a location to the player's visited locations
        # check to see if locs_visited has been initialized
        if self.locs_visited is None:
            self.locs_visited = ["foyer"]
            return True

        # check to see if we have already added the location
        if location in self.locs_visited:
            raise Exception(LocationAlreadyVisited)
            # return False
        else:
            self.locs_visited.append(location)
            return True

    # def remove_location(self, location): is this needed? I can't think of any scenario where we'd remove a location

    def has_item(self, item) -> bool:
        # returns true if the player has a given item
        if not self.inventory:
            return False
        elif item in self.inventory:
            return True
        else:
            return False

    def get_location(self) -> str:
        # returns the player's current location
        return self.cur_location

    def get_locs_visited(self) -> list:
        # returns the locations the player has visited
        return self.locs_visited

    def update_location(self, location) -> None:
        # updates the player's current location
        self.cur_location = location

        # adds the location to the list of locations
        if location not in self.get_locs_visited():
            self.add_location(location)


if __name__ == "__main__":
    # test code
    p1 = Player("Foyer")

    # location functions
    print("Current Location: " + p1.get_location())
    p1.update_location("Library")
    print("Current Location: " + p1.get_location())
    print("Locations Visited: " + str(p1.get_locs_visited()) + "\n")

    # inventory functions
    p1.add_item("Fire Poker")
    p1.add_item("Coin")
    p1.add_item("Shovel")
    print("Current Inventory: " + str(p1.view_inventory()))
    print("Has Coin: " + str(p1.has_item("Coin")))
    p1.remove_item("Coin")
    print("Current Inventory: " + str(p1.view_inventory()))
    print("Has Coin: " + str(p1.has_item("Coin")))
