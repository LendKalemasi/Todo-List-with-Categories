# Todo List with Categories

A command-line todo list app with category-based task organization. Built in Python using OOP principles.

## Features

- Add and delete categories
- Add, complete, and delete tasks within categories
- View all tasks or filter by category
- Data persists between runs using JSON
- Input validation with descriptive error messages
- Unit tested with pytest

## Project Structure

```
Todo-List-with-Categories/
├── todo.py          # Main application
├── test_todo.py     # Unit tests
├── data.json        # Auto-generated, stores your tasks
├── .gitignore
└── README.md
```

## Getting Started

### Requirements

- Python 3.x

### Run the app

```bash
python todo.py
```

### Run tests

```bash
python -m pytest test_todo.py
```

## Usage

On launch, you get a menu:

```
1 - Add Category
2 - Delete Category
3 - Add Task
4 - Delete Task
5 - Complete Task
6 - View All Tasks
7 - View Category
8 - Quit
```

Enter the number of your choice and follow the prompts.
When deleting or completing a task, enter the task number shown next to it in the list (numbered per category).

## Author

[LendKalemasi](https://github.com/LendKalemasi)