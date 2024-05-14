import threading
from abc import ABC, abstractmethod
import uuid
import datetime
from threading import Lock


class IToDoList(ABC):
    """
    Abstract base class for a ToDo list.

    Methods:
        addTask: Add a task to the ToDo list.
        getTask: Get a task from the ToDo list.
        modifyTask: Modify a task in the ToDo list.
        removeTask: Remove a task from the ToDo list.
    """

    @abstractmethod
    def addTask(self, task):
        pass

    @abstractmethod
    def getTask(self, task_id):
        pass

    @abstractmethod
    def modifyTask(self, task):
        pass

    @abstractmethod
    def removeTask(self, task_id):
        pass


class Task:
    """
    Represents a task with an ID, description, deadline, and completion status.

    Args:
        task_id: The unique identifier for the task.
        description: The description or details of the task.
        deadline (optional): The deadline for completing the task. Defaults to None.

    Attributes:
        id: The unique identifier for the task.
        description: The description or details of the task.
        deadline: The deadline for completing the task.
        completed: A boolean indicating whether the task is completed or not.
    """

    def __init__(self, task_id, description, deadline=None):
        self.id = task_id
        self.description = description
        self.deadline = deadline
        self.completed = False


class ToDoList(IToDoList):
    """
    Class representing a ToDo list with task management functionalities.

    Methods:
        addTask: Add a task to the ToDo list.
        getTask: Get a task from the ToDo list.
        modifyTask: Modify a task in the ToDo list.
        removeTask: Remove a task from the ToDo list.
        completeTask: Mark a task as completed.
        listTasks: List tasks based on optional filtering and sorting functions.
        getStatistics: Get statistics on tasks and activities within a specified time period.
        getActivityLog: Get the activity log within a specified time period.
    """

    def __init__(self):
        super().__init__()
        self.tasks = {}
        self.archive = []
        self.log = {}

    def addTask(self, task):

        if task.id in self.tasks:
            return "Error: Task with similar id already exists"

        self.tasks[task.id] = task
        self.log[str(uuid.uuid4())] = {
            "action": "add",
            "time": datetime.datetime.now(),
            "logMessage": f"Task Added - ID {task.id}",
        }
        return f"Task Added SuccessFully - ID {task.id}"

    def getTask(self, task_id):

        return self.tasks.get(task_id, "Task Not Found!!!")

    def modifyTask(self, task):
        if task.id in self.tasks:
            self.tasks[task.id] = task
            self.log[str(uuid.uuid4())] = {
                "action": "update",
                "time": datetime.datetime.now(),
                "logMessage": f"Task Updated - ID {task.id}",
            }
            return f"Task Updated SuccessFully - ID {task.id}"

        return "Provided Task doesn't exist"

    def removeTask(self, task_id):
        if task_id in self.tasks:
            return self._extracted_from_completeTask_3(
                task_id,
                "delete",
                'Task Deleted - ID ',
                'Task Removed SuccessFully - ID ',
            )
        return "Provided Task doesn't exist"

    def completeTask(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].completed = True
            return self._extracted_from_completeTask_3(
                task_id,
                "complete",
                'Task Completed - ID ',
                'Task Completed SuccessFully - ID ',
            )
        return "Provided Task doesn't exist"

    # TODO Rename this here and in `removeTask` and `completeTask`
    def _extracted_from_completeTask_3(self, task_id, arg1, arg2, arg3):
        task_pop = self.tasks.pop(task_id)
        self.archive.append(task_pop)
        self.log[str(uuid.uuid4())] = {
            "action": arg1,
            "time": datetime.datetime.now(),
            "logMessage": f"{arg2}{task_id}",
        }
        return f"{arg3}{task_id}"

    def listTasks(self, filter_func=None, sort_func=None):
        filter_tasks = [
            task
            for task in self.tasks.values()
            if (not filter_func or filter_func(task))
        ]
        if sort_func:
            filter_tasks.sort(key=sort_func)

        return filter_tasks

    def getStatistics(self, time_period=None):
        """
        Get statistics based on the activities and tasks within a specified time period.

        Args:
            time_period (int, optional): The number of days to consider for the statistics. Defaults to None.

        Returns: dict: A dictionary containing the counts of tasks added, completed, and spilled within the specified
        time period.
        """

        start_time = (
            datetime.datetime.now() - datetime.timedelta(days=time_period)
            if time_period
            else None
        )
        summary = {"Added": 0, "Completed": 0, "Spilled": 0}
        for activity in self.log.values():
            # Assuming TimePeriod as Last X Days
            if not start_time or activity["time"] > start_time:
                if activity["action"] == "add":
                    summary["Added"] += 1
                elif activity["action"] == "complete":
                    summary["Completed"] += 1

        for task in self.tasks.values():
            # Assuming TimePeriod as Last X Days
            if task.deadline and start_time and task.deadline < datetime.datetime.now():
                summary["Spilled"] += 1

        return summary

    def getActivityLog(self, time_period=None):
        start_time = (
            datetime.datetime.now() - datetime.timedelta(days=time_period)
            if time_period
            else None
        )
        return [
            activity
            for activity in self.log.values()
            if not start_time or activity["time"] > start_time
        ]


# Driver Program
task_1 = Task(1, "Learn Python")
task_2 = Task(
    2,
    "Understand PostgreSQL Connections",
    datetime.datetime.now() - datetime.timedelta(days=7),
)
task_3 = Task(3, "Learn Cooking")
# print(task_1.__dict__)
# print(task_2.__dict__)
todo_list = ToDoList()
print(todo_list.addTask(task_1))
print(todo_list.addTask(task_2))
print(todo_list.addTask(task_3))
# print(todo_list.log)
print(todo_list.getTask(1))
print(todo_list.getTask("1111"))
task_3 = Task(1, "Learn Advanced Python")
print(todo_list.modifyTask(task_3))
print(todo_list.getTask(1).__dict__)
print(todo_list.removeTask(1))
print(todo_list.listTasks())
print(todo_list.completeTask(2))
print(todo_list.listTasks())
# print(todo_list.log)
print(todo_list.getActivityLog())
print(todo_list.getStatistics(2))
