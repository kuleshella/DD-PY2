import doctest
from typing import Union


class Baby:
    def __init__(self, age: Union[float, int], weight: Union[float, int], name: str):
        """
        :param age: возраст ребёнка в годах
        :param weight: вес вес ребёнка в килограммах
        :param name: имя ребёнка

        Примеры:
        >>> artem = Baby(.5, 8, 'Артём')  # инициализация экземпляра класса
        >>> andrey = Baby(23, 80, 'Андрей')  # инициализация экземпляра класса
        """
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа float или int")
        if age < 0:
            raise ValueError("Возраст должен быть не отрицательным")
        self.age = age

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес ребёнка должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес ребёнка должен быть положительным")
        self.weight = weight

        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой!")
        if not name:
            raise ValueError("Имя должно быть как минимум из одного симвала")
        self.name = name

    def eat(self, food_weight: float) -> float:
        """
        Поедание еды.

        :param food_weight: вес доступной еды в килограммах
        :raise ValueError: некорректное значение параметра

        :return: веc реально сьеденой еды в килограммах
        Примеры:
        >>> baby = Baby(.5, 8, 'Артём')
        >>> baby.eat(.2)
        """
        ...

    def cry(self):
        """
        Плакать, звать родителей.

        Примеры:
        >>> baby = Baby(.5, 8, 'Артём')
        >>> baby.cry()
        """
        ...


class Sofa:
    def __init__(self, condition: Union[float, int], folded: bool = True):
        """
        :param condition: состояние дивана [0:1], где 0 - непригоден для использования, а 1 - новый.
        :param folded: сложен ли диван.

        Примеры:
        >>> old_sofa = Sofa(.4, False)  # инициализация экземпляра класса
        >>> new_sofa = Sofa(1)  # инициализация экземпляра класса
        """
        if not isinstance(condition, (float, int)):
            raise TypeError("Состояние дивана должно быть типа float или int")
        if condition < 0:
            raise ValueError("Состояние должно быть положительным")
        if condition > 1:
            raise ValueError("Состояние должно быть не более 1")
        self.condition = condition

        if not isinstance(folded, bool):
            raise TypeError("Сложен ли диван это bool!")
        self.folded = folded

    def fold(self) -> None:
        """
        Диван складываеся.

        Примеры:
        >>> sofa = Sofa(.8)  # инициализация экземпляра класса
        >>> sofa.fold()
        """
        ...

    def put_in_box(self, thing) -> None:
        """
        В ящик дивана кладётся вещ.

        :param thing: вещ, которая кладётся в диван

        Примеры:
        >>> sofa = Sofa(.8)  # инициализация экземпляра класса
        >>> sofa.put_in_box(Baby(.5, 8, 'Артём'))
        """
        ...

    def fix(self) -> float:
        """
        Починка дивана.

        :return: какое состояние у дивана после починки

        Примеры:
        >>> sofa = Sofa(.8)  # инициализация экземпляра класса
        >>> sofa.fix()
        """
        ...


class Cat:
    def __init__(self, weight: Union[float, int], name: str):
        """
        :param weight: Вес кота
        :param name: Кличка кота

        Примеры:
        >>> gavr = Cat(5, 'Gavroid')  # инициализация экземпляра класса
        >>> salamon = Cat(.5, 'Great Salamon 2022')  # инициализация экземпляра класса
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кота должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес кота должен быть положительным числом")
        self.weight = weight

        if not isinstance(name, str):
            raise TypeError("Кличка кота должна быть строкой!")
        if not name:
            raise ValueError("Кличка кота должна быть как минимум из одного симвала")
        self.name = name

    def tear_up_the_sofa(self, sofa: Sofa) -> bool:
        """
        Побуждает кота разодрать диван.

        :param sofa: диван для заточки когтей
        :raise ValueError: некорректное значение параметра sofa

        :return: привлекло ли действие внимание хозяина

        Примеры:
        >>> gavr = Cat(5, 'Gavroid')
        >>> sofa = Sofa(1, True)
        >>> gavr.tear_up_the_sofa(sofa)
        """
        ...

    def hide_in_box(self) -> None:
        """
        Прячет кота в ближайшую коробку или ящик.

        Примеры:
        >>> gavr = Cat(5, 'Gavroid')
        >>> gavr.hide_in_box()
        """
        ...

    def eat(self, food_weight: float) -> float:
        """
        Кот поедает корм.

        :param food_weight: вес доступной еды в килограммах
        :raise ValueError: некорректное значение параметра food_weight

        :return: веc реально сьеденой еды в килограммах

        Примеры:
        >>> gavr = Cat(5, 'Gavroid')
        >>> gavr.eat(.1)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()   # тестирование примеров, которые находятся в документации
