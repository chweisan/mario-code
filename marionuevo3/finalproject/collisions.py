from tilemap import Tilemap
import pyxel

class CollisionEntity:
    def __init__(self, layout: Tilemap):
        # Global for collisions
        self.__layout = layout

    @property
    def layout(self) -> Tilemap:
        return self.__layout

    def touches_floor(self, entity) -> bool:
        raise TypeError("Do not use this class without inheritance")
        # Method to see if he touches floor

    def touches_ceiling(self, entity) -> bool:
        # Method to see if the hits the ceiling, as well as controlling those big jumps
        raise TypeError("Do not use this class without inheritance")


class CollisionMario(CollisionEntity):

    def touches_floor(self, mario) -> bool:
        # Method to see if he touches floor
        return (self.layout.is_floor(self.layout.get_tile(mario.x,
                                                          mario.y + 32))
                or self.layout.is_floor(self.layout.get_tile(mario.x + 8,
                                                             mario.y + 32)))

    def touches_ceiling(self, mario) -> bool:
        # Method to see if the hits the ceiling, as well as controlling those big jumps
        is_touching = (self.layout.is_ceiling(self.layout.get_tile(mario.x,
                                                                   mario.y))) or (
                          self.layout.is_ceiling(self.layout.get_tile(
                              mario.x + 8, mario.y)))
        return is_touching

    # def rebound(self, tile: bool, x: int, y: int) -> bool:
    # if Collision.touches_ceiling():

    def touch_little_entity(self, mario, little_entities: list):
        """Coins, fire, etc..."""
        for little_entity in little_entities:
            if (mario.x <= little_entity.x < mario.x + 16 and mario.y <=
                little_entity.y < mario.y + 24) or (
                    mario.x <= little_entity.x + 7 < mario.x + 16 and mario.y <=
                    little_entity.y < mario.y + 24) or (
                    mario.x <= little_entity.x < mario.x + 16 and mario.y <=
                    little_entity.y + 7 < mario.y + 24) or (
                    mario.x <= little_entity.x + 7 < mario.x + 16 and mario.y <=
                    little_entity.y + 7 < mario.y + 24):
                return little_entity
        return None

    def touch_big_entity(self, mario, big_entities: list):
        """Shellcreepers cangrejos, etc..."""
        for big_entity in big_entities:
            if (mario.x <= big_entity.x < mario.x + 16 and mario.y <=
                big_entity.y < mario.y + 24) or (
                    mario.x <= big_entity.x + 15 < mario.x + 16 and mario.y <=
                    big_entity.y < mario.y + 24) or (
                    mario.x <= big_entity.x < mario.x + 16 and mario.y <=
                    big_entity.y + 15 < mario.y + 24) or (
                    mario.x <= big_entity.x + 15 < mario.x + 16 and mario.y <=
                    big_entity.y + 15 < mario.y + 24):
                return big_entity
        return None

    def bump_entity(self, mario, big_entities: list):
        for big_entity in big_entities:
            if (mario.x <= big_entity.x < mario.x + 16 and mario.y - 24 <=
                big_entity.y+ 16 < mario.y) or (
                    mario.x <= big_entity.x + 15 < mario.x + 16 and
                    mario.y - 24 <=
                    big_entity.y + 16 < mario.y):
                return big_entity
        return None


class CollisionEnemy(CollisionEntity):
    def touches_floor(self, enemy) -> bool:
        # Method to see if he touches floor
        return (self.layout.is_floor(self.layout.get_tile(enemy.x,
                                                          enemy.y +
                                                          enemy.height +
                                                          8))
                or self.layout.is_floor(self.layout.get_tile(enemy.x
                                                             + 8,
                                                             enemy.y +
                                                             enemy.height
                                                             + 8)))


class CollisionCoin(CollisionEntity):
    def touches_floor(self, coin) -> bool:
        # Method to see if he touches floor
        return (self.layout.is_floor(self.layout.get_tile(coin.x,
                                                          coin.y +
                                                          coin.height +
                                                          8)))
