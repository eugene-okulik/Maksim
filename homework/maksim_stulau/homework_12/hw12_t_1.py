"""Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
Создать экземпляры (объекты) цветов разных видов.
Собрать букет (букет - еще один класс) с определением его стоимости.
В букете цветы пусть хранятся в списке. Это будет список объектов.

Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость)(это тоже методы)

Реализовать поиск цветов в букете по каким-нибудь параметрам
(например, по среднему времени жизни) (и это тоже метод)."""


class Flowers:
    shop = "On the corner"

    def __init__(self, price, evg_time):
        self.price = price
        self.evg_time = evg_time


class FlType1(Flowers):
    height = "40 sm"


class FlType2(Flowers):
    height = "25 sm"


class FlType3(Flowers):
    height = "15 sm"


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def wilting_time(self):
        total_time = sum(flower.evg_time for flower in self.flowers)
        return total_time / len(self.flowers) if len(self.flowers) > 0 else 0

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.evg_time, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.price)

    def sort_by_length(self):
        self.flowers.sort(key=lambda x: x.height)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def find_by_wilting_time(self, target_time):
        return [flower for flower in self.flowers if flower.evg_time == target_time]


white_rose = FlType1(20, 5)
red_rose = FlType1(18, 5)
tulip = FlType2(7, 6)
lily = FlType3(15, 7)

flowers_in_bouquet = [white_rose, red_rose, tulip, lily]
bouquet = Bouquet(flowers_in_bouquet)

print("Время увядания букета:", bouquet.wilting_time())
bouquet.sort_by_freshness()
print("Букет после сортировки по свежести:", [flower.evg_time for flower in bouquet.flowers])
bouquet.sort_by_color()
print("Букет после сортировки по цвету:", [flower.price for flower in bouquet.flowers])
bouquet.sort_by_length()
print("Букет после сортировки по длине стебля:", [flower.height for flower in bouquet.flowers])
bouquet.sort_by_price()
print("Букет после сортировки по стоимости:", [flower.price for flower in bouquet.flowers])

target_wilting_time = 6
found_flowers = bouquet.find_by_wilting_time(target_wilting_time)
print(f"Цветы с временем увядания {target_wilting_time}:", [flower.price for flower in found_flowers])
