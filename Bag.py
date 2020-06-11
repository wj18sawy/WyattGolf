class Bag:

    def __init__(self, name, clubs):
        self.name = name
        self.clubs = clubs

    def add_club(self, new_club):
        self.clubs.Append(new_club)

def create_bag_from_payload(dct):
    return Bag(dct['name'], dct['clubs'])