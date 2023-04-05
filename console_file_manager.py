import os
import shutil
import sys

while True:
    print('1. создать папку')
    print('2. удалить(файл / папку)')
    print('3. копировать(файл / папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории(*необязательный пункт)')
    print('12. выход')


    choice = input('Выберите пункт меню: ')

    if choice == '1':
        new_folder = input('Введите имя создаваемой папки: ')
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

    elif choice == '2':
        del_folder = input('Введите имя удаляемой папки/файла: ')
        if del_folder in os.listdir():
            try:
                os.rmdir(del_folder)
            except:
                os.remove(del_folder)

    elif choice == '3':
        folder_from_copy = input('Введите имя копируемой папки/файла: ')
        folder_to_copy = input('Введите имя новой папки/файла: ')
        try:
            shutil.copytree(folder_from_copy, folder_to_copy)
        except:
            shutil.copyfile(folder_from_copy, folder_to_copy)

    elif choice == '4':
        print(os.listdir("."))

    elif choice == '5':
        for folder in os.listdir("."):
            if os.path.isdir(folder):
                print(folder)

    elif choice == '6':
        for filename in os.listdir("."):
            if os.path.isfile(filename):
                print(filename)

    elif choice == '7':
        print(sys.platform)

    elif choice == '8':
        print(os.getlogin())

    elif choice == '9':
        import victory

    elif choice == '10':
        import use_functions

    elif choice == '11':
        print(f'Текущая рабочая директория: {os.getcwd()}')
        new_dir = input('Введите путь к новой рабочей директории: ')
        os.chdir(new_dir)
        print(f'Новая рабочая директория: {os.getcwd()}')

    elif choice == '12':
        break

    else:
        print('Неверный пункт меню')