from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import datetime
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)


class Program:
    def __init__(self, session):
        self.session = session
        self.commands = {
            "1": ("Today's tasks", self.print_today_tasks),
            "2": ("Week's tasks", self.print_week_tasks),
            "3": ("All tasks", self.print_all_tasks),
            "4": ("Missed tasks", self.print_missed_tasks),
            "5": ("Add task", self.add_task),
            "6": ("Delete task", self.delete_task),
            "0": ("Exit", self.exit)
        }

    session = None

    @staticmethod
    def print_tasks(tasks):
        if len(tasks) == 0:
            print("Nothing to do!")
        else:
            for i in range(len(tasks)):
                task = tasks[i]
                print(f"{i + 1}. {task.task}")
        print()

    def print_commands(self):
        for command in self.commands.keys():
            print(f"{command}) {self.commands[command][0]}")

        current_command = input()
        print()
        return current_command

    def print_today_tasks(self):
        today = datetime.datetime.now().date()
        tasks = self.session.query(Task).filter(Task.deadline == today).order_by(Task.deadline).all()
        print(f"Today {today.day} {today.strftime('%b')}:")
        self.print_tasks(tasks)

    def print_week_tasks(self):
        today = datetime.datetime.now().date()
        start = today
        end = start + datetime.timedelta(days=7)

        tasks = self.session.query(Task).filter(Task.deadline >= start, Task.deadline <= end).order_by(Task.deadline).all()
        grouped = {datetime.date.fromordinal(x): [] for x in range(start.toordinal(), end.toordinal())}
        for task in tasks:
            grouped[task.deadline].append(task)

        for date in grouped:
            print(f"{date.strftime('%A')} {date.day} {date.strftime('%b')}:")
            tasks = grouped[date]
            self.print_tasks(tasks)

    def print_all_tasks(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()
        if len(tasks) == 0:
            print("Nothing to do!")
        else:
            print("All tasks:")
            for i in range(len(tasks)):
                task = tasks[i]
                print(f"{i + 1}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
        print()

    def print_missed_tasks(self):
        today = datetime.datetime.now().date()
        tasks = self.session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()
        if len(tasks) == 0:
            print("Nothing is missed!")
            return
        print("Missed tasks:")
        self.print_tasks(tasks)

    def delete_task(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()
        if len(tasks) == 0:
            print("Nothing to delete")
            return
        print("Choose the number of the task you want to delete:")
        self.print_tasks(tasks)
        task_number = int(input())
        task_id = tasks[task_number - 1].id
        rows = self.session.query(Task).filter(Task.id == task_id).all()
        specific_row = rows[0]
        self.session.delete(specific_row)
        self.session.commit()
        print("The task has been deleted!")

    def add_task(self):
        task_name = input("Enter task\n>")
        dead_line_parts = [int(x) for x in input("Enter deadline\n>").split("-")]
        dead_line = datetime.datetime(dead_line_parts[0], dead_line_parts[1], dead_line_parts[2])
        new_task = Task(task=task_name, deadline=dead_line)
        self.session.add(new_task)
        self.session.commit()
        print("The task has been added!\n")

    @staticmethod
    def exit():
        print("Bye!")
        sys.exit()

    def main(self):
        while True:
            current_command = self.print_commands()
            if current_command in self.commands:
                self.commands[current_command][1]()


Program(sessionmaker(bind=engine)()).main()
