from to_do import TODO


class Hero:
    def __init__(self):
        self.__health = 10
        self.__level = 0

    @property
    def health(self):
        return self.__health

    @property
    def level(self):
        return self.__level

    def sick(self):
        self.__health -= 1


    def heal(self):
        self.__health += 1


    def attack(self):
        self.__level += 1
if __name__ == "__main__":

    hero = Hero()


    print(hero.health)  # 10
    print(hero.level)  # 0


    hero.sick()
    print(hero.health)  # 9


    hero.heal()
    print(hero.health)  # 10


    hero.attack()
    print(hero.level)  # 1





