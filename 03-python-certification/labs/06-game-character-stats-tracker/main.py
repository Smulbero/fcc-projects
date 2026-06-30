class GameCharacter():
    costants = {
        'MIN_HEALTH': 0,
        'MAX_HEALTH': 100,
        'MIN_MANA': 0,
        'MAX_MANA': 50,
    }

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, v):
        if v < 0:
            self._health = GameCharacter.costants['MIN_HEALTH']
        elif v > 100:
            self._health = GameCharacter.costants['MAX_HEALTH']
        else:
            self._health = v

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, v):
        if v < 0:
            self._mana = GameCharacter.costants['MIN_MANA']
        elif v > 50:
            self._mana = GameCharacter.costants['MAX_MANA']
        else:
            self._mana = v

    @property
    def level(self):
        return self._level
    
    def level_up(self):
        # Class constants do no work here for the tests.
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self.name} leveled up to {self.level}!')

    def __str__(self):
        return(f'''Name: {self.name}
Level: {self.level}
Health: {self.health}
Mana: {self.mana}''')
    
hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats