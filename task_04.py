from datetime import datetime, timedelta


def adjust_to_weekday(birthday: datetime.date) -> datetime.date:
    if birthday.weekday() >= 5:
        return birthday + timedelta(days=(7 - birthday.weekday()))
    return birthday

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming_birthdays = []
    current_year = today.year
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=current_year + 1)
        
        if today <= birthday_this_year <= (today + timedelta(days=7)):
            congratulation_date = adjust_to_weekday(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1989.10.28"}, 
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)