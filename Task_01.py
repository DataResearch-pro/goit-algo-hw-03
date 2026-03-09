from datetime import datetime


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


def get_days_from_today():
    '''Calculating the difference between today's date and any other date (in days)'''
    # Вхідні дані та операційні змінні
    date_custom: str
    date_convert: datetime
    date_difference: int

    # Основний блок
    try:
        date_custom     = input("Enter the date in the format YYYY-MM-DD: ")        # Отримання дати від користувача
        date_convert    = datetime.strptime(date_custom, '%Y-%m-%d')                # Конвертація рядка у дату
        date_difference = (datetime.today() - date_convert).days * (-1)             # Різниця дат (у днях)
    except ValueError:
        print(f"Date '{date_custom}' is incorrect. For example, 2026-01-29.")       # Стандартний виняток
    else:
        print(f"\nDifference: {date_difference} (days)\n")                          
        #return date_difference                                                     # Якщо потрібен експорт результату


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


if __name__=='__main__':
    get_days_from_today()