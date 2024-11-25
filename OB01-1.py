# Пример реализации класса `Task` на Python
#
from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.creation_date = datetime.now()
        self.due_date = due_date
        self.completed = False
        self.completion_date = None

    def mark_as_completed(self):
        self.completed = True
        self.completion_date = datetime.now()

    def __repr__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return (f"Задача: {self.description}, "
                f"Дата создания: {self.creation_date.strftime('%Y-%m-%d %H:%M')}, "
                f"Срок выполнения: {self.due_date.strftime('%Y-%m-%d %H:%M')}, "
                f"Статус: {status}, "
                f"Дата фактического исполнения: {self.completion_date.strftime('%Y-%m-%d %H:%M') if self.completion_date else 'Не выполнено'}")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        return sorted(current_tasks, key=lambda x: x.due_date)

    def get_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if  task.completed]
        return sorted(completed_tasks, key=lambda x: x.due_date)

# Пример использования:
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Сделать домашнее задание", datetime(2024, 12, 15))
    manager.add_task("Купить продукты", datetime(2024, 12, 10))
    manager.add_task("Подготовить отчет", datetime(2024, 12, 20))

    # Вывод текущих задач
    print("Текущие задачи:")
    current_tasks = manager.get_current_tasks()
    for index, task in enumerate(current_tasks):
        print(f"{index}: {task}")

    # Отметка задачи как выполненной
    manager.mark_task_as_completed(1)

    # Вывод текущих задач после отметки
    print("\nТекущие задачи после выполнения одной из них:")
    current_tasks = manager.get_current_tasks()
    for index, task in enumerate(current_tasks):
        print(f"{index}: {task}")

    # Вывод выполненных задач после отметки
    print("\nВыполненные задачи после выполнения одной из них:")
    completed_tasks = manager.get_completed_tasks()
    for index, task in enumerate(completed_tasks):
        print(f"{index}: {task}")