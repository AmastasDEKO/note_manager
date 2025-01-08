"""
3. display_notes_function.py: Функция отображения заметок
Функциональность:
Функция display_notes(notes) принимает список заметок.
Выводит каждую заметку в удобном формате.
Обрабатывает пустые списки заметок.
"""

# Подключение библиотек datetime, prettytable, colorama
from datetime import datetime
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)

# Создание списка с заметками
notes1 = [{
        "username":"анна",
        "titles":["дом", "пылесос"],
        "content":"купить домой пылесос",
        "status":"в процессе",
        "created_date":datetime(2025,1,2),
        "issue_date":datetime(2025,1,10)
        },
          {
        "username":"кристина",
        "titles":["любовь", "подарок"],
        "content":"выбрать подарок на 14 февраля",
        "status":"новая",
        "created_date":datetime.today(),
        "issue_date":datetime(2025,1,15)
        },
          {
        "username":"максим",
        "titles":["стиральная машина", "дом"],
        "content":"отремонтировать стиральную машину в доме бабушки",
        "status":"отложено",
        "created_date":datetime(2025,1,10),
        "issue_date":datetime(2025,1,25)
        },
          {
        "username":"анна",
        "titles":["машина", "поход"],
        "content":"загрузить машину инвентарем для похода в горы",
        "status":"выполнено",
        "created_date":datetime(2025,1,2),
        "issue_date":datetime(2025,1,20)
        },
          {
        "username":"анна",
        "titles":["рисование", "любовь"],
        "content":"написать сочинение об любви к рисованию",
        "status":"в процессе",
        "created_date":datetime(2025,1,6),
        "issue_date":datetime(2025,1,30)
        }]

# Создание пустого списка
notes2 = []

# Создание списка с одной заметкой
notes3 = [{
        "username":"костя",
        "titles":["код", "гит"],
        "content":"проверить код на гитхабе",
        "status":"в процессе",
        "created_date":datetime.today(),
        "issue_date":datetime(2025,1,12)
        }]

# Функция сортировки выборкой
def sort_by_date(_notes, name_date):
    # Перебор заметок в списке
    for i in range(len(_notes)):
        # Перемещаем i-ую заметку, дату и индекс в переменные
        note = _notes[i]
        nearest_date = note[name_date]
        index_nearest_date = i
        # Перебор заметок в списке начиная с i+1
        for j in range(i+1, len(_notes)):
            # Перемещаем j-ую заметку в переменную
            next_note = _notes[j]
            # Сравниваем даты
            if next_note[name_date] < nearest_date:
                # Меняем наименьшую дату и индекс
                nearest_date = next_note[name_date]
                index_nearest_date = j
        # Меняем i-тую заметку с наименьшей местами
        _notes[i], _notes[index_nearest_date] = _notes[index_nearest_date],_notes[i]

