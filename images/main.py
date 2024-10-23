class Task:
    def __init__(self, name):
        self.name = name
        self.next = None

class DailyRoutine:
    def __init__(self):
        self.start = None

    def create_task(self):
        # Create the tasks
        start_of_day = Task("Start of day")
        wake_up = Task("Wake up")
        drink_coffee = Task("Drink coffee")
        meeting = Task("Meeting")
        lunch = Task("Lunch")

        # Connect the tasks
        self.start = start_of_day
        start_of_day.next = wake_up
        wake_up.next = drink_coffee
        drink_coffee.next = meeting
        meeting.next = lunch

    def show_task(self):
        current_task = self.start
        while current_task:
            print(current_task.name)
            if current_task.next:
                print("|")
            current_task = current_task.next

    def add_task(self, task_name):
        new_task = Task(task_name)
        if self.start is None:
            self.start = new_task
        else:
            current_task = self.start
            while current_task.next:
                current_task = current_task.next
            current_task.next = new_task

# Criação da rotina e execução das tarefas
routine = DailyRoutine()
routine.create_task()
routine.show_task()

print("\n>> Adding new task 'Exercise'")
routine.add_task("Exercise")
print("\n")
routine.show_task()
