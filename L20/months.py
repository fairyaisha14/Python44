import datetime

# Loop through all 12 months
for month in range(1, 13):
    # Create a date object for the first day of each month
    date = datetime.date(2025, month, 1)
    # Format and print the month's full name
    print(date.strftime("%B"))

