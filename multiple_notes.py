# Подключение формата даты
from datetime import datetime, date

# Создание списка для хранения заметок
notes = []

# Функция для ввода дедлайна
def input_deadline_date(note):
    issue_date_input = input("Введите дату дедлайн в формате (день.месяц.год): ").split(sep=".", maxsplit=-1)
    try:
        # Приведение года в формат "20__"
        if len(issue_date_input[2]) == 2:
            issue_date_input[2] = "20" + issue_date_input[2]

        # Добавление в словарь с преобразованием списка в дату
        note.update({"issue_date": date(
            int(issue_date_input[2]),
            int(issue_date_input[1]),
            int(issue_date_input[0]))
        })
        # Возвращаем словарь
        return note
    # Ловим исключения по значению и формату
    except IndexError:
        print("Ошибка формата: Дата введена не день.месяц.год")
        return input_deadline_date(note)
    except ValueError:
        print("Ошибка значения: Были использованы не цифры или неверный формат дня, месяца, года")
        return input_deadline_date(note)

# Функция для ввода даты создания
def input_created_date(note):
    created_date_input = input("Введите дату дедлайн в формате (день.месяц.год): ").split(sep=".", maxsplit=-1)
    # Ловим исключения по значению и формату
    try:
        # Приведение года в формат "20__"
        if len(created_date_input[2]) == 2:
            created_date_input[2] = "20" + created_date_input[2]

        # Добавление в словарь с преобразованием списка в дату
        note.update({"created_date": date(
            int(created_date_input[2]),
            int(created_date_input[1]),
            int(created_date_input[0]))
        })
        # Возвращаем словарь
        return note
    # Ловим исключения по значению и формату
    except IndexError:
        print("Ошибка формата: Дата введена не день.месяц.год")
        return input_created_date(note)
    except ValueError:
        print("Ошибка значения: Были использованы не цифры или неверный формат дня, месяца, года")
        return input_created_date(note)

# Функция для выбора статуса
def input_status(note):
    # Словарь значений статуса
    choice_status = {"1": "Выполнено",
                     "2": "В процессе",
                     "3": "Новая"
                     }
    # Ввод нового статуса и проверка корректности ввода
    new_status = input("Введите статус:\n1. Выполнено\n2. В процессе\n3. Отложено\nВвод: ").strip().capitalize()
    # Проверка по ключу(цифре)
    if new_status in choice_status.keys():
        # Сохранение статуса
        note.update({"status":choice_status[new_status]})
        return note
    # Проверка по значению(словам)
    elif new_status in choice_status.values():
        # Сохранение статуса
        note.update({"status":new_status})
        return note
    else:
        #Обработка ошибки ввода
        print("Ошибка ввода (Допустимо: 1, 2, 3 или Выполнено, В процессе, Отложено)")
        return input_status(note)

# Функция для ввода описания
def input_content(note):
    content = input("Введите описание заметки: ").strip().capitalize()
    # Проверка на пустой ввод
    if content == "":
        print("Пожалуйста заполните описание.")
        return input_content(note)
    note.update({"content":content})
    return note

# Функция для ввода заголовков
def input_titles(note):
    titles_set = set()
    # Цикл ввода заголовков
    while True:
        title = input("Введите заголовок (для окончание введите \"стоп\" или ничего): ").strip().capitalize()
        # Проверка на окончание ввода или добавление заголовка в множество
        if title == "" or title == "Стоп":
            # Проверка на наличие заголовков
            if len(titles_set) != 0:
                titles = list(titles_set)
                note.update({"titles": titles})
                break
            else:
                print("Введите хотя бы один заголовок")
        else:
            titles_set.add(title)
    return note

# Функция для ввода имени пользователя
def input_username(note):
    username = input("Введите имя пользователя: ").strip().capitalize()
    # Проверка на пустой ввод
    if username == "":
        print("Пожалуйста заполните имя пользователя.")
        return input_username(note)
    note.update({"username":username})
    return note

# Функция для вывода списка заметок
def output_notes(_notes):
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дата истечения'
                  }
    # Проверка на наличие заметок
    if len(_notes) == 0:
        print("Нет ни одной заметки")
        return 
    else:
        print("Список заметок:")
        # Цикл вывода заметок из списка
        for i in range(len(_notes)):
            # Помещаем текущую заметку в переменную
            note = _notes[i]
            # Вывод данных заметки
            print(f"\nЗаметка №{note["ID"]}")
            for key, value in note.items():
                if key == "titles":
                    print(f"{note_print[key]}:", ", ".join(value))
                elif key == "created_date" or key == "issue_date":
                    splitting = str(value).split(sep="-",maxsplit=-1)
                    print(f"{note_print[key]}:", '.'.join(splitting[:0:-1]))
                # Пропускаем ID
                elif key == "ID":
                    continue
                else:
                    print(f"{note_print[key]}: {value}")

# Функция для создания заметок
def can_give(_notes):
    # Запрос на добавление новой заметки
    give = input("Хотите добавить новую заметку? (Да/Нет)\nВвод: ").strip().capitalize()
    if give == "Да":
        new_note = {}
        # Добавление ID заметки
        new_note.update({"ID":len(_notes)+1})
        # Вызов функций ввода
        input_username(new_note)
        input_titles(new_note)
        input_content(new_note)
        input_status(new_note)
        input_created_date(new_note)
        input_deadline_date(new_note)
        # Добавление заметки в список
        _notes.append(new_note)
        return can_give(_notes)
    elif give == "Нет":
        output_notes(_notes)
    else:
        #Обработка ошибки ввода
        print("Ошибка ввода (Допустимо: Да, Нет)")
        return can_give(_notes)

# Вывод приветствия пользователя и запуск функции создания заметок
print("Приветствуем в Менеджере заметок!")
can_give(notes)