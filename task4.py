from datetime import datetime, timedelta

users = [
    {"name": "Іван", "birthday": "1990.03.24"},
    {"name": "Марія", "birthday": "1985.03.14"},
    {"name": "Петро", "birthday": "1992.03.17"},
    {"name": "Олена", "birthday": "1989.03.20"},
]

def get_upcoming_birthdays(users):
    # Поточна дата (використовуємо реальну поточну дату)
    today = datetime.today().date()  # Поточна дата
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо день народження з рядка у форматі 'рік.місяць.дата' в об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Якщо день народження вже був цього року, використовуємо дату наступного року
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)
        
        # Перевіряємо, чи день народження знаходиться в межах наступного тижня
        if today <= birthday <= today + timedelta(days=7):
            # Перевірка, чи день народження припадає на вихідний (субота або неділя)
            if birthday.weekday() == 5:  # Субота
                birthday = birthday + timedelta(days=2)  # Переносимо на понеділок
            elif birthday.weekday() == 6:  # Неділі
                birthday = birthday + timedelta(days=1)  # Переносимо на понеділок
            
            # Додаємо користувача з оновленою датою привітання
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)

# Виводимо результати
print("Список користувачів з найближчими днями народження:")
for user in upcoming_birthdays:
    print(f"Користувач: {user['name']}, Дата привітання: {user['congratulation_date']}")

