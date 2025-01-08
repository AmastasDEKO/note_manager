"""
1. create_note_function.py: Функция создания заметки
Функциональность:
Функция create_note() запрашивает данные у пользователя для создания заметки.
Формирует словарь с полями заметки, включая автоматическую генерацию текущей даты.
Проверяет корректность формата даты дедлайна.
"""

# Подключение формата даты
from datetime import datetime
# Функция вывода данных о заметке
def output_notes(note):
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дата истечения'
                  }

    for key, value in note.items():
        if key == "titles":
            print(f"{note_print[key]}:", ", ".join(value).title())
        elif key == "created_date" or key == "issue_date":
            splitting = str(value).split()
            splitting = splitting[0].split(sep="-", maxsplit=-1)
            print(f"{note_print[key]}:", '.'.join(splitting[:0:-1]))
        else:
            print(f"{note_print[key]}: {value.capitalize()}")

# Функция для создания заметок
def create_note():
    new_note = {}
    print("Введите информацию о новой заметке")
    # Ввод имени пользователя
    while True:
        username = input("Введите имя пользователя: ").strip().lower()
        # Проверка на пустой ввод
        if username != "":
            new_note.update({"username": username})
            break
        else:
            print("Пожалуйста заполните имя пользователя.")

            
    # Ввод заголовков
    titles_set = set()
    # Цикл ввода заголовков
    while True:
        title = input("Введите заголовок (для окончание введите \"стоп\" или ничего): ").strip().capitalize()
        # Проверка на окончание ввода или добавление заголовка в множество
        if title == "" or title == "Стоп":
            # Проверка на наличие заголовков
            if len(titles_set) != 0:
                titles = list(titles_set)
                new_note.update({"titles": titles})
                break
            else:
                print("Введите хотя бы один заголовок")
        else:
            titles_set.add(title)
            
    # Ввода описания
    while True:
        content = input("Введите описание заметки: ").strip().lower()
        # Проверка на пустой ввод
        if content != "":
            new_note.update({"content": content})
            break
        else:
            print("Пожалуйста заполните описание.")

    # Выбор статуса
    while True:
        # Словарь значений статуса
        choice_status = {"1": "выполнено",
                         "2": "в процессе",
                         "3": "новая"
                        }
        # Ввод нового статуса и проверка корректности ввода
        new_status = input(
            "Введите статус:\n1. Выполнено\n2. В процессе\n3. Новая\nВвод: ").strip().lower()
        # Проверка по ключу(цифре)
        if new_status in choice_status.keys():
            # Сохранение статуса
             new_note.update({"status": choice_status[new_status]})
             break
        # Проверка по значению(словам)
        elif new_status in choice_status.values():
              # Сохранение статуса
              new_note.update({"status": new_status})
              break
        else:
            # Обработка ошибки ввода
            print("Ошибка ввода (Допустимо: 1, 2, 3 или Выполнено, В процессе, Новая)")

    # Дата создания
    new_note.update({"created_date":datetime.today()})
            
    # Ввод дедлайна
    while True:
        # Запрос на автоматический ввод дедлайна через неделю.
        auto_date = input("Хотите автоматически поставить дедлайн"
                          " на следующую неделю (Да/Нет)?\nВвод: ").strip().lower()
        if auto_date == "да":
            # Отдельная переменная для "сегодня"
            today = datetime.today()
            try:
                new_note.update({"issue_date":datetime.replace(today,today.year,today.month,today.day+7)})
            # Ловим исключения если дедлайн будет в следующем месяце
            except ValueError:
                # Для месяцев с 30 днями
                if (today.day + 7) > 30:
                    new_note.update({"issue_date":
                         datetime.replace(today, today.year, today.month + 1, 31 - (today.day + 7))
                        })
                # Для месяцев с 31 днем
                elif (today.day+ 7) > 31:
                    new_note.update({"issue_date":
                                     datetime.replace(today, today.year, today.month+1, 31 - (today.day + 7))
                                    })
                # Для февраля
                elif (today.day+ 7) > 28:
                    new_note.update({"issue_date":
                                     datetime.replace(today, today.year, today.month+1, 28 - (today.day + 7))
                                    })
                # Для февраля (в високосный год)
                elif (today.day+ 7) > 29:
                    new_note.update({"issue_date":
                                     datetime.replace(today, today.year, today.month+1, 29 - (today.day + 7))
                                    })
            break
        elif auto_date == "нет":
            while True:
                issue_date_input = input("Введите дату дедлайн в формате (день.месяц.год): "
                                        ).split(sep=".",maxsplit=-1)
                try:
                    # Приведение года в формат "20__"
                    if len(issue_date_input[2]) == 2:
                        issue_date_input[2] = "20" + issue_date_input[2]

                    # Добавление в словарь с преобразованием списка в дату
                    new_note.update({"issue_date": datetime(
                        int(issue_date_input[2]),
                        int(issue_date_input[1]),
                        int(issue_date_input[0]))
                    })
                    # Возвращаем словарь
                    break
                # Ловим исключения по значению и формату
                except IndexError:
                    print("Ошибка формата: Дата введена не день.месяц.год")

                except ValueError:
                    print("Ошибка значения: Были использованы не цифры или неверный формат дня, месяца, года")
            break
        else:
            print("Ошибка ввода. (Допустимо: да, нет)")

    return new_note

# Вызов функций
output_notes(create_note())


