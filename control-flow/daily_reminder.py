#!/usr/bin/env python3

# Prompt for a Single Task
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize reminder message
reminder_message = ""
action_required = ""

# Process the Task Based on Priority using Match Case
match priority:
    case 'high':
        reminder_message = f"'{task}' is a **high priority** task"
    case 'medium':
        reminder_message = f"'{task}' is a **medium priority** task"
    case 'low':
        reminder_message = f"Note: '{task}' is a **low priority** task. Consider completing it when you have free time."
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level."

# Use an if statement to modify the reminder if the task is time-bound (for high/medium priority)
if time_bound == 'yes':
    # This message is added to the high/medium priority cases
    action_required = " that requires immediate attention today!"

# Output the Customized Reminder
if priority in ['high', 'medium']:
    # Combine the base reminder and the action required (if any)
    print(f"\nReminder: {reminder_message}{action_required}")
else:
    # For low priority or unknown priority, print the pre-generated message
    print(f"\n{reminder_message}")
