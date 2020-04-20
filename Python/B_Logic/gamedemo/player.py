__author__ = "Joseph Rossitto"

from B_Logic.gamedemo.weapons import Weapon

class Player:
    def __init__(self, name: str, weapon: Weapon, health: int):
        """
        Create the Player Character
        :param name: The Players Name
        :param weapon: The Players Weapon
        """
        self.name = name
        self.weapon = weapon
        self.health = 100

    def takeHit(self, damage: int) -> int:
        """
        A player takes a hit from a source
        :param damage: How much damage is taken
        :return: How much health is left after
        """
        self.health -= damage
        return self.health

    @property
    def isAlive(self) -> bool:
        """
        Check if the player is alive
        :return: Returns true if the player is alive
        """
        return self.health > 0

    def __str__(self) -> str:
        return "Player {} has {} health and brings his {} to fight".format(self.name, self.health, self.weapon)
