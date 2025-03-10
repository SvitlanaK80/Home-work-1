import random

min_value = 1
max_value = 49
quantity_value = 6

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо, чи параметри відповідають обмеженням
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []  # Повертаємо порожній список, якщо параметри некоректні
    
    # Генеруємо набір унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)

ticket_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
print(f"Ваші лотерейні числа: {ticket_numbers}")