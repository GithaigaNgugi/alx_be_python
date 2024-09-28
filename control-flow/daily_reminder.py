# daily_reminder.py

def get_task_input():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    reminder = f"'{task}' is a {priority} priority task."
    
    # Modify the reminder if the task is time-sensitive
    if time_bound == 'yes':
        reminder += " It requires immediate attention today!"
    else:
        match priority:
            case 'high':
                reminder += " Try to complete it soon."
            case 'medium':
                reminder += " You should aim to complete it today."
            case 'low':
                reminder += " Consider completing it when you have free time."
    
    return reminder

def main():
    while True:
        task, priority, time_bound = get_task_input()
        
        # Ensure the priority and time-bound inputs are valid
        if priority in ['high', 'medium', 'low'] and time_bound in ['yes', 'no']:
            reminder = create_reminder(task, priority, time_bound)
            print("Reminder:", reminder)  # This line satisfies the print("Reminder: ...") condition
            break  # Exit the loop once a valid input is processed
        else:
            print("\nInvalid input. Please try again.\n")
            continue

if __name__ == "__main__":
    main()