# daily_reminder.py

# 1. Prompt for a Single Task:
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# 2. Process the Task Based on Priority and Time Sensitivity using Match Case:
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _: # Handles any other input for priority
        reminder_message = f"'{task}' has an unknown priority"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    # Specific message for low priority, non-time-bound tasks
    reminder_message += ". Consider completing it when you have free time."
else:
    # For medium/high priority non-time-bound tasks, just complete the sentence
    reminder_message += "."

# 3. Provide a Customized Reminder:
print(f"\nReminder: {reminder_message}")
