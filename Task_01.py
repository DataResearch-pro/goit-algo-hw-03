from datetime import datetime


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶

# Константи та вхідні дані
DATE_NOW = datetime.today()
date_custom = input("Enter the date in the format: YYYY-MM-DD (for example, 2026-01-01): ")

#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


def get_days_from_today(date: str) -> int:
    '''Calculating the difference between dates (in days)'''
    try:
        date_convert = datetime.strptime(date, '%Y-%m-%d')                                              # Конвертація до об'єкта datetime
        difference_date = DATE_NOW - date_convert                                                       # Різниця дат (timedelta obj)
    except ValueError:
        print(f"Date '{date}' is incorrect. Format: YYYY-MM-DD (for example, 2026-01-01)")              # Стандартний виняток
    else:
        return difference_date.days * (-1)


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


if __name__=='__main__':
    diff_dates = get_days_from_today(date_custom)
    if diff_dates is not None:
        print(f"\nDifference: {get_days_from_today(date_custom)} (days)\n")