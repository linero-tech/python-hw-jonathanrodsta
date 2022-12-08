from to_do import TODO


class Hero:
    def __init__(self):
        self._health = 10
        self._level = 0

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    def sick(self):
        self._health -= 1

    def heal(self):
        self._health += 1

    def attack(self):
        self._level += 1
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





