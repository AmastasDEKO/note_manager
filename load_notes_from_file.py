"""
2. Загрузка заметок из файла
Файл: load_notes_from_file.py
Описание задачи:
Создать функцию load_notes_from_file(filename), которая:
Читает заметки из текстового файла в формате YAML.
Преобразует данные в список словарей.

"""
# Подключение формата даты, цвет текста, json и функции вывода
from datetime import datetime
import json
from colorama import init, Fore
from display_notes_function import display_notes
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
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
        with open(f"{filename}.json", encoding="utf-8") as file:
            # Выгружаем список
            notes = json.load(file)
            # Цикл перебора заметок
            for i in range(len(notes)):
                note = notes[i].copy()
                # Цикл замены ключей в заметке
                for key in note_for_true_key.keys():
                    for key1 in notes[i].keys():
                        if note_for_true_key[key] == key1 and key1 != "Дата создания" and key1 != "Дедлайн":
                            note[key] = note.pop(key1)
                        elif note_for_true_key[key] == key1 and (key1 == "Дата создания" or key1 == "Дедлайн"):
                            note[key] = datetime.fromisoformat(note.pop(key1))
                notes[i] = note
    # Ошибка прав доступа
    except PermissionError:
        print("Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    # Ошибка в названии файла
    except OSError:
        print("Файл не найден")
        return
    # Проверка закрыт ли файл
    if file.closed:
        print(Fore.GREEN+"Заметки успешно записаны в список")
        #Возвращает список
        return notes
    else:
        print(Fore.RED+"Файл не был закрыт")
# Основная часть кода
if __name__ == "__main__":
    # Вызов функции
    notes_from_file = load_notes_from_file()
    display_notes(notes_from_file)