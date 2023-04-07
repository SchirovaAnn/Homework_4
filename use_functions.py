"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

count = 0
with open('count.txt', 'w') as f:
    f.write(str(count))

history = []


def decorator(f):
    def inner(*args, **kwargs):
        print('Вы вносите изменения в счет!')
        result = f(*args, **kwargs)
        print('Значение счета изменилось!')
        return result
    return inner


@decorator
def add_count():
    with open('count.txt', 'r') as f:
        count = int(f.read())
    add_sum = int(input('Введите сумму пополнения счета: '))
    count += add_sum
    with open('count.txt', 'w') as f:
        f.write(str(count))
    return count

@decorator
def purchase():
    global count
    purchase_sum = int(input('Введите сумму покупки: '))
    if purchase_sum > count:
        print('Недостаточно денег на счете!')
        return count
    else:
        history.append((input('Введите название покупки: '), purchase_sum))
        with open('purchase.txt', 'w') as f:
            f.write(str(history))
        count -= purchase_sum
        return count


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        count = add_count()

    elif choice == '2':
        count = purchase()

    elif choice == '3':
        print(history)

    elif choice == '4':
        break

    else:
        print('Неверный пункт меню')
