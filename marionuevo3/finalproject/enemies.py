import random

from entities import Coin
from constants import WIDTH
from constants import HEIGHT
from entities import Shellcreeper
from constants import FPS


class EntitiesManager:
    def __init__(self, num_entities: int, delay: int, entity_type: int,
                 velocity: int, spawned: int):
        self.__entities = []
        self.__entity_type = entity_type
        self.__num_entities = num_entities
        self.__velocity = velocity # Not yet done
        self.__spawned = spawned
        self.enemies = []
        self.__time_counter = 0
        self.__enemy_counter = 0
        self.__coin_counter = 0
        self.coins = []
        # The code does not know about seconds, knows about Frames Per Second
        # So we need to convert the seconds to frames
        self.__delay_frames = delay * FPS
        # Now we store the number of frames since the last entity was created
        self.__frames_since_last_entity_created = 0

    def __create_entity(self):
        if self.__entity_type == 0:
            self.__entities.append(Coin(16, 50, WIDTH, HEIGHT))
        elif self.__entity_type == 1:
            self.__entities.append(Shellcreeper(x=16, y=42, w=WIDTH,
                                                h=HEIGHT))


    @property
    def entities(self):
        return self.__entities
    
    @property
    def pending_entities(self):
        return self.__spawned

    def remove(self, entity):
        self.__entities.remove(entity)
        if self.__spawned > 0:
            self.__spawned -= 1
            self.__frames_since_last_entity_created = (self.__delay_frames *
                                                       (len(
                                                           self.__entities)-1))


    def update(self):
        # We only spawn new entities if the number of entities we want to
        # create is smaller than the number of entities we have already
        # if not, we don't create new entities
        if self.__spawned > 0:
            # We need to create a new entity because we are below the number
            # of entities we want to create on the screen
            if len(self.__entities) < self.__num_entities:
                current_delay_new_entity = self.__delay_frames * len(
                    self.__entities)
                if current_delay_new_entity == self.__frames_since_last_entity_created:
                    self.__create_entity()

        # We increment the number of frames from the start in this method
        # because we assume that this method will be invoked once per frame
        # in the main loop
        self.__frames_since_last_entity_created += 1
