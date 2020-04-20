__author__ = "Joseph Rossitto"

import random

from B_Logic.gamedemo.player import Player
from B_Logic.gamedemo.weapons import Weapon, Sword, FireBreath

class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def run(self):
        print(self.p1)
        print(self.p2)
        while self.p1.isAlive and self.p2.isAlive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.attack()
            print(attacker.name, "attacks:", sound)
            print(attacker.name, "did", dmg, "damage")
            defender.takeHit(dmg)
        print(attacker.name, "won with", attacker.health, "health left")


if __name__ == "__main__":
    random.seed()
    g = Game(Player("The Knight", Sword(), 100), Player("The Dragon", FireBreath(), 500))
    g.run()
