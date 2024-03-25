import random
import sys


class Game_kniffel:
    def __init__(self):
        self.players = []
        self.dice = [0, 0, 0, 0, 0]
        self.round = 1
        self.current_player = 0
        self.current_throw = 0
        self.current_round = 1
        self.current_category = 0
        self.categories = [
            "Ones",
            "Twos",
            "Threes",
            "Fours",
            "Fives",
            "Sixes",
            "Three of a kind",
            "Four of a kind",
            "Full House",
            "Small Straight",
            "Large Straight",
            "Chance",
            "Kniffel",
        ]
        self.categories_score = [0] * len(self.categories)
        self.categories_used = [False] * len(self.categories)
        self.categories_score_total = 0
        self.categories_score_bonus = 35
        self.categories_score_upper = 0
        self.categories_score_lower = 0
        self.categories_score_upper_bonus = False
        self.categories_score_total = 0

    def add_player(self, name):
        self.players.append(name)

    def next_player(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0
            self.current_round += 1
        if self.current_round > 13:
            self.end_game()

    def end_game(self):
        print("Game over")
        for i in range(len(self.players)):
            print(f"{self.players[i]}: {self.categories_score[i]}")
        sys.exit()

    def throw_dice(self):
        if self.current_throw >= 3:
            return
        for i in range(len(self.dice)):
            if self.dice[i] == 0:
                self.dice[i] = random.randint(1, 6)
        self.current_throw += 1

    def reset_dice(self):
        self.dice = [0, 0, 0, 0, 0]
        self.current_throw = 0

    def set_category(self, category):
        if self.categories_used[category]:
            return
        self.categories_used[category] = True
        self.categories_score[category] = self.calculate_score(category)
        self.categories_score_total += self.categories_score[category]
        if category < 6:
            self.categories_score_upper += self.categories_score[category]
            if self.categories_score_upper >= 63:
                self.categories_score_bonus = 35
        else:
            self.categories_score_lower += self.categories_score[category]
        self.next_player()

    def calculate_score(self, category):
        if category < 6:
            return self.dice.count(category + 1) * (category + 1)
        if category == 6:
            return self.calculate_three_of_a_kind()
        if category == 7:
            return self.calculate_four_of_a_kind()
        if category == 8:
            return self.calculate_full_house()
        if category == 9:
            return self.calculate_small_straight()
        if category == 10:
            return self.calculate_large_straight()
        if category == 11:
            return self.calculate_chance()
        if category == 12:
            return self.calculate_kniffel()

    def calculate_three_of_a_kind(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 3:
                return sum(self.dice)
        return 0

    def calculate_four_of_a_kind(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 4:
                return sum(self.dice)
        return 0

    def calculate_full_house(self):
        for i in range(1, 7):
            if self.dice.count(i) == 3:
                for j in range(1, 7):
                    if self.dice.count(j) == 2:
                        return 25
        return 0

    def calculate_small_straight(self):
        if sorted(self.dice) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
            return 30
        return 0

    def calculate_large_straight(self):
        if sorted(self.dice) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            return 40
        return 0

    def calculate_chance(self):
        return sum(self.dice)

    def calculate_kniffel(self):
        for i in range(1, 7):
            if self.dice.count(i) == 5:
                return 50
        return 0

    def print_game(self):
        print(f"Round: {self.current_round}")
        print(f"Player: {self.players[self.current_player]}")
        print(f"Throw: {self.current_throw}")
        print(f"Category: {self.categories[self.current_category]}")
        print(f"Score: {self.categories_score}")
        print(f"Total: {self.categories_score_total}")
        print(f"Upper: {self.categories_score_upper}")
        print(f"Lower: {self.categories_score_lower}")
        print(f"Bonus: {self.categories_score_bonus}")
        print(f"Upper bonus: {self.categories_score_upper_bonus}")
        print(f"Dice: {self.dice}")

    def play(self):
        while True:
            self.print_game()
            self.throw_dice()
            self.print_game()
            self.reset_dice()
            self.set_category(0)
            self.next_player()


game = Game_kniffel()
game.add_player("Alice")
game.play()
