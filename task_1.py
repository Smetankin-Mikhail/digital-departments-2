import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Plant:
    """Класс, описывающий растение."""

    def __init__(self, name: str, species: str, count: int):
        """Инициализация растения.

        :param name: Название растения.
        :param species: Вид растения.
        :param count: Количество растений.

        >>> rose = Plant("Роза", "Роза садовая", 3)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть 'str'")
        if not isinstance(species, str):
            raise TypeError("Вид должен быть 'str'")
        if not isinstance(count, int):
            raise TypeError("Количество должно быть целым числом")

        self.name = name
        self.species = species
        self.count = count

    def grow(self):
        """Рост растения."""
        ...

    def reproduce(self):
        """Размножение растения."""
        ...


class HouseholdAppliance:
    """Класс, описывающий бытовое устройство."""

    def __init__(self, name: str, brand: str, power_source: str):
        """Инициализация бытового устройства.

        :param name: Название бытового устройства.
        :param brand: Марка бытового устройства.
        :param power_source: Источник питания бытового устройства.

        >>> fridge = HouseholdAppliance("Холодильник", "Samsung", "Электричество")
        """

        if not isinstance(name, str):
            raise TypeError("Название должно быть 'str'")
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть 'str'")
        if not isinstance(power_source, str):
            raise TypeError("Источник питания должен быть 'str'")

        self.name = name
        self.brand = brand
        self.power_source = power_source

    def turn_on(self):
        """Включение бытового устройства."""
        ...

    def turn_off(self):
        """Выключение бытового устройства."""
        ...


class MagicalCreature:
    """Класс, описывающий магическое существо."""

    def __init__(self, name: str, species: str):
        """Инициализация магического существа.

        :param name: Имя существа.
        :param species: Вид существа.
        >>> dragon = MagicalCreature("Дракон", "Водяной дракон")
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно быть 'str'")
        if not isinstance(species, str):
            raise TypeError("Вид должен быть 'str'")

        self.name = name
        self.species = species

    def cast_spell(self, spell: str):
        """Произнести заклинание с использованием магических способностей существа.

        :param spell: Заклинание, которое нужно произнести.
        """
        ...

    def teleport(self, destination: str):
        """Телепортироваться в указанное место.

        :param destination: Место, куда нужно телепортироваться.
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
