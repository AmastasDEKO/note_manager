"""
5. Выбор формата файла
save_notes_json.py
Описание задачи:
    Создать функцию save_notes_to_json(notes, filename), которая:
        Перезаписывает данные файла, записывая список заметок в структуре JSON.
        Данные сохраняются в удобочитаемом формате (с отступами).
"""
# Подключение формата даты и цвет текста
from datetime import datetime
from colorama import init, Fore
import json
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
def save_notes_json(notes, filename = "notes"):
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
                notes_json.append({
                    note_print["username"]: note["username"],
                    note_print["titles"]: note["titles"],
                    note_print["content"]: note["content"],
                    note_print["status"]: note["status"],
                    note_print["created_date"]: str(note["created_date"]),
                    note_print["issue_date"]: str(note["issue_date"])
                })

            # После выполнения цикла, закрываем файл
            else:
                json.dump(notes_json, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print("Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    except OSError:
        print("Имя файла некорректно")
        filename_new = input("Введите имя файла ещё раз: ").strip()
        return save_notes_json(notes, filename_new)

    # Проверка закрыт ли файл
    if file.closed:
        print(Fore.GREEN + "Заметки сохранены успешно")
    else:
        print(Fore.RED + "Файл не был закрыт")
        file.close()


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
    # Вызов функции
    save_notes_json(notes1)
