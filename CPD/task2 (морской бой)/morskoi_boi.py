from random import randint, choice

class Ship:
    def __init__(self, length: int, tp=1, x=None, y=None) -> None:
        self._length = length  # Длина корабля
        self._tp = tp  # Направление: 1 - горизонтально, 2 - вертикально
        self._x = x  # Начальные координаты по x
        self._y = y  # Начальные координаты по y
        self._is_move = True  # Может ли корабль двигаться
        self._cells = [1] * length  # Состояние ячеек корабля: 1 - здоров, 2 - повреждён

    def set_start_coords(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_start_coords(self) -> tuple:
        return self._x, self._y

    def move(self, go: int):
        """Движение корабля по полю: go - на сколько клеток сдвигаться"""
        if self._is_move:
            if self._tp == 1:
                self._x += go  # Горизонтальное перемещение
            elif self._tp == 2:
                self._y += go  # Вертикальное перемещение

    def is_collide(self, ship):
        """Проверка столкновений с другим кораблём"""
        if self._x is None or self._y is None or ship._x is None or ship._y is None:
            return False  # Если координаты не заданы, столкновения быть не может

        # Зоны обоих кораблей
        ship_zone = self.get_z(ship._x, ship._y, ship._tp, ship._length, 10)
        self_zone = self.get_self_zone(self._x, self._y, self._tp, self._length)

        for coord in self_zone:
            if coord in ship_zone:
                return True
        return False

    def is_out_pole(self, size: int) -> bool:
        """Проверка, выходит ли корабль за пределы игрового поля"""
        if self._tp == 1:
            return (self._x + self._length) > size
        else:
            return (self._y + self._length) > size

    def get_z(self, x: int, y: int, tp: int, length: int, size: int) -> list:
        """Зона вокруг корабля для проверки столкновений"""
        zone = []
        if tp == 1:
            zone = [[i, j] for i in range(x - 1, x + length + 1) if 0 <= i < size for j in range(y - 1, y + 2) if 0 <= j < size]
        elif tp == 2:
            zone = [[i, j] for i in range(x - 1, x + 2) if 0 <= i < size for j in range(y - 1, y + length + 1) if 0 <= j < size]
        return zone

    def get_self_zone(self, x: int, y: int, tp=None, length=None) -> list:
        """Зона, занимаемая самим кораблем"""
        if tp == 1:
            return [[i, y] for i in range(x, x + length)]
        else:
            return [[x, i] for i in range(y, y + length)]

    def make_position(self) -> dict:
        """Создание позиции корабля на поле"""
        position = {}
        if self._tp == 1:
            for i in range(self._length):
                position[i] = (self._x + i, self._y, self._cells[i])
        else:
            for i in range(self._length):
                position[i] = (self._x, self._y + i, self._cells[i])
        return position

    @property
    def tp(self):
        return self._tp

    @property
    def length(self):
        return self._length

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, item, value):
        self._cells[item] = value
class GamePole:
    def __init__(self, pole_size: int) -> None:
        self._size = pole_size
        self._ships = []
        self._spaced_ships = []
        self._pole = [[0 for i in range(self._size)] for i in range(self._size)]

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]
        starting_ships = self._ships[0] # Установка первого корабля
        while True:
            x = randint(0, self._size - 1)
            y = randint(0, self._size - 1)
            starting_ships.set_start_coords(x, y)
            if not starting_ships.is_out_pole(self._size):
                self._spaced_ships.append(starting_ships)
                break

        for i in range(1, len(self._ships)): # Установка остальных кораблей
            ship = self._ships[i]
            while True:
                sz = self._size - 1
                x = randint(0, sz)
                y = randint(0, sz)
                ship.set_start_coords(x, y)
                count = 0
                for spaced_ship in self._spaced_ships:
                    if not ship.is_collide(spaced_ship):
                        count += 1
                if (not ship.is_out_pole(self._size)) and (count == len(self._spaced_ships)):
                    self._spaced_ships.append(ship)
                    break
        self.make_pole()

    def get_ships(self):
        return self._ships

    def update_pole(self): # Функция обновления поля
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = self.get_random_cords(ship) if ship._x == ship._y is None else ship.get_start_coords()
            if ship.tp == 1:
                for index, i in enumerate(range(x, x + ship.length)):
                    self._pole[y][i] = ship._cells[index]
            elif ship.tp == 2:
                for index, i in enumerate(range(y, y + ship.length)):
                    self._pole[i][x] = ship._cells[index]
            ship.set_start_coords(x, y)

    def show(self):
        self.update_pole()
        for row in self._pole:
            print(" ".join([str(v) for v in row]))

    def secret_show(self):
        self.update_pole()
        for row in self._pole:
            for v in row:
                if v != 2:
                    print("#", end=" ")
                else:
                    print(str(v), end=" ")
            print("\n", end="")

    def get_pole(self):
        return tuple(tuple(i) for i in self._pole)

    def make_pole(self):
        for ship in self._ships:
            for index, data in ship.make_position().items():
                self._pole[data[0]][data[1]] = data[2]

    def move_check(self, ship, go): # Проверка возможности движения корабля
        x, y = ship.get_start_coords()
        if ship.tp == 1:
            zone = ship.get_z(x + go, y, ship.tp, ship.length, self._size)
            if go == 1:
                check_length = x + go + ship.length
            else:
                check_length = x + go - 1
            for x_z, y_z in zone:
                if self._pole[y_z][x_z] != 0 and x_z == check_length:
                    return False

            if x + go < 0 or x + go + ship.length > self._size:
                return False

        elif ship.tp == 2:
            zone = ship.get_z(x, y + go, ship.tp, ship.length, self._size)
            if go == 1:
                check_lenght = y + go + ship.length
            else:
                check_lenght = y + go - 1
            for x_z, y_z in zone:
                if self._pole[y_z][x_z] != 0 and y_z == check_lenght:
                    return False

            if y + go < 0 or y + go + ship.length > self._size:
                return False
        return True

    def move_ships(self) -> None: # Движение кораблей
        for ship in self._ships:
            go = choice([-1, 1])
            flag = self.move_check(ship, go)
            if flag:
                ship.move(go)
                self.update_pole()
            else:
                flag = self.move_check(ship, -go)
                if flag:
                    ship.move(-go)
                    self.update_pole()
        self._attacked = []


class GameService:
    def __init__(self, size) -> None:
        self.player_pole = GamePole(size)
        self.ii_pole = GamePole(size)

    def player_attack(self, x, y): # Атака игрока
        for ship in self.ii_pole.get_ships():
            if [x, y] in ship.get_self_zone(ship._x, ship._y, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("Игрок: Попадание")
                    break
                if ship._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("Игрок: Попадание")
                    break
        else:
            print("Игрок: Нет попадания")

    def ii_attack(self): # Атака ИИ
        x = randint(0, self.player_pole._size)
        y = randint(0, self.player_pole._size)
        print("Ход противника",x,y)
        for ship in self.player_pole.get_ships():
            if [x, y] in ship.get_self_zone(ship._x, ship._y, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("ИИ: Попадание")
                    break
                if ship._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("ИИ: Попадание")
                    break
        else:
            print("ИИ: Нет попадания")

    def run(self): # Запуск игры
        self.player_pole.init()
        self.ii_pole.init()
        while True:
            print("****** Поле игрока ******")
            self.player_pole.show()
            print("****** Поле ИИ ******")
            self.ii_pole.secret_show()
            x, y = input("Введите х и у чтобы выбрать координаты выстрела").split(' ')
            self.player_attack(int(x), int(y))
            self.ii_attack()
            self.player_pole.move_ships()
            self.ii_pole.move_ships()

if __name__ == "__main__":
    game = GameService(10)
    game.run()
