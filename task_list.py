tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def print_task(task, one_line = True):
    completed_msg = "done" if task['completed'] else "UNCOMPLETED"
    if one_line:
        print(f"* {task['description']:25s}\t{completed_msg:11s}\t[{task['time_taken']:2d}]")
    else:
        print(f"* description:  {task['description']}")
        print(f"  status:       {completed_msg}")
        print(f"  time taken:   {task['time_taken']:2d}")

def print_tasks(tasks=tasks):
    for task in tasks:
        print_task(task)
    print(f"{len(tasks):d} tasks")

def print_uncompleted_tasks():
    print_tasks([task for task in tasks if task['completed'] == False])
    # for task in tasks:
    #     if task['completed'] == False:
    #         print_task(task)

def print_completed_tasks():
    print_tasks([task for task in tasks if task['completed']])
    # for task in tasks:
    #     if task['completed']:
    #         print_task(task)

def print_tasks_minimum_time_taken(minimum_time_taken):
    print_tasks([task for task in tasks if task['time_taken'] >= minimum_time_taken])
    # for task in tasks:
    #     if task['time_taken'] >= minimum_time_taken:
    #         print_task(task)

def first(list):
    if len(list) == 0:
        return None
    return list[0]

def search_list(list, predicate):
    return first([ item for item in list if predicate(item)])
    #for item in list:
    #    if predicate(item):
    #        return item
    #return None

def search_list_of_dicts(list, key, value):
    return search_list(list, lambda item: item[key] == value)

def find_task_by_description(description):
    return search_list_of_dicts(tasks, 'description', description)

def print_task_by_description(description):
    found_task = find_task_by_description(description)
    print_task(found_task, one_line=False)

def mark_task_as_complete(description):
    found_task = find_task_by_description(description)
    found_task['completed'] = True

def add_task(description, time_taken, completed=False):
    tasks.append({
        'description': description,
        'completed': completed,
        'time_taken': time_taken,
    })

print("=== UNCOMPLETED TASKS ===")
print_uncompleted_tasks()
print()

print("=== COMPLETED TASKS ===")
print_completed_tasks()
print()

print("=== ALL TASKS ===")
print_tasks()
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
add_task(description="Eat Supper", time_taken=15)

print("=== ALL TASKS ===")
print_tasks()
print()
