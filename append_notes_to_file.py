"""
4. Добавление данных в файл
append_notes_to_file.py
Описание задачи:
    Создать функцию append_notes_to_file(notes, filename), которая:
        Загружает существующие заметки из файла.
        Добавляет новые заметки и сохраняет обратно в файл.
        Проверяет корректность формата новых заметок.
"""
# Подключение формата даты и цвет текста и json
from datetime import datetime
from colorama import init, Fore
import json
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
def append_notes_to_file(notes, filename):
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
        # Открытие файла на запись и чтение с кодировкой "utf-8"
        with open(filename, "r", encoding="utf-8") as file:
            notes_json = json.load(file)
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

        with open(filename, "w", encoding="utf-8") as file:
            data = json.dumps(notes_json, ensure_ascii=False, indent=4)
            file.write(data)

    # Ошибка прав доступа
    except PermissionError:
        print(Fore.RED + "Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    # Файл не найден
    except FileNotFoundError:
        print(Fore.RED + "Файл не найден")
        while True:
            create_file = input(f"Хотите создать файл с именем {filename}? "
                                f"(Да/Нет) Ввод: ").strip().lower()
            if create_file == "да":
                file_new = open(filename, "w", encoding="utf-8")
                file_new.close()
                print("Файл создан")
                return
            elif create_file == "нет":
                return
            else:
                print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")
    # Ошибка в имени файла
    except OSError:
        print(Fore.RED + "Имя файла некорректно")
        filename_new = input("Введите имя файла ещё раз: ").strip()
        return append_notes_to_file(notes,filename_new)
    # Файл повреждён или пуст
    except ValueError:
        print(Fore.RED + "Файл повреждён или пуст")
        while True:
            create_file = input(f"Хотите очистить файл с именем {filename}?"
                                f" (Да/Нет) Ввод: ").strip().lower()
            if create_file == "да":
                with open(filename, "w+", encoding="utf-8") as file_new:
                    file_new.truncate(0)
                    print("Файл очищен")
                return
            elif create_file == "нет":
                return
            else:
                print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")
    print(Fore.GREEN + "Заметки сохранены успешно")

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
    # Создание пустого списка
    notes2 = []

    # Создание списка с одной заметкой
    notes3 = [{
        "username": "костя",
        "titles": ["код", "гит"],
        "content": "проверить код на гитхабе",
        "status": "в процессе",
        "created_date": datetime.today(),
        "issue_date": datetime(2025, 1, 12)
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
    append_notes_to_file(notes3, filename_save)
