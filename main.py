import datetime, bday_messages, random

today = datetime.date.today()
next_birthday = datetime.date(2027, 10, 25).days
date_of_birth = datetime.date(2005, 10, 25).days
time_difference = next_birthday - today

if today == next_birthday:
    print(random.choice(bday_messages))
else:
    print(f'My next birthday is {time_difference} days away!')
    print(f'You were born {today - date_of_birth} days ago!')