class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(f'Имя героя: {self.name}')

    # не получилось вызвать этот метод, выдовало ошибку
    def health(self):
        return self.health_point * 2

    def __str__(self):
        return f'Прозвище: {self.nickname} \nСупер сила: {self.superpower}\nОчки здоровья: {self.health_point} \nКоронная фраза: {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('каска', 'черныш', 'женщина', 1000, 'любовь')
hero.print_name()
print(hero)
print(len(hero))


class Air(SuperHero):
    damage = 100
    fly = False

    def health(self):
        self.fly = True
        return self.health_point ** 2, self.fly

    def printTrue(self):
        print('True in the True_phrase')


class Earth(SuperHero):
    damage = 100
    fly = False

    def health(self):
        self.fly = True
        return self.health_point ** 2, self.fly

    def printTrue(self):
        print('True in the True_phrase')


hero2 = Air('Гатс', 'капитан три отряда', 'фехтование ', 2000, 'я хочу быть счастливым')
hero2.health()
hero2.print_name()
hero2.printTrue()
hero3 = Earth('Рыцарь черепа', '?', 'лошадь', 4000, 'смерть длани господней')
hero3.health()
hero3.print_name()
hero3.printTrue()
print(hero3)


class Villian(Air):
    people = 'monster'

    def gen_x(self): ...

    def crit(self):
        return print(self.damage ** 2)


vil1 = Villian('Грифит', 'Белый сокол', 'God', 40000, 'длань господня')
vil1.crit()

