import csv
import os.path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name[:10]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(num: str):
        """Статистический метод, возвращающий число из числа-строки"""
        try:
            return int(num)
        except ValueError:
            s = num.split('.')
            return int(s[0])

    @classmethod
    def instantiate_from_csv(cls, filepath = '../src/items.csv'):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""

        try:
            cls.all = []
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for line in reader:
                    item1 = (cls(line['name'], line['price'], line['quantity']))
                    cls.all.append(item1)
        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            return f"Отсутствует файл item.csv"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity + other.quantity)

class InstantiateCSVError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Файл item.csv поврежден'