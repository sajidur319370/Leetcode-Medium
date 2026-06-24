from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class FoodRatings:
    # O(n log n)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_cuisines = defaultdict(str)
        self.foods_ratings = defaultdict(int)
        self.cuisines_ratings_foods = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.foods_cuisines[foods[i]] = cuisines[i]
            self.foods_ratings[foods[i]] = ratings[i]
            self.cuisines_ratings_foods[cuisines[i]].add((-ratings[i], foods[i]))

    # O(log n)
    def changeRating(self, food: str, newRating: int) -> None:
        c = self.foods_cuisines[food]
        r = self.foods_ratings[food]

        self.cuisines_ratings_foods[c].remove((-r, food))
        self.cuisines_ratings_foods[c].add((-newRating, food))

        self.foods_ratings[food] = newRating

    # O(1)
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_ratings_foods[cuisine][0][1]


obj = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                  ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                  [9, 12, 8, 15, 14, 7])
obj.changeRating("sushi", 16)
obj.changeRating("ramen", 16)
print(obj.highestRated("korean"))
print(obj.highestRated("japanese"))
