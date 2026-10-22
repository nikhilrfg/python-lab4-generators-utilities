
# Task 3: Diary Entry Program

import os
from datetime import datetime


# Name of the diary file
filename = "diary.txt"

try:
    # Check if the diary file exists
    if not os.path.exists(filename):

        # Create the file if it does not exist
        with open(filename, "w", encoding="utf-8") as file:
            pass

        print("New diary file created.")

    else:
        print("Diary file already exists.")

    # Ask the user to enter a diary entry
    entry = input("Enter your diary entry: ")

    # Get the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the entry to the diary file
    with open(filename, "a", encoding="utf-8") as file:
        file.write(timestamp + " - " + entry + "\n")

    print("\nDiary entry saved successfully.")

    # Read and display all diary entries
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()

    print("\nAll Diary Entries:")
    print(contents)

except OSError as error:
    print("File Error: " + str(error))
