tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def print_uncompleted_tasks():
    pass
    # raise NotImplementedError()

def print_completed_tasks():
    pass
    # raise NotImplementedError()

def print_all_tasks():
    pass
    # raise NotImplementedError()

def print_tasks_minimum_time_taken(minimum_time_taken):
    pass
    # raise NotImplementedError()

def print_task_by_description(description):
    pass
    # raise NotImplementedError()

def mark_task_as_complete(description):
    pass
    # raise NotImplementedError()

def add_task(description, completed, time_taken):
    pass
    # raise NotImplementedError()

print("=== UNCOMPLETED TASKS ===")
print_uncompleted_tasks()
print()

print("=== COMPLETED TASKS ===")
print_completed_tasks()
print()

print("=== ALL TASKS ===")
print_all_tasks()
print()

print("=== TASKS THAT TAKE AT LEAST 30 MINUTES ===")
print_tasks_minimum_time_taken(minimum_time_taken=30)
print()

print("=== DETAILS OF \"Make Dinner\" ===")
print_task_by_description("Make Dinner")
print()

print("=== MARKING \"Wash Dishes\" AS COMPLETE ===")
mark_task_as_complete("Wash Dishes")

print("=== ADDING TASK ===")
add_task(description="Eat Supper", completed=False, time_taken=15)

print("=== ALL TASKS ===")
print_all_tasks()
print()
