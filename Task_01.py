from datetime import datetime


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


def get_days_from_today(date: str) -> int:
    '''Calculating the difference between today's date and any other date (in days)'''
    # Операційні змінні
    date_convert: datetime
    date_difference: int

    # Основний блок
    try:
        date_convert    = datetime.strptime(date, '%Y-%m-%d')                # Конвертація рядка у дату
        date_difference = (datetime.today() - date_convert).days * (-1)      # Різниця дат (у днях)
    except ValueError:
        print(f"Date '{date}' is incorrect. For example, 2026-01-29.")       # Стандартний виняток
    else:                         
        return date_difference


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


if __name__=='__main__':
    print(get_days_from_today('2026-01-01'))