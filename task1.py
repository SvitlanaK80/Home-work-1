from datetime import datetime

def get_days_from_today(date):
    # Перетворюємо рядок у форматі 'РРРР-ММ-ДД' у об'єкт datetime
    given_date = datetime.strptime(date, '%Y-%m-%d')
    
    today = datetime.today()   # Отримуємо поточну дату
    
    delta = today - given_date # Розраховуємо різницю між поточною датою і заданою
    
    return delta.days  # Повертаємо різницю в днях

# Запит на введення дати
date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

# Викликаємо функцію з введеною датою
print(f"Кількість днів між заданою датою і сьогоднішнім днем: {get_days_from_today(date_input)}")

