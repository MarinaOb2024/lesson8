#Создаем абстрактный класс Weapon
from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

#создадим несколько классов, унаследованных от Weapon
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")
#Добавим поле weapon для хранения текущего оружия и
# метод change_weapon() для изменения оружия.
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Поле для хранения оружия

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("У бойца нет оружия!")
#Создаем класс Monster, который просто будет представлять врага для бойца.
class Monster:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def take_damage(self):
        self.is_alive = False
        print(f"{self.name} побежден!")
#Создадим функцию, которая будет демонстрировать бой
# между бойцом и монстром с выбранным оружием.
def battle(fighter, monster):
    if monster.is_alive:
        fighter.attack()
        monster.take_damage()
    else:
        print(f"{monster.name} уже побежден!")
# Создаем бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Создаем оружие
sword = Sword()
bow = Bow()

# Боец выбирает меч и атакует монстра
fighter.change_weapon(sword)
battle(fighter, monster)

# Появляется новый монстр
monster2 = Monster("Другой Монстр")

# Боец меняет оружие на лук и атакует нового монстра
fighter.change_weapon(bow)
battle(fighter, monster2)
