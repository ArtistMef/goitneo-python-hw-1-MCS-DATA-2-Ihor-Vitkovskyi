from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthday_week = defaultdict(list)
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        delta_days = (birthday_this_year - today).days
        weekday_birthday = birthday_this_year.weekday()
        
        if delta_days < 0:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days
            weekday_birthday = birthday_this_year.weekday()

        if delta_days < 7:
            greeting_day = weekday_birthday
            if delta_days == 0:  
                birthday_week[weekday_names[greeting_day]].append(name)
            elif greeting_day >= 5:  
                greeting_day = 0  
                birthday_week[weekday_names[greeting_day]].append(name)
            else:
                birthday_week[weekday_names[greeting_day]].append(name)
        
        
    print("Birthdays:")
    for day, users in birthday_week.items():
        print(f"{day}: {', '.join(users)}")
  

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Anton Pinchuk", "birthday": datetime(1988, 12, 17)},
    {"name": "Ivan Mazepa", "birthday": datetime(1955, 12, 17)},
        ]

get_birthdays_per_week(users)