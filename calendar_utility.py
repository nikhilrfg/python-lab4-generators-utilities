
# Task 4: Date and Calendar Utility

import calendar
from datetime import datetime


try:
    # Ask the user to enter a year and month
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))

    # Validate the year and month
    if year < 1 or year > 9999:
        raise ValueError("Year must be between 1 and 9999.")

    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    # Display the selected month's calendar
    print("\nCalendar for the Selected Month:")
    print(calendar.month(year, month))

    # Get today's date
    today = datetime.now()

    print("Today's Date: " + today.strftime("%B %d, %Y"))

    # Check whether today falls in the selected month and year
    if today.year == year and today.month == month:
        print("Today is " + today.strftime("%B %d, %Y") +
              " and falls within the selected month.")
    else:
        print("Today's date does not fall within the selected month.")

except ValueError as error:
    print("\nInvalid Input: " + str(error))
