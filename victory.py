import random

celebrities = ['Мэрилин Монро', 'Криштиану Роналду', 'Пушкин', 'Колумб', 'Наполеон']
date = ['02.01.1926', '02.01.1985', '02.01.1799', '02.01.1451',  '02.01.1769']
answer = ['Второе января 1926 года', 'Второе января 1985 года', 'Второе января 1799 года',\
          'Второе января 1451 года', 'Второе января 1769 года']

while True:

    numbers = [0, 1, 2, 3, 4]
    result = random.sample(numbers, 2)
    print(result)

    answers = []
    for ind in result:
        ans_tmp = input(f'Назовите дату рождения {celebrities[ind]}: ')
        if ans_tmp != date[ind]:
            print(f'Верный ответ: {date[ind]}')
            answers.append(0)
        else:
            answers.append(1)

    print(f'Количество правильных ответов: {sum(answers)}')
    print(f'Количество неправильных ответов: {len(answers)-sum(answers)}')
    print(f'Процент правильных ответов: {sum(answers)*100/len(answers)}')
    print(f'Процент неправильных ответов: {(len(answers)-sum(answers))*100/len(answers)}')

    con = input('Вы хотите продолжить игру (Введите Да или Нет)?')
    if con=='Да':
        continue
    else:
        break