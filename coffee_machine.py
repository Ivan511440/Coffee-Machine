# импортируем модуль time для задержки выполнения
import time

# определяем функцию для выбора типа кофе
def choose_coffee():
    while True:
        choice = input("Выберите тип кофе:\n1 - эспрессо\n2 - латте\n3 - капучино\n")
        if choice == "1":
            return "эспрессо"
        elif choice == "2":
            return "латте"
        elif choice == "3":
            return "капучино"
        else:
            print("Ошибка ввода, повторите попытку")

# определяем функцию для приготовления кофе
def make_coffee(coffee_type):
    print("Приготовление {}...".format(coffee_type))
    time.sleep(5)
    print("{} готов!".format(coffee_type))

# определяем функцию для добавления сахара
def add_sugar():
    while True:
        sugar = input("Хотите добавить сахар? (да/нет) ")
        if sugar == "да":
            print("Сахар добавлен!")
            return
        elif sugar == "нет":
            print("Сахар не добавлен")
            return
        else:
            print("Ошибка ввода, повторите попытку")

# определяем функцию для работы кофейной машины
def coffee_machine():
    print("Добро пожаловать! Что желаете выпить?")
    coffee_type = choose_coffee()
    make_coffee(coffee_type)
    add_sugar()
    print("Приятного кофепития!")

# запускаем работу кофейной машины
coffee_machine()