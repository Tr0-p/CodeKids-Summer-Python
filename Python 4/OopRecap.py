"""
Name: Pokemon Backpack
Date: 29/04/2024
Author: Tom @ CODEKIDS
"""


class Pokemon:
    def __init__(self, name: str, hp: int, type: str):
        self._name = name
        self._hp = hp
        self._type = type
        self._attacks = {}

    def add_attack(self, attackName: str, attackDamage: int):
        self._attacks[attackName] = attackDamage

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def __str__(self):
        displayString = ''
        displayString += f'\nName: {self._name}'
        displayString += f'\nHP: {self._hp}'
        displayString += f'\nType: {self._type}'
        displayString += f'\nAttacks: | '

        for attack in self._attacks:
            displayString += attack + ' | '

        return displayString


if __name__ == '__main__':
    fuecoco = Pokemon('Fuecoco', 80, 'Fire')

    fuecoco.add_attack('Gnaw', 10)
    fuecoco.add_attack('Combustion', 50)

    print(fuecoco)