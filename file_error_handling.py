# Подключение формата даты, цвет текста, json и функции вывода
from datetime import datetime
import json
from colorama import init, Fore
from display_notes_function import display_notes

# Основная часть кода
if __name__ == "__main__":
    try:
        with open("notes.json", "w", encoding="utf-8") as file:



