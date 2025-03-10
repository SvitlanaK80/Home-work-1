from datetime import datetime, timedelta

# Список користувачів:
users = [
    {"name": "Іван", "birthday": "1990.03.10"},
    {"name": "Марія", "birthday": "1985.03.12"},
    {"name": "Петро", "birthday": "1992.03.15"},
    {"name": "Олена", "birthday": "1989.03.17"},
    {"name": "Андрій", "birthday": "1987.03.18"},
    {"name": "Оксана", "birthday": "1995.03.20"},
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()  # Отримуємо поточну дату
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Замінюємо рік на поточний
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження входить у діапазон 7 днів від сьогодні
        if today <= birthday_this_year <= today + timedelta(days=7):
            # Якщо день народження припадає на вихідний, переносимо на наступний понеділок
            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                birthday_this_year += timedelta(days=1)
            
            # Додаємо користувача до списку привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Отримуємо список привітань
upcoming_birthdays = get_upcoming_birthdays(users)

# Виводимо результати
print("Список користувачів з найближчими днями народження:")
for user in upcoming_birthdays:
    print(f"Користувач: {user['name']}, Дата привітання: {user['congratulation_date']}")
