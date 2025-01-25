"""
5. menu.py: Меню действий
Функциональность:
Выводит интерактивное меню для выбора действий.
Обрабатывает выбор пользователя и вызывает соответствующую функцию.
Повторяет показ меню до тех пор, пока пользователь не выберет выход.
"""
# Импорт библиотек datetime, colorama и функций заметки
from datetime import datetime
from colorama import init, Fore
from utils.create_note_function import create_note
from utils.update_note_function import update_note
from interface.display_notes_function import display_notes
from utils.delete_note import delete_notes
from utils.search_notes_function import search_notes
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Создание списка заметок с содержимым
notes = [{
        "username": "анна",
        "titles": ["дом", "пылесос"],
        "content": "купить домой пылесос",
        "status": "в процессе",
        "created_date": datetime(2025, 1, 2),
        "issue_date": datetime(2025, 1, 10)
    },
        {
            "username": "кристина",
            "titles": ["любовь", "подарок"],
            "content": "выбрать подарок на 14 февраля",
            "status": "новая",
            "created_date": datetime.today(),
            "issue_date": datetime(2025, 1, 15)
        },
        {
            "username": "максим",
            "titles": ["стиральная машина", "дом"],
            "content": "отремонтировать стиральную машину в доме бабушки",
            "status": "отложено",
            "created_date": datetime(2025, 1, 10),
            "issue_date": datetime(2025, 1, 25)
        },
        {
            "username": "анна",
            "titles": ["машина", "поход"],
            "content": "загрузить машину инвентарем для похода в горы",
            "status": "выполнено",
            "created_date": datetime(2025, 1, 2),
            "issue_date": datetime(2025, 1, 20)
        },
        {
            "username": "анна",
            "titles": ["рисование", "любовь"],
            "content": "написать сочинение об любви к рисованию",
            "status": "в процессе",
            "created_date": datetime(2025, 1, 6),
            "issue_date": datetime(2025, 1, 30)
        }]

print("Приветствуем в \"Менеджере заметок\"")
# Кортеж значений
menu_tuple = ("1","создать новую заметку",
             "2","показать все заметки",
             "3","обновить заметку",
             "4","удалить заметку",
             "5","найти заметки",
             "6","выйти из программы")
# Цикл выбора действия
while True:
    # Запрос действия
    input_menu = input("Меню действий:"
                       "\n1. Создать новую заметку"
                       "\n2. Показать все заметки"
                       "\n3. Обновить заметку"
                       "\n4. Удалить заметку"
                       "\n5. Найти заметки"
                       "\n6. Выйти из программы"
                       "\nВаш выбор: ").strip().lower()
    # Создание заметки
    if input_menu in menu_tuple[:2]:
        notes.append(create_note())
    # Показ всех заметок
    elif input_menu in menu_tuple[2:4]:
        display_notes(notes)
    # Обновить заметку
    elif input_menu in menu_tuple[4:6]:
        if len(notes) == 0:
            print(Fore.BLUE+"У вас нет сохранённых заметок")
            continue
        while True:
            number_note = input(f"Введите номер заметки, если хотите выйти ничего не вводите: ").strip()
            if number_note == "":
                break
            elif int(number_note)<= len(notes):
                new_note = update_note(notes[int(number_note) - 1])
                notes[int(number_note)] = new_note
            else:
                print(Fore.BLUE+"Заметка не найдена")
    # Удалить заметку
    elif input_menu in menu_tuple[6:8]:
        notes = delete_notes(notes)
    # Найти заметку
    elif input_menu in menu_tuple[8:10]:
        # Кортеж критериев
        choice_tuple = ("1", "ключевое слово", "2", "статус", "3", "ключевое слово и статус")
        # Цикл выбора критерия
        while True:
            input_choice = input("Выберите критерий поиска:"
                                 "\n1. Ключевое слово"
                                 "\n2. Статус"
                                 "\n3. Ключевое слово и статус"
                                 "\nВвод: ").strip().lower()
            # Только ключевое слово
            if input_choice in choice_tuple[:2]:
                # Ввод ключевых слов
                input_keyword = input("Введите ключевые слова через пробел или оставьте поле пустым "
                                      "\n(Зона поиска: Имя пользователя, Заголовки, Описание)"
                                      "\nВвод: ").strip().lower()
                founded_notes = search_notes(notes, input_keyword.split())
                if len(founded_notes) == 0:
                    break
                else:
                    display_notes(founded_notes)
                break
            # Только статус
            elif input_choice in choice_tuple[2:4]:
                # Ввод статуса
                while True:
                    # Словарь значений статуса
                    choice_status = {"1": "выполнено",
                                     "2": "в процессе",
                                     "3": "новая",
                                     "4": "отложено"
                                     }
                    # Ввод нового статуса и проверка корректности ввода
                    _status = input(
                        "Введите статус или оставьте поле пустым:\n1. Выполнено\n2. В процессе\n3. Новая\n4. Отложено\nВвод: ").strip().lower()
                    # Проверка по ключу(цифре)
                    if _status in choice_status.keys():
                        # Сохранение статуса в переменную
                        input_status = choice_status[_status]
                        break
                    # Проверка по значению(словам)
                    elif _status in choice_status.values():
                        # Сохранение статуса переменную
                        input_status = _status
                        break
                    elif _status == "":
                        input_status = _status
                        break
                    else:
                        # Обработка ошибки ввода
                        print("Ошибка ввода (Допустимо: 1, 2, 3, 4 или Выполнено, В процессе, Новая, Отложено)")
                    # Вызов функций для 3 списков заметок
                founded_notes = search_notes(notes, status= input_status)
                if len(founded_notes) == 0:
                    break
                else:
                    display_notes(founded_notes)
                break
            # Ключевое слово и статус
            elif input_choice in choice_tuple[4:]:
                # Ввод ключевых слов
                input_keyword = input("Введите ключевые слова через пробел или оставьте поле пустым "
                                      "\n(Зона поиска: Имя пользователя, Заголовки, Описание)"
                                      "\nВвод: ").strip().lower()

                # Ввод статуса
                while True:
                    # Словарь значений статуса
                    choice_status = {"1": "выполнено",
                                     "2": "в процессе",
                                     "3": "новая",
                                     "4": "отложено"
                                     }
                    # Ввод нового статуса и проверка корректности ввода
                    _status = input(
                        "Введите статус или оставьте поле пустым:\n1. Выполнено\n2. В процессе\n3. Новая\n4. Отложено\nВвод: ").strip().lower()
                    # Проверка по ключу(цифре)
                    if _status in choice_status.keys():
                        # Сохранение статуса в переменную
                        input_status = choice_status[_status]
                        break
                    # Проверка по значению(словам)
                    elif _status in choice_status.values():
                        # Сохранение статуса переменную
                        input_status = _status
                        break
                    # Обработка ошибки ввода
                    else:
                        print("Ошибка ввода (Допустимо: 1, 2, 3, 4 или Выполнено, В процессе, Новая, Отложено)")
                founded_notes = search_notes(notes, input_keyword.split(), input_status)
                if len(founded_notes) == 0:
                    break
                else:
                    display_notes(founded_notes)
                break
            else:
                print(Fore.RED + "Ошибка ввода "
                                 "(Допустимо: 1, 2, 3, "
                                 "Ключевое слово, Статус, Ключевое слово и статус")
    # Выйти
    elif input_menu in menu_tuple[10:]:
        print("Программа завершена. Спасибо за использование!")
        break
    # Обработка ошибок ввода
    else:
        print(Fore.RED+"Ошибка ввода (Допустимо: порядковый номер действия или название действия)")
