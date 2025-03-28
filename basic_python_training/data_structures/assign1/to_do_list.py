tasks=[]

def add_task(task):
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")

def remove_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print(f"Removed: {task}")
            return
    print(f"Task '{task}' not found!")

def update_task(old_task, new_task):
    for t in tasks:
        if t["task"] == old_task:
            t["task"] = new_task
            print(f"Updated: '{old_task}' ➝ '{new_task}'")
            return
    print(f"Task '{old_task}' not found!")

def mark_complete(task):
    for t in tasks:
        if t["task"] == task:
            t["done"] = True
            print(f"Marked as complete: {task}")
            return
    print(f"Task '{task}' not found!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n To-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Not Done"
        print(f"{i}. {t['task']} - {status}")

add_task("Read a book")
add_task("Take a walk")
add_task("Workout")

show_tasks()

mark_complete("take a walk")
update_task("Workout", "Exercise")
remove_task("read a book")

show_tasks()