class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\t------ Frog World ------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug(),


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard encounters {obstacle} and {act}!'
        print(msg)


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class Priest:
    def __str__(self):
        return 'a good Priest'

    def action(self):
        return 'it heals you'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\t------ Wizard World ------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork(), Priest()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        for obs in self.obstacle:
            self.hero.interact_with(obs)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError:
        print(f'Age {age} is invalid, please try again...')
        return False, age
    return True, age


def main():
    name = ''
    while name.strip() == '':
        name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
