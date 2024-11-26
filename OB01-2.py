#Пример кода на Python для реализации классов `Tovar` и `Store` :


class Tovar:
    items = {}

    def __init__(self, name, type, ed, ves):
        self.name = name
        self.type = type  # "штучный" или "весовой"
        self.ed = ed  # "шт.", "кг" и т.д.
        self.ves = ves  # вес единицы товара или None

        # Добавляем товар и его цену в словарь items
        Tovar.items[name] = None  # Изначально цена будет None

    @classmethod
    def set_price(cls, name, price):
        if name in cls.items:
            cls.items[name] = price
        else:
            print(f"Товар {name} не найден.")

    @classmethod
    def get_price(cls, name):
        return cls.items.get(name, None)

# Создаем несколько товаров
apple = Tovar("Яблоки", "штучный", "шт.", 0.2)
banana = Tovar("Бананы", "штучный", "шт.", 0.15)
carrot = Tovar("Морковь", "весовой", "кг", None)
potato = Tovar("Картофель", "весовой", "кг", None)
milk = Tovar("Молоко", "весовой", "л", None)
bread = Tovar("Хлеб", "штучный", "шт.", 0.5)
cheese = Tovar("Сыр", "весовой", "кг", None)
chicken = Tovar("Курица", "весовой", "кг", None)
egg = Tovar("Яйцо", "штучный", "шт.", 0.05)
orange = Tovar("Апельсины", "весовой", "кг", None)

# Устанавливаем цены на товары
Tovar.set_price("Яблоки", 0.5)
Tovar.set_price("Бананы", 0.75)
Tovar.set_price("Морковь", 0.4)
Tovar.set_price("Картофель", 0.3)
Tovar.set_price("Молоко", 1.0)
Tovar.set_price("Хлеб", 0.6)
Tovar.set_price("Сыр", 2.0)
Tovar.set_price("Курица", 5.0)
Tovar.set_price("Яйцо", 0.1)
Tovar.set_price("Апельсины", 0.9)

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, tovar_name, price):
        self.items[tovar_name] = price

    def remove_item(self, tovar_name):
        if tovar_name in self.items:
            del self.items[tovar_name]
        else:
            print(f"Товар {tovar_name} не найден в ассортименте.")

    def get_price(self, tovar_name):
        return self.items.get(tovar_name, None)

    def update_price(self, tovar_name, new_price):
        if tovar_name in self.items:
            self.items[tovar_name] = new_price
        else:
            print(f"Товар {tovar_name} не найден в ассортименте.")

# Создаем несколько магазинов
store1 = Store("Магазин 1", "Улица 1")
store2 = Store("Магазин 2", "Улица 2")
store3 = Store("Магазин 3", "Улица 3")

#
#Добавляем товары в магазины
store1.add_item("Яблоки", Tovar.get_price("Яблоки"))
store1.add_item("Бананы", Tovar.get_price("Бананы"))
store1.add_item("Молоко", Tovar.get_price("Молоко"))
store1.add_item("Хлеб", Tovar.get_price("Хлеб"))
store1.add_item("Курица", Tovar.get_price("Курица"))
store3.add_item("Яйцо", Tovar.get_price("Яйцо"))

# Протестируем методы на примере store1
print("Цены в магазине 1:")
print(store1.items)

# Обновим цену на яблоки
store1.update_price("Яблоки", 0.6)
print("Обновленная цена на яблоки:", store1.get_price("Яблоки"))

# Уберем бананы из ассортимента
store1.remove_item("Бананы")
print("Ассортимент магазина 1 после удаления бананов:")
print(store1.items)

# Запросим цену на бананы
print("Цена на бананы:", store1.get_price("Бананы"))
#```

#В этом коде реализованы классы `Tovar` и `Store`, которые содержат необходимые атрибуты и методы. Созданы несколько товаров и магазинов, а также проведены тесты на методах класса `Store`.