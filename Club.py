import math
import statistics

class Club:

    # Constructor method with instance variables name and age
    def __init__(self, name):
        self.name = name
        self.strike_ratings = []
        self.strike_consistency = statistics.mean(self.strike_ratings) #consistency is the average of how well the ball is hit with this club
        self.horizontal_misses = [] #yards left or right I usually miss
        self.miss_tendency = statistics.mean(self.horizontal_misses)
        self.distances = []
        self.distance = statistics.mean(self.distances)

    # Method with instance variable followers
    def update_distance(self, new_distance):
        self.distances.append(new_distance)
        self.distance = statistics.mean(self.distances)

    def update_strike_consistency(self, new_strike_rating):
        # Strike rating key:
        # 1 = horrible
        # 2 = bad 
        # 3 = okay
        # 4 = good
        # 5 = excellent
        self.strike_ratings.append(new_strike_rating)
        self.strike_consistency = statistics.mean(self.strike_ratings)

    def update_miss_tendency(self, new_miss):
        self.horizontal_misses.append(new_miss)
        self.miss_tendency = statistics.mean(self.horizontal_misses)




