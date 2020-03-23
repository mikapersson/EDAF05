

class Person:
    """Class describing a person (or something that will match with something"""
    def __init__(self, iD, pref):
        self.id = iD
        self.prefs = pref

    def printPerson(self):
        print("ID: {}, preferences: {}".format(self.id, self.prefs))
