"""
3. check_deadline.py: Обработка дедлайнов
Функциональность:
Запрашивает дату дедлайна и сравнивает её с текущей датой.
Сообщает, истёк ли дедлайн или сколько дней осталось.
Проверяет корректность формата ввода.
"""

# Подключение формата даты
from datetime import datetime, date

# Функция для расчёта дней
def days(note):
    days_count = (note["issue_date"] - datetime.today().date()).days
    # Вывод сообщению о состоянии дедлайна
    if days_count > 0:
        print(f"До дедлайна осталось дней: {days_count}")
    elif days_count == 0:
        print("Дедлайн сегодня!")
    elif days_count < 0:
        print(f"Дедлайн был дней назад: {days_count*-1} ")
    return


# Функция для ввода дедлайн
def input_deadline():
        issue_date_input = input("Введите дату дедлайн в формате (день.месяц.год): ").split(sep=".", maxsplit=-1)
        # Ловим исключения по значению и формату
        try:
            # Приведение года в формат "20__"
            if len(issue_date_input[2]) == 2:
                issue_date_input[2] = "20" + issue_date_input[2]
            # Добавление в словарь с преобразованием списка в дату
            note = {"issue_date": date(
                   int(issue_date_input[2]),
                   int(issue_date_input[1]),
                   int(issue_date_input[0]))
                   }
            # Возвращаем словарь
            return note
        except IndexError:
            print("Ошибка формата: Дата введена не день.месяц.год")
            return input_deadline()
        except ValueError:
            print("Ошибка значения: Были использованы не цифры или неверный формат дня, месяца, года")
            return input_deadline()

# Вызов функций
days(input_deadline())
