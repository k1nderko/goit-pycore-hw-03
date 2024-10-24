from datetime import datetime

input_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")

def get_days_from_today(date_str: str) -> datetime.day:
   
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date
        
        return delta.days
   
    except ValueError:
        return "Невірний формат дати. Використовуйте формат РРРР-ММ-ДД."


print(get_days_from_today(input_date))