# Enter your code here
is_weekday = bool(True)
is_holiday = bool(False)

no_school_today = bool((not is_weekday) or is_holiday)

print(no_school_today)