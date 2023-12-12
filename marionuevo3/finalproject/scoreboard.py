# So in map we take care of what goes on in the game: platforms, objects and bg
class Map:
    def __init__(self, width, height):
        """Here we would initialize all the entities that will appear on the game
        i.e. Mario and enemies"""
        self.shellcreepers = None
        self.coins = None
        self.mario = None
        self.texts = []     # texts that will contain the score
        self.texts = ["500", "800",
                      "1600"]  # texts that will contain the score
        # enemies
        # this will work this way: a loop that will execute for each element (enemy) inside the list
        # once the enemy dies (lives = 0) we would use a pop function to remove this enemy form the list
        # lives for mario, that will be drawn in the main program:
        self.lives_sprite = [24, 0, 0, 104, 8, 8]
        # score:
        self.__score = 0
        self.__max_score = 0    # I use max score instead of top score
        self.i_score = "{:06d}".format(self.__score)   # score is not yet defined,
        # but it's a 6-digit number, I'm nor sure if the score would be in
        # map or in the main program, but anyway, we'd have a part in update
        # that will constantly change the score, otherwise it would remain
        # as it begins
        self.top_score = "{:06d}".format(self.__max_score)
        self.i_sprite = [24, 14, 0, 0, 96, 16, 8]
        self.top_sprite = [104, 14, 0, 96, 96, 32, 8]
        self.i_score_sprite = []  # we must figure out a way to make it so
        # that x value will be the one below
        self.top_score_sprite = []
        self.__score_numbers = {"0": 16, "1": 24, "2": 32, "3": 40, "4": 48, "5": 56, "6": 64, "7": 72, "8": 80, "9": 88}

    def score_update(self, score):
        self.__score = score
        if self.__max_score < self.__score:
            self.__max_score = self.__score

        self.i_score = "{:06d}".format(self.__score)
        self.i_score_sprite.clear()
        self.top_score = "{:06d}".format(self.__max_score)
        self.top_score_sprite.clear()
        for n in range(
                6):  # update for top score, would do later, if we decide the player can play again
            self.i_score_sprite.append(
                [0, self.__score_numbers[self.i_score[n]], 96, 8, 8])
            self.top_score_sprite.append(
                [0, self.__score_numbers[self.top_score[n]], 96, 8, 8])

