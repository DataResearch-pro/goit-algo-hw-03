import random


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    '''Generation uniq numbers'''
    uniq_numbers = []                                                           # Унікальні числа
    flag_type = all(isinstance(args, int) for args in (min, max, quantity))     # Перевірка аргументів [ type(int) ]
    
    # Обмеження для типу
    if not flag_type:
        return uniq_numbers
    
    # Валідація логіки відповідно умов задачі
    flag_min = 0 < min < max
    flag_max = min < max < 1001
    flag_quantity = 0 < quantity < max
    
    # ↑ Обмеження для значень аргументів
    if not flag_min or not flag_max or not flag_quantity:
        return uniq_numbers
    
    # Основні операції
    interval = range(min, max)                                                  # Інтервал для рандомної вибірки
    uniq_numbers = sorted(random.sample(interval, quantity))                    # Генерація унікальних чисел
    
    return uniq_numbers


#⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶⊷⊶


if __name__ == "__main__":
    start_lottery = get_numbers_ticket(1, 1000, 6)
    print(f"\nВаші лотерейні числа:\n{start_lottery}\n")