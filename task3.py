import re
# існуючі номери телефонів в базі:
raw_numbers = [ 
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    # Видаляємо зайві пробіли, табуляції, символи нового рядка та інші непотрібні символи
    phone_number = phone_number.strip()  # Видаляємо пробіли з початку та кінця
    phone_number = re.sub(r'[\s\t\n]', '', phone_number)  # Видаляємо табуляції, пробіли та символи нового рядка
    
    # Видаляємо всі символи, крім цифр та символу '+'
    normalized_number = re.sub(r'[^0-9+]', '', phone_number)
    
    # Перевіряємо, чи є вже міжнародний код
    if normalized_number.startswith('+'):
        # Якщо номер починається з '+', перевіряємо, чи є код країни
        if normalized_number[:3] != '+38':
            # Якщо код не український, додаємо '+38'
            normalized_number = '+38' + normalized_number[1:]
    else:
        # Якщо номер не починається з '+', додаємо код '+38'
        normalized_number = '+38' + normalized_number
    
    return normalized_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Виводимо нормалізовані номери кожен на новому рядку
print("Номери телефонів для SMS-розсилки:")
for num in sanitized_numbers:
    print(num)

