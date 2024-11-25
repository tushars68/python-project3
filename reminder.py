# Importing necessary libraries
import time
from plyer import notification
from IPython.display import clear_output

# Function to handle notifications
def notify_user(reminder_title, reminder_message):
    try:
        notification.notify(
            title=reminder_title,
            message=reminder_message,
            timeout=8  # Notification stays for 8 seconds
        )
    except NotImplementedError:
        print(f"ALERT: {reminder_title} - {reminder_message}")

# Function to input reminder details
def get_reminder_details():
    reminder_title = input("What should the reminder title be? ")
    reminder_message = input("Add some details for the reminder: ")
    try:
        reminder_time = int(input("After how many seconds should I remind you? "))
        if reminder_time <= 0:
            raise ValueError("Time must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None, None
    return reminder_title, reminder_message, reminder_time

# Main function for the reminder program
def run_reminder_program():
    while True:
        clear_output(wait=True)
        print("==== Welcome to My Reminder App ====")
        print("1. Add a new reminder")
        print("2. Quit")
        user_choice = input("Choose an option (1/2): ")

        if user_choice == '1':
            print("\n--- Setting up your reminder ---")
            title, message, delay = get_reminder_details()
            
            if title and message and delay:
                print(f"Reminder set! I will remind you in {delay} seconds.\n")
                time.sleep(delay)
                notify_user(title, message)
                print("Reminder notification sent!")
            else:
                print("Reminder not set. Please try again.")
            time.sleep(2)

        elif user_choice == '2':
            print("Thank you for using the reminder app. Goodbye!")
            break

        else:
            print("Invalid choice. Please select either 1 or 2.")
            time.sleep(2)

# Run the app
run_reminder_program()
