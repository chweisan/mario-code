import copy

from tilemap import Tilemap
class Level:
    """ A class to represent a level in the game."""
    def __init__(self, num_coins, num_shellcreepers, num_sidesteppers, num_fliers, layout: Tilemap):
        self.__num_coins = num_coins
        self.__num_shellcreepers = num_shellcreepers
        self.__num_sidesteppers = num_sidesteppers
        self.__num_fliers = num_fliers
        self.__layout = layout
        self.__completed = False

    @property
    def num_coins(self):
        return self.__num_coins

    @num_coins.setter
    def num_coins(self, num_coins):
        self.__num_coins = num_coins
    
    @property
    def num_shellcreepers(self):
        return self.__num_shellcreepers
    
    @num_shellcreepers.setter
    def num_shellcreepers(self, num_shellcreepers):
        self.__num_shellcreepers = num_shellcreepers
    
    @property
    def num_sidesteppers(self):
        return self.__num_sidesteppers
    
    @num_sidesteppers.setter
    def num_sidesteppers(self, num_sidesteppers):
        self.__num_sidesteppers = num_sidesteppers

    @property
    def num_fliers(self):
        return self.__num_fliers
    
    @num_fliers.setter
    def num_fliers(self, num_fliers):
        self.__num_fliers = num_fliers

    @property
    def layout(self):
        return self.__layout
    
    @property
    def completed(self):
        """ Returns True if the level is completed, False otherwise. Call every update to check if the level is completed."""
        if self.__num_shellcreepers == 0 and self.__num_sidesteppers == 0 and self.__num_fliers == 0:
            self.__completed = True
        return self.__completed
    
    def update(self, num_coins, num_shellcreepers, num_sidesteppers, num_fliers):
        """ Updates the number of entities in the level."""
        self.__num_coins = num_coins
        self.__num_shellcreepers = num_shellcreepers
        self.__num_sidesteppers = num_sidesteppers
        self.__num_fliers = num_fliers
    
class Levels:
    """ A class to represent all the levels in the game and manage how to pass to the next level."""

    def __init__(self, levels_list:list = []):
        self.__levels_list = levels_list
        self.__current_level = 0

    @property
    def current_level(self) -> int:
        """ Returns the current level, starting in 0."""
        return self.__current_level

    @current_level.setter
    def current_level(self, level: int):
        """ Sets the current level to the level given."""
        self.__current_level = level

    
    @property
    def current_level_object(self) -> Level:
        """ Returns the current level object, starting in 0. 
        If the level requested is greater than the number of levels, it will return the module of the level requested and the number of levels,
        so it will start again from the first levels."""
        level = self.__levels_list[self.__current_level % len(self.__levels_list)]
        return copy.deepcopy(level)

    def append(self, level):
        """ Appends a new level to the list of levels."""
        self.__levels_list.append(level)

    def next_level(self) -> int:
        """ Increments the current level by 1 and return the new level"""
        self.__current_level += 1
        return self.__current_level