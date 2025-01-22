"""
3. Обработка ошибок при работе с файлами
file_error_handling.py
Описание задачи:
    Добавить обработку ошибок в функции работы с файлами:
    Если файл отсутствует:
        Создать новый файл.
    Если файл повреждён или данные некорректны:
        Очистить файл.
    Если возникают другие ошибки (например, отсутствие прав):
        Вывести подробное сообщение об ошибке.
        Корректно завершить выполнение программы.
"""

# Подключение формата даты, цвет текста, json и функции вывода
import json
from datetime import datetime
from turtledemo.sorting_animate import enable_keys

from colorama import init, Fore
from Stage3.display_notes_function import display_notes
import yaml
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
def save_note_to_file(notes, filename = "notes"):
    # Словарь значений полей.
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
    # Проверка на существования списка
    if notes is None:
        print(Fore.RED+"У вас нет заметок для сохранения")
        return
    # Проверка на наличие заметок в списке
    elif len(notes) == 0:
        print(Fore.RED + "У вас нет заметок для сохранения")
        return
    try:
        # Открытие файла на запись с кодировкой "utf-8"
        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            notes_json = []
            # Цикл перебора заметок
            for i in range(len(notes)):
                note = notes[i]
                # Создание одной заметки с новыми ключами
                notes_json.append({
                    note_print["username"]: note["username"],
                    note_print["titles"]: note["titles"],
                    note_print["content"]: note["content"],
                    note_print["status"]: note["status"],
                    note_print["created_date"]: str(note["created_date"]),
                    note_print["issue_date"]: str(note["issue_date"])
                    })
            else:
                # Преобразовываем в формат yaml и записываем в файл json
                file.write(json.dumps(notes_json, ensure_ascii=False, indent=4))
    # Ошибка прав доступа
    except PermissionError:
        print("Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    # Ошибка в имени файла
    except OSError:
        print("Имя файла некорректно")
        filename_new = input("Введите имя файла ещё раз: ").strip()
        return save_note_to_file(notes, filename_new)

    print(Fore.GREEN + "Заметки сохранены успешно")
# Функция загрузки заметок из файла в список
def load_notes_from_file(filename = "notes"):
    # Словарь для замены ключей
    note_for_true_key = {'username': "Имя пользователя",
                         'titles': "Заголовки",
                         'content': "Описание",
                         'status': "Статус",
                         'created_date': 'Дата создания',
                         'issue_date': 'Дедлайн'
                        }
    # Ловим ошибки при открытии файла
    try:
        with open(f"{filename}.json","r", encoding="utf-8") as file:
            # Выгружаем список
            notes = json.load(file)
            # Цикл перебора заметок
            for i in range(len(notes)):
                note = notes[i].copy()
                # Цикл замены ключей в заметке
                for key in note_for_true_key.keys():
                    for key1 in notes[i].keys():
                        if note_for_true_key[key] == key1 and (key1 == "Дата создания" or key1 == "Дедлайн"):
                            note[key] = datetime.fromisoformat(note.pop(key1))
                        elif note_for_true_key[key] == key1:
                            note[key] = note.pop(key1)
                notes[i] = note
    # Ошибка прав доступа
    except PermissionError:
        print(Fore.RED +"Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    # Файл не найден
    except FileNotFoundError:
        print(Fore.RED +"Файл не найден")
        while True:
            create_file = input(f"Хотите создать файл с именем {filename}.json? "
                                f"(Да/Нет) Ввод: ").strip().lower()
            if create_file == "да":
                file_new = open(f"{filename}.json","w", encoding="utf-8")
                file_new.close()
                print("Файл создан")
                return
            elif create_file == "нет":
                return
            else:
                print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")
    # Ошибка в имени файла
    except OSError:
        print(Fore.RED +"Имя файла некорректно")
        filename_new = input("Введите имя файла ещё раз: ").strip()
        return load_notes_from_file(filename_new)
    # Файл повреждён или пуст
    except ValueError:
        print(Fore.RED +"Файл повреждён или пуст")
        while True:
            create_file = input(f"Хотите очистить файл с именем {filename}.json?"
                                f" (Да/Нет) Ввод: ").strip().lower()
            if create_file == "да":
                with open(f"{filename}.json", "w+", encoding="utf-8") as file_new:
                    file_new.truncate(0)
                    print("Файл очищен")
                return
            elif create_file == "нет":
                return
            else:
                print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")

    print(Fore.GREEN+"Заметки успешно записаны в список")
    #Возвращает список
    return notes

# Основная часть кода
if __name__ == "__main__":
    # Создание списка с 5 заметками
    notes1 = [{
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
    # Цикл ввода названия файла
    while True:
        count = 0
        filename_save = input("Введите имя файла для сохранения "
                              "(для перехода в другую папку используйте двойной \\: ").strip()
        for char in filename_save:
            if char == "\\":
                count += 1
        else:
            if count % 2 != 0:
                print("Для ввода \\ вам нужно вести двойной \\")
            else:
                break
    # Вызов функции
    save_note_to_file(notes1, filename_save)
    # Цикл ввода названия файла
    while True:
        count = 0
        filename_load = input("Введите имя файла для загрузки "
                              "(для перехода в другую папку используйте двойной \\: ").strip()
        for char in filename_load:
            if char == "\\":
                count += 1
        else:
            if count % 2 != 0:
                print("Для ввода \\ вам нужно вести двойной \\")
            else:
                break
    # Вызов функции
    notes_from_file = load_notes_from_file(filename_load)
    display_notes(notes_from_file)


