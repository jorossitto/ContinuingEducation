__author__ = "Joseph Rossitto"

from abc import ABC, abstractmethod
from typing import Tuple
import random



class Weapon(ABC):
    @abstractmethod
    def attack(self) -> Tuple[int, str]:
        """
        This method should return a tuple(damage, text) how much damage was dealt and what text to output
        """

class Sword(Weapon):
    def attack(self) -> Tuple[int, str]:

        return(random.choice([10,15]),
               random.choice(["Bam!", "Whack!", "Pow!"]))

class FireBreath(Weapon):
    def __init__(self) -> None:
        self._cooldown: int = 0

    def attack(self) -> Tuple[int, str]:
        if self._cooldown <=0:
            dmg: int
            sound: str
            dmg = random.choice([0,40])
            if dmg > 0:
                self._cooldown = 2
                sound = "Boom! Dragon fire!"
            else:
                sound = "The dragon produces only smoke.."
            return dmg, sound
        else:
            self._cooldown-=1
            return(0, "(waiting until it can breath fire again")
