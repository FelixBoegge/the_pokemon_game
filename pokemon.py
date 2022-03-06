import csv


# create a Pokemon
class Pokemon:
    all = []

    def __init__(self, num: int, name: str, type: str, max_hp: int, dam: int, status: str):
        assert max_hp >= 0, f"Max Health {max_hp} must be positive!"
        assert type in {"fire", "water", "grass", "electric", "rock"}, "Invalid Pokemon-Type!"
        assert status in {"active", "KO", "Invalid Status! (Must be 'active' or 'KO')"}
        assert dam >= 0, f"Attack value {dam} must be positive!"

        self.num = num
        self.name = name
        if type == "fire":
            self.type = "\033[0;31mfire\033[0;0m"
        if type == "water":
            self.type = "\033[0;34mwater\033[0;0m"
        if type == "grass":
            self.type = "\033[0;32mgrass\033[0;0m"
        if type == "electric":
            self.type = "\033[0;33melectric\033[0;0m"
        if type == "rock":
            self.type = "\033[0;35mrock\033[0;0m"
        self.hp = max_hp
        self.max_hp = max_hp
        self.dam = dam
        self.status = status

        Pokemon.all.append(self)

    def __str__(self):
        a = (str(self.num)).rjust(2)
        b = (self.name).ljust(11)
        c = (self.type).ljust(22)
        d1 = ((self.max_hp - self.hp) * u"\u25a1" + self.hp * u"\u25a0").rjust(12)
        d2 = (str(self.hp) + "/" + str(self.max_hp) + "HP").rjust(8)
        e = (str(self.dam)).rjust(2)
        if self.status == 'active':
            f = f"\033[0;32m{self.status}\033[0;0m".rjust(19)
        elif self.status == 'KO':
            f = f"\033[0;31m{self.status}\033[0;0m".rjust(19)
        return f"#{a} {b}{c}{d1}{d2} Damage: {e} Status: {f}"

    # Read Pokemon-Data from file to create them
    @classmethod
    def instantiate_from_csv(cls):
        with open('Pokemonlist.csv', 'r') as f:
            reader = csv.DictReader(f)
            pokemons = list(reader)

        for pokemon in pokemons:
            Pokemon(
                int(pokemon.get('num')),
                pokemon.get('name'),
                pokemon.get('type'),
                int(pokemon.get('max_hp')),
                int(pokemon.get('dam')),
                pokemon.get('status')
            )

    # Give Pokemon a Healthpotion to increase HP
    def heal(self, name, add, width):
        print(width * "\033[0;34m-\033[0;0m")
        if self.max_hp - self.hp >= add:
            print(f"{name} is giving a Healthpotion to {self.name} (\033[0;33m+{add}HP\033[0;0m)")
            self.hp += add
        else:
            print(
                f"{name} is giving a Healthpotion to {self.name} (\033[0;33m+{self.max_hp - self.hp}HP\033[0;0m)")
            self.hp = self.max_hp
        print(f"{self.name} now has {self.hp}HP")

    # Train Pokemon to increase Damage
    def train(self, name, add, width):
        print(width * "\033[0;34;40m-\033[0;37;40m")
        print(f"{name} is training {self.name} (\033[0;33m+{add} Damage\033[0;0m)")
        self.dam += add
        print(f"{self.name} now deals {self.dam} Damage")

    # Let the Fight
    def battle(self, other, width):
        a = (self.name + " " + str(self.hp) + "/" + str(self.max_hp) + "HP (" + str(self.dam) + " Damage)").ljust(28)
        b = ("\033[0;31mVS\033[0;0m").center(width + 13 - (2 * 28))
        c = (other.name + " " + str(other.hp) + "/" + str(other.max_hp) + "HP (" + str(other.dam) + " Damage)").rjust(
            28)
        print("\n\n" + a + b + c + "\n" + width * "\033[0;34m-\033[0;0m")
        result = self.typewheel(self.type, other.type)

        if result == "ad":
            self.hp -= other.dam
            other.hp -= 2 * self.dam
            print(f"{self.name} ({self.type}) had Advantage over {other.name} ({other.type})")
            print(f"{self.name} delt \033[0;33m{2 * self.dam} Damage\033[0;0m")
            print(f"{other.name} delt \033[0;33m{other.dam} Damage\033[0;0m")
        elif result == "disad":
            self.hp -= 2 * other.dam
            other.hp -= self.dam
            print(f"{self.name} ({self.type}) had Disadvantage over {other.name} ({other.type})")
            print(f"{self.name} delt \033[0;33m{self.dam} Damage\033[0;0m")
            print(f"{other.name} delt \033[0;33m{2 * other.dam} Damage\033[0;0m")
        elif result == "tie":
            self.hp -= other.dam
            other.hp -= self.dam
            print(f"{self.name} and {other.name} have the same Type: {self.type}")
            print(f"{self.name} delt \033[0;33m{self.dam} Damage\033[0;0m")
            print(f"{other.name} delt \033[0;33m{other.dam} Damage\033[0;0m")

        if self.hp <= 0 and other.hp > 0:
            print(f"{self.name} went \033[0;31mKO\033[0;0m")
            self.status = "KO"
            self.hp = 0
            print(f"{other.name} now has {other.hp}/{other.max_hp}HP")
        elif self.hp > 0 and other.hp <= 0:
            print(f"{self.name} now has {self.hp}/{self.max_hp}HP")
            print(f"{other.name} went \033[0;31mKO\033[0;0m")
            other.status = "KO"
            other.hp = 0
        elif self.hp <= 0 and other.hp <= 0:
            print(f"{self.name} went \033[0;31mKO\033[0;0m")
            self.status = "KO"
            self.hp = 0
            print(f"{other.name} went \033[0;31mKO\033[0;0m")
            other.status = "KO"
            other.hp = 0
        else:
            print(f"{self.name} now has {self.hp}/{self.max_hp}HP")
            print(f"{other.name} now has {other.hp}/{other.max_hp}HP")

    # Defines which Pokemon-Type has Advantage over which Pokemon-Type
    @staticmethod
    def typewheel(type1, type2):
        result = {0: "tie", 1: "ad", -1: "disad"}
        # mapping between types and result conditions
        game_map = {"\033[0;31mfire\033[0;0m": 0,
                    "\033[0;34mwater\033[0;0m": 1,
                    "\033[0;32mgrass\033[0;0m": 2,
                    "\033[0;33melectric\033[0;0m": 3,
                    "\033[0;35mrock\033[0;0m": 4}
        # implement win-lose matrix
        ad_matrix = [
            [0, -1, 1, 1, -1],  # fire
            [1, 0, -1, -1, 1],  # water
            [-1, 1, 0, -1, 1],  # grass
            [-1, 1, 1, 0, -1],  # elctric
            [1, -1, -1, 1, 0]  # rock
        ]
        # declare a winner
        return result[
            ad_matrix[game_map[type1]][game_map[type2]]
        ]