# Функция для вывода списка заметок
def display_notes(_notes):

    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
    # Создания словаря для фильтров вывода
    filter_choice = ("1","неполный вывод",
                     "2","сортировка по дате создания",
                     "3","сортировка по дате дедлайна",
                     "4","вывод в виде таблицы",
                     "5","без фильтров")
    # Проверка на наличие заметок
    if len(_notes) == 0:
        print("\nУ вас нет сохранённых заметок\n")
        return
    # Цикл вывода
    while True:
        # Выбор фильтра
        filter_display = input("Выберите фильтр для вывода:"
                               "\n1. Неполный вывод"
                               "\n2. Сортировка по дате создания"
                               "\n3. Сортировка по дате дедлайна"
                               "\n4. Вывод в виде таблицы"
                               "\n5. Без фильтров"
                               "\nВвод: ").strip().lower()
        # Неполный вывод
        if filter_display in filter_choice[:2]:
            print("Список заметок:")
            print("---------------")
            # Цикл вывода заметок из списка
            for i in range(len(_notes)):
                # Помещаем текущую заметку в переменную
                note = _notes[i]
                # Вывод данных заметки
                print(f"Заметка №{i + 1}")
                for key, value in note.items():
                    if key == "titles":
                            # Меняем цвет заголовков на яркий жёлтый
                        print(f"{note_print[key]}: {Fore.YELLOW+Style.BRIGHT+", ".join(value).title()}")
                else:
                    print("---------------")
            else:
                break
        # Сортировка по дате создания
        elif filter_display in filter_choice[2:4]:
            # Вызываем функцию сортировки
            sort_by_date(_notes, "created_date")
            print("Список заметок:")
            print("---------------")
            # Цикл вывода заметок из списка
            for i in range(len(_notes)):
                # Помещаем текущую заметку в переменную
                note = _notes[i]
                # Вывод данных заметки
                print(f"Заметка №{i + 1}")
                for key, value in note.items():
                    if key == "titles":
                        print(f"{note_print[key]}: {", ".join(value).title()}")
                    elif key == "created_date" or key == "issue_date":
                        splitting = str(value).split()
                        splitting = splitting[0].split(sep="-", maxsplit=-1)
                        if key == "created_date":
                            # Меняем цвет даты создания на зелёный
                            print(f"{note_print[key]}: {Fore.GREEN+'.'.join(splitting[:0:-1])}")
                        else:
                            print(f"{note_print[key]}: {'.'.join(splitting[:0:-1])}")
                    else:
                        print(f"{note_print[key]}: {value.capitalize()}")
                else:
                    print("---------------")
            else:
                break
        # Сортировка по дате дедлайна
        elif filter_display in filter_choice[4:6]:
            # Вызываем функцию сортировки
            sort_by_date(_notes, "issue_date")
            print("Список заметок:")
            print("---------------")
            # Цикл вывода заметок из списка
            for i in range(len(_notes)):
                # Помещаем текущую заметку в переменную
                note = _notes[i]
                # Вывод данных заметки
                print(f"Заметка №{i + 1}")
                for key, value in note.items():
                    if key == "titles":
                        print(f"{note_print[key]}: {", ".join(value).title()}")
                    elif key == "created_date" or key == "issue_date":
                        splitting = str(value).split()
                        splitting = splitting[0].split(sep="-", maxsplit=-1)
                        if key == "issue_date":
                            # Меняем цвет даты дедлайна на красный
                            print(f"{note_print[key]}: {Fore.RED+'.'.join(splitting[:0:-1])}")
                        else:
                            print(f"{note_print[key]}: {'.'.join(splitting[:0:-1])}")
                    else:
                        print(f"{note_print[key]}: {value.capitalize()}")
                else:
                    print("---------------")
            else:
                break
        # Вывод в виде таблицы
        elif filter_display in filter_choice[6:8]:
            note_table = PrettyTable()
            note_table.field_names = list(note_print.values())
            # Цикл добавления значений в таблицу
            for i in range(len(_notes)):
                # Помещаем текущую заметку в переменную
                note = _notes[i]
                # Список для значений заметки
                note_list = []
                # Цикл форматирования значений и добавления их в список
                for key, value in note.items():
                    if key == "titles":
                        note_list.append(", ".join(value).title())
                    elif key == "created_date" or key == "issue_date":
                        splitting = str(value).split()
                        splitting = splitting[0].split(sep="-", maxsplit=-1)
                        note_list.append('.'.join(splitting[:0:-1]))
                    else:
                        note_list.append(value.capitalize())
                # Добавление значений заметки в таблицу
                note_table.add_row(note_list)
            # Вывод таблицы
            print("Таблица заметок")
            print(note_table)
            break
        # Без фильтров
        elif filter_display in filter_choice[8:]:
            print("Список заметок:")
            print("---------------")
            # Цикл вывода заметок из списка
            for i in range(len(_notes)):
                # Помещаем текущую заметку в переменную
                note = _notes[i]
                # Вывод данных заметки
                print(f"Заметка №{i+1}")
                for key, value in note.items():
                    if key == "titles":
                        print(f"{note_print[key]}: {", ".join(value).title()}")
                    elif key == "created_date" or key == "issue_date":
                        splitting = str(value).split()
                        splitting = splitting[0].split(sep="-", maxsplit=-1)
                        print(f"{note_print[key]}: {'.'.join(splitting[:0:-1])}")
                    else:
                        print(f"{note_print[key]}: {value.capitalize()}")
                else:
                    print("---------------")
            else:
                break

        else:
            print("Ошибка ввода (Допустимо:1, 2, 3, 4, 5 или"
                  " Неполный вывод, Сортировка по дате создания,"
                  " Сортировка по дате дедлайна, Вывод в виде таблицы, Без фильтров")

#Вызов функции с разными списками
display_notes(notes1)
display_notes(notes2)
display_notes(notes3)
