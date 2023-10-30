# A Class with 5 classattributes, 3 of them with private setter & getter

x = None 

# Class with constructor
class Haustier:
    def __init__(self, *args):
        self.name = args[0]
        self.farbe = args[1]
        self.__alter = 0
        self.__rasse = ""
        self.__merkmale = ""

# Get & Set
    def get_alter(self):
        return self.__alter

    def set_alter(self, alter):
        self.__alter = alter

    def get_rasse(self):
        return self.__rasse

    def set_rasse(self, rasse):
        self.__rasse = rasse

    def get_merkmale(self):
        return self.__merkmale

    def set_merkmale(self, merkmale):
        self.__merkmale = merkmale


    def show_haustier(self):
        print(f"Das Haustier {self.name} hat die Farbe {self.farbe} und ist schon {self.__alter} Jahre alt. Die Rasse ist {self.__rasse} und das besondere Merkmale am Haustier ist: {self.__merkmale}")


# Instance of the class
x = Haustier("Rufus", "Rosa")
x.set_alter(4)
x.set_rasse("Nacktmul")
x.set_merkmale("gepunktet")
x.show_haustier()
