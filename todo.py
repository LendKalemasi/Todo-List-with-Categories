import json


class Task:
    
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
    
    def mark_done(self):
        self.done = True
    
    def __str__(self):
        if self.done:
            return f'[x] {self.title}'
        return f'[ ] {self.title}'

class TodoList:
    
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        if name in self.categories:
            raise ValueError(f"Category '{name}' already exists.")
        self.categories[name] = []
    
    def delete_category(self, name):
        if name not in self.categories:
            raise ValueError(f"Category '{name}' doesn't exist.")
        del self.categories[name]
    
    def add_task(self, category, title):
        if category not in self.categories:
            raise ValueError(f"Category '{category}' doesn't exist.")
        for task in self.categories[category]:
            if title == task.title:
                raise ValueError(f"Task with title '{title}' already exists.")
        self.categories[category].append(Task(title))

    def delete_task(self, category, index):
        if category not in self.categories:
            raise ValueError(f"Category '{category}' doesn't exist.")
        tasks = self.categories[category]
        if index < 1 or index > len(tasks):
            raise ValueError(f"Task index '{index}' out of range.")
        tasks.pop(index - 1)

    def complete_task(self, category, index):
        if category not in self.categories:
            raise ValueError(f"Category '{category}' doesn't exist.")
        tasks = self.categories[category]
        if index < 1 or index > len(tasks):
            raise ValueError(f"Task index '{index}' out of range.")
        tasks[index - 1].mark_done()

    
    def view_all(self):
        if not self.categories:
            print('There are no tasks at this moment.')
            return
        for category in self.categories:
            print(f'{category}:')
            for i, task in enumerate(self.categories[category], start=1):
                print(f'  {i}. {task}')

    def view_category(self, name):
        if name not in self.categories:
            raise ValueError(f"Category '{name}' doesn't exist.")
        for i, task in enumerate(self.categories[name], start=1):
            print(f'  {i}. {task}')

    def save(self, filename="data.json"):
        data = {}
        for category, tasks in self.categories.items():
            data[category] = [{"title": task.title, "done": task.done} for task in tasks]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for category, tasks in data.items():
                self.categories[category] = [Task(t["title"], t["done"]) for t in tasks]
        except FileNotFoundError:
            pass


def main():
    todo = TodoList()
    todo.load()
    while True:
        try:
            choice = int(input('''
1 - Add Category
2 - Delete Category
3 - Add task
4 - Delete task
5 - Complete task
6 - View All Tasks
7 - View Category
8 - Quit
''').strip())
            if choice == 1:
                category = input('Choose the category:\n')
                todo.add_category(category)
                todo.save()
            elif choice == 2:
                category = input('Choose the category:\n')
                todo.delete_category(category)
                todo.save()
            elif choice == 3:
                category = input('Choose the category:\n')
                title = input('What is the title of the task?\n')
                todo.add_task(category, title)
                todo.save()
            elif choice == 4:
                category = input('Choose the category:\n')
                tid = int(input('What is the task ID?\n'))
                todo.delete_task(category, tid)
                todo.save()
            elif choice == 5:
                category = input('Choose the category:\n')
                tid = int(input('What is the task ID?\n'))
                todo.complete_task(category, tid)
                todo.save()
            elif choice == 6:
                todo.view_all()
            elif choice == 7:
                category = input('Choose the category:\n')
                todo.view_category(category)
            elif choice == 8:
                return
            else:
                print('Invalid choice.')
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()