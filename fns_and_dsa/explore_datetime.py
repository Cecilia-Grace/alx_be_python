from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date
    

def calculate_future_date():
    number_of_days_to_add = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=number_of_days_to_add)
    future_date = display_current_datetime() + duration
    return f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}"


print(display_current_datetime().strftime("%Y-%m-%d %H:%M:%S"))
print(calculate_future_date())