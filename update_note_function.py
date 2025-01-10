"""
2. update_note_function.py: Функция обновления заметки
Функциональность:
Функция update_note(note) принимает заметку (словарь) как аргумент.
Позволяет пользователю выбрать поле для обновления.
Проверяет корректность ввода и обновляет выбранное поле.
"""

# Подключение формата даты и цвет текста
from datetime import datetime
from colorama import init, Fore
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция вывода данных о заметке
def output_note(_note):
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дата истечения'
                  }

    for key, value in _note.items():
        if key == "titles":
            print(f"{note_print[key]}:", ", ".join(value).title())
        elif key == "created_date" or key == "issue_date":
            splitting = str(value).split()
            splitting = splitting[0].split(sep="-", maxsplit=-1)
            print(f"{note_print[key]}:", '.'.join(splitting[:0:-1]))
        else:
            print(f"{note_print[key]}: {value.capitalize()}")

# Функция для изменения заметок
def update_note(_note):
    output_note(_note)
    # Кортеж с полями, которые можно изменить и выход
    choice_field = ("1","имя пользователя",
                    '2', "заголовки",
                    '3', "описание",
                    '4', "статус",
                    '5', 'дата истечения',
                    '6', 'выход'
                    )
    while True:
        # Ввод поля
        field = input("\nВыберите поле для изменения:"
                      "\n1. Имя пользователя"
                      "\n2. Заголовки"
                      "\n3. Описание"
                      "\n4. Статус"
                      "\n5. Дата истечения"
                      "\n6. Выход"
                      "\nВвод: ").strip().lower()
        # Изменение имени пользователя
        if field in choice_field[:2]:
            while True:
                last_choice = input("Вы точно хотите изменить имя пользователя?"
                                    " (Да/Нет)\nВвод: ").strip().lower()
                if last_choice == "да":
                    new_username = input("Введите новое имя пользователя"
                                         "(для отмены оставьте поле пустым): ").strip().lower()
                    # Проверка на пустой ввод
                    if new_username != "":
                        print(Fore.GREEN+"Имя пользователя изменено успешно")
                        _note["username"] = new_username
                        break
                    else:
                        print(Fore.BLUE+"Имя пользователя не изменено.")
                        break
                elif last_choice == "нет":
                    print(Fore.BLUE+"Вы отменили изменения")
                    break
                else:
                    print(Fore.RED+"Ошибка ввода (Допустимо: Да, Нет)")
        # Изменение заголовков
        elif field in choice_field[2:4]:
            while True:
                last_choice = input("Вы точно хотите изменить заголовки?"
                                    " (Да/Нет)\nВвод: ").strip().lower()
                if last_choice == "да":
                    titles = _note["titles"]
                    # Цикл изменения заголовков
                    for i in range(len(titles)):
                        new_title = input(f"Введите новый заголовок вместо \"{titles[i].capitalize()}\" "
                                          "(для отмены оставьте поле пустым): ").strip().lower()
                        # Проверка на пустой ввод
                        if new_title != "":
                            titles[i] = new_title
                        else:
                            print(Fore.BLUE+"Заголовок не изменен")
                    else:
                        print(Fore.GREEN+"Изменение заголовков успешно")
                        _note["titles"] = titles
                    break
                elif last_choice == "нет":
                    print(Fore.BLUE+"Вы отменили изменения")
                    break
                else:
                    print(Fore.RED+"Ошибка ввода (Допустимо: Да, Нет)")
        # Изменение описания
        elif field in choice_field[4:6]:
            while True:
                last_choice = input("Вы точно хотите изменить описание?"
                                    " (Да/Нет)\nВвод: ").strip().lower()
                if last_choice == "да":
                    new_content = input("Введите новое описание заметки "
                                        "(для отмены оставьте поле пустым): ").strip().lower()
                    # Проверка на пустой ввод
                    if new_content != "":
                        print(Fore.GREEN+"Описание изменено успешно")
                        _note["content"] = new_content
                        break
                    else:
                        print(Fore.BLUE+"Описание не изменено.")

                elif last_choice == "нет":
                    print(Fore.BLUE+"Вы отменили изменения")
                    break
                else:
                    print(Fore.RED+"Ошибка ввода (Допустимо: Да, Нет)")
        # Изменение статуса
        elif field in choice_field[6:8]:
            # Словарь значений статуса
            choice_status = {"1": "выполнено",
                             "2": "в процессе",
                             "3": "отложено"
                             }
            while True:
                last_choice = input("Вы точно хотите изменить статус?"
                                    " (Да/Нет)\nВвод: ").strip().lower()
                if last_choice == "да":
                    # Ввод нового статуса и проверка корректности ввода
                    new_status = input(
                        "Введите статус:\n1. Выполнено\n2. В процессе\n3. Отложено\nВвод: ").strip().lower()
                    # Проверка по ключу(цифре)
                    if new_status in choice_status.keys():
                        # Изменение и вывод нового статуса
                        _note["status"] = choice_status[new_status]
                        print(Fore.GREEN+f"Статус успешно обновлен на: {_note["status"]}")
                        break
                    # Проверка по значению(словам)
                    elif new_status in choice_status.values():
                        # Изменение и вывод нового статуса
                        _note["status"] = new_status
                        print(Fore.GREEN+f"Статус успешно обновлен на: {_note["status"]}")
                        break
                    else:
                        print(Fore.RED+"Ошибка ввода (Допустимо: 1, 2, 3 или Выполнено, В процессе, Отложено)")

                elif last_choice == "нет":
                    print(Fore.BLUE+"Вы отменили изменения")
                    break
                else:
                    print(Fore.RED+"Ошибка ввода (Допустимо: Да, Нет)")
        # Изменение дедлайна
        elif field in choice_field[8:10]:
            while True:
                last_choice = input("Вы точно хотите изменить дедлайн?"
                                    " (Да/Нет)\nВвод: ").strip().lower()
                if last_choice == "да":
                    issue_date_input = input("Введите новую дату дедлайна в формате "
                                             "(день.месяц.год): ").split(sep=".", maxsplit=-1)
                    try:
                        # Приведение года в формат "20__"
                        if len(issue_date_input[2]) == 2:
                            issue_date_input[2] = "20" + issue_date_input[2]

                        # Добавление в словарь с преобразованием списка в дату
                        _note["issue_date"] = datetime(int(issue_date_input[2]),
                                                       int(issue_date_input[1]),
                                                       int(issue_date_input[0]))
                        print(Fore.GREEN+"Дедлайн изменен успешно")
                        break
                    # Ловим исключения по значению и формату
                    except IndexError:
                        print(Fore.RED+"Ошибка формата: Дата введена не день.месяц.год")

                    except ValueError:
                        print(Fore.RED+"Ошибка значения: Были использованы не цифры или неверный формат дня, месяца, года")
                elif last_choice == "нет":
                    print(Fore.BLUE+"Вы отменили изменения")
                    break
                else:
                    print(Fore.RED+"Ошибка ввода (Допустимо: Да, Нет)")
        # Выход
        elif field in choice_field[10:]:
            break
        # Обработка ошибки ввода
        else:
            print(Fore.RED+"Ошибка ввода (Допустимо: 1, 2, 3, 4, 5 или"
                  " Имя пользователя, Заголовки, Описание, Статус, Дата истечения)")
    # Возвращение словаря
    return _note
# Главная часть
if __name__ == "__main__":
    # Пример готовой записки
    note = {'username': "роман",
            'titles': ["код", "правки"],
            'content': "исправить код",
            'status': "Отложено",
            'created_date': datetime.today(),
            'issue_date': datetime(2025, 2, 10)
            }
    # Вызов функций
    output_note(update_note(note))







