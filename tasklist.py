tasks = []

def add_task(task, priority):
    tasks.append((priority, task))
    tasks.sort()

def remove_task():
    if tasks:
        return tasks.pop(0)[1]
    return "No tasks available"

def update_task(old_task, new_task, new_priority):
    global tasks
    tasks = [(p, t) for p, t in tasks if t != old_task]
    add_task(new_task, new_priority)

def show_tasks():
    return tasks

add_task("Design UI", 2)
add_task("Fix bugs", 1)
add_task("Write documentation", 3)
print(show_tasks())
print(remove_task())
print(show_tasks())
