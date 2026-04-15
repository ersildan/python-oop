t = """
Задача 1
Создай пустой класс PiggyBank.
Создай один экземпляр этого класса и присвой его переменной money_box.

Задача 2
Создай пустой класс PiggyBank.
Создай два экземпляра:

money_box1 → атрибут coins = 10
money_box2 → атрибут coins = 13 и атрибут color = 'pink'

Задача 3
Создай класс PiggyBank, который имеет:
атрибут класса content = 'coins'
атрибут класса alternate_name = 'penny bank'

Затем создай один экземпляр класса и присвой его переменной money_box.
"""
# Задача 1
class PiggyBank:
    pass

money_box = PiggyBank()

# Задача 2
class PiggyBank2:
    pass

money_box1 = PiggyBank2()
money_box2 = PiggyBank2()

money_box1.coins = 10
money_box2.coins = 13
money_box2.color = 'pink'

# Задача 3
class PiggyBank3:
    content = 'coins'
    alternate_name = 'penny bank'

money_box3 = PiggyBank3()
